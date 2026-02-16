import type { ImportRowError, Job } from "../domain/types";
import { toDateOnlyISO } from "./businessDays";

type ImportResult = {
  jobs: Job[];
  errors: ImportRowError[];
  missingColumns: string[];
};

const REQUIRED = ["property name", "client name", "job number", "report writer", "fee", "due date"];

const normalizeHeader = (s: string) => s.toLowerCase().replace(/[_-]/g, " ").replace(/\s+/g, " ").trim();

const parseCSVLine = (line: string): string[] => {
  const result: string[] = [];
  let current = "";
  let inQuotes = false;

  for (let i = 0; i < line.length; i += 1) {
    const ch = line[i];
    if (ch === '"') {
      if (inQuotes && line[i + 1] === '"') {
        current += '"';
        i += 1;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (ch === "," && !inQuotes) {
      result.push(current.trim());
      current = "";
    } else {
      current += ch;
    }
  }
  result.push(current.trim());
  return result;
};

const parseCurrency = (v: string) => Number(v.replace(/[$,\s]/g, ""));

const parseDate = (raw: string): string | null => {
  const val = raw.trim();
  if (!val) return null;
  const direct = new Date(val);
  if (!Number.isNaN(direct.getTime())) return toDateOnlyISO(direct);

  const m = val.match(/^(\d{1,2})\/(\d{1,2})\/(\d{2,4})$/);
  if (!m) return null;
  const month = Number(m[1]) - 1;
  const day = Number(m[2]);
  const year = Number(m[3].length === 2 ? `20${m[3]}` : m[3]);
  const dt = new Date(year, month, day);
  if (Number.isNaN(dt.getTime())) return null;
  return toDateOnlyISO(dt);
};

const toUuid = () => crypto.randomUUID();

export const importJobsFromCSV = (text: string, existingJobs: Job[]): ImportResult => {
  const lines = text.split(/\r?\n/).filter((l) => l.trim().length > 0);
  if (lines.length < 2) return { jobs: [], errors: [{ rowNumber: 0, message: "CSV has no data rows." }], missingColumns: [] };

  const headers = parseCSVLine(lines[0]);
  const indexMap = new Map<string, number>();
  headers.forEach((header, i) => indexMap.set(normalizeHeader(header), i));

  const missingColumns = REQUIRED.filter((required) => !indexMap.has(required));
  if (missingColumns.length) return { jobs: [], errors: [], missingColumns };

  const now = new Date();
  const importBatchId = `batch-${now.toISOString()}`;
  const existingMap = new Map(existingJobs.map((j) => [j.jobNumber, j]));

  const jobs: Job[] = [];
  const errors: ImportRowError[] = [];

  for (let i = 1; i < lines.length; i += 1) {
    const cols = parseCSVLine(lines[i]);
    const get = (field: string) => cols[indexMap.get(field) ?? -1]?.trim() ?? "";

    const propertyName = get("property name");
    const clientName = get("client name");
    const jobNumber = get("job number");
    const reportWriter = get("report writer");
    const fee = parseCurrency(get("fee"));
    const dueDateISO = parseDate(get("due date"));
    const dateEnteredRaw = get("date entered");
    const dateEnteredISO = dateEnteredRaw ? new Date(`${parseDate(dateEnteredRaw)}T09:00:00`).toISOString() : now.toISOString();

    const missingValues = [
      ["Property Name", propertyName],
      ["Client Name", clientName],
      ["Job Number", jobNumber],
      ["Report Writer", reportWriter]
    ].filter(([, v]) => !v);

    if (missingValues.length || Number.isNaN(fee) || !dueDateISO) {
      errors.push({ rowNumber: i + 1, message: `Invalid row. Missing/invalid: ${missingValues.map(([k]) => k).join(", ") || "Fee/Due Date"}` });
    }

    const base: Job = {
      id: toUuid(),
      propertyName: propertyName || "Needs Attention",
      clientName: clientName || "Needs Attention",
      jobNumber: jobNumber || `INVALID-${i + 1}`,
      reportWriter: reportWriter || "Unassigned",
      fee: Number.isNaN(fee) ? 0 : fee,
      dueDateISO: dueDateISO ?? toDateOnlyISO(now),
      dateEnteredISO,
      createdAtISO: now.toISOString(),
      updatedAtISO: now.toISOString(),
      contactedPropertyContact: { value: null, answeredAtISO: null },
      propertyContactReplied: { value: null, answeredAtISO: null },
      infoReceived: { value: null, answeredAtISO: null, lastPromptedOn: null },
      frontEndComplete: { value: null, answeredAtISO: null },
      frontEndIncompleteReason: null,
      isCompleted: false,
      completedAtISO: null,
      importBatchId
    };

    const dedupeExisting = existingMap.get(base.jobNumber);
    const dedupeImported = jobs.find((j) => j.jobNumber === base.jobNumber);
    const target = dedupeImported ?? dedupeExisting;

    if (target) {
      const identical = JSON.stringify({ ...target, id: undefined, createdAtISO: undefined, updatedAtISO: undefined }) === JSON.stringify({ ...base, id: undefined, createdAtISO: undefined, updatedAtISO: undefined });
      if (identical) continue;
      const merged = {
        ...target,
        ...base,
        id: target.id,
        createdAtISO: target.createdAtISO,
        importConflicts: [...(target.importConflicts ?? []), `Conflict in batch ${importBatchId}; last row won.`],
        updatedAtISO: now.toISOString()
      };
      const idx = jobs.findIndex((j) => j.jobNumber === merged.jobNumber);
      if (idx >= 0) jobs[idx] = merged;
      else jobs.push(merged);
    } else {
      jobs.push(base);
    }
  }

  return { jobs, errors, missingColumns };
};
