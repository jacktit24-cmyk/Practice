import { create } from "zustand";
import type { Job, UIState, UserSettings } from "../domain/types";
import { storage } from "../services/storage";
import { importJobsFromCSV } from "../services/csvImport";
import { toDateOnlyISO } from "../services/businessDays";

type Store = {
  jobs: Job[];
  selectedJobId: string | null;
  importErrors: string[];
  settings: UserSettings;
  ui: UIState;
  hydrate: () => void;
  importCsvText: (csv: string) => { success: boolean; message: string };
  setSelectedJob: (jobId: string | null) => void;
  updateJob: (jobId: string, patch: Partial<Job>) => void;
  answerPrompt: (jobId: string, field: "contactedPropertyContact" | "propertyContactReplied" | "frontEndComplete", value: boolean) => void;
  answerInfoReceived: (jobId: string, value: boolean) => void;
  markCompleted: (jobId: string, value: boolean) => void;
  setFrontEndReason: (jobId: string, reason: string) => void;
  updateSettings: (patch: Partial<UserSettings>) => void;
  updateUI: (patch: Partial<UIState>) => void;
};

const defaultSettings: UserSettings = {
  businessDaysExcludeWeekends: true,
  dailyPromptTime: "09:00",
  dedupeStrategy: "last-row-wins",
  density: "comfortable",
  defaultView: "board"
};

const defaultUI: UIState = {
  search: "",
  writerFilter: "All",
  statusFilter: "All",
  dueFilter: "All",
  sortBy: "dueDate",
  sortDir: "asc",
  allJobsView: "board"
};

export const useJobsStore = create<Store>((set, get) => ({
  jobs: [],
  selectedJobId: null,
  importErrors: [],
  settings: defaultSettings,
  ui: defaultUI,
  hydrate: () => {
    set({ jobs: storage.getJobs(), settings: storage.getSettings(defaultSettings), ui: storage.getUI(defaultUI) });
  },
  importCsvText: (csv: string) => {
    const { jobs: imported, errors, missingColumns } = importJobsFromCSV(csv, get().jobs);
    if (missingColumns.length) {
      const message = `Missing required columns: ${missingColumns.join(", ")}`;
      set({ importErrors: [message] });
      return { success: false, message };
    }

    const mergedByJobNumber = new Map(get().jobs.map((j) => [j.jobNumber, j]));
    imported.forEach((j) => mergedByJobNumber.set(j.jobNumber, j));
    const nextJobs = Array.from(mergedByJobNumber.values());
    storage.saveJobs(nextJobs);
    set({ jobs: nextJobs, importErrors: errors.map((e) => `Row ${e.rowNumber}: ${e.message}`) });
    return { success: true, message: `Imported ${imported.length} rows with ${errors.length} warning(s).` };
  },
  setSelectedJob: (jobId) => set({ selectedJobId: jobId }),
  updateJob: (jobId, patch) => {
    const next = get().jobs.map((j) => (j.id === jobId ? { ...j, ...patch, updatedAtISO: new Date().toISOString() } : j));
    storage.saveJobs(next);
    set({ jobs: next });
  },
  answerPrompt: (jobId, field, value) => {
    const next = get().jobs.map((j) =>
      j.id === jobId ? { ...j, [field]: { value, answeredAtISO: new Date().toISOString() }, updatedAtISO: new Date().toISOString() } : j
    );
    storage.saveJobs(next);
    set({ jobs: next });
  },
  answerInfoReceived: (jobId, value) => {
    const today = toDateOnlyISO(new Date());
    const next = get().jobs.map((j) =>
      j.id === jobId
        ? {
            ...j,
            infoReceived: { value, answeredAtISO: new Date().toISOString(), lastPromptedOn: today },
            updatedAtISO: new Date().toISOString()
          }
        : j
    );
    storage.saveJobs(next);
    set({ jobs: next });
  },
  markCompleted: (jobId, value) => {
    const next = get().jobs.map((j) =>
      j.id === jobId
        ? {
            ...j,
            isCompleted: value,
            completedAtISO: value ? new Date().toISOString() : null,
            updatedAtISO: new Date().toISOString()
          }
        : j
    );
    storage.saveJobs(next);
    set({ jobs: next });
  },
  setFrontEndReason: (jobId, reason) => {
    const next = get().jobs.map((j) => (j.id === jobId ? { ...j, frontEndIncompleteReason: reason, updatedAtISO: new Date().toISOString() } : j));
    storage.saveJobs(next);
    set({ jobs: next });
  },
  updateSettings: (patch) => {
    const next = { ...get().settings, ...patch };
    storage.saveSettings(next);
    set({ settings: next });
  },
  updateUI: (patch) => {
    const next = { ...get().ui, ...patch };
    storage.saveUI(next);
    set({ ui: next });
  }
}));
