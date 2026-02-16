import type { Job } from "../domain/types";
import { getAlerts, getAutoStatus } from "../domain/status";
import { businessDaysLeft, isOverdue, isWithinNextBusinessDays, parseISODateOnly } from "../services/businessDays";

export type JobView = Job & {
  statusAuto: ReturnType<typeof getAutoStatus>;
  statusEffective: ReturnType<typeof getAutoStatus>;
  businessDaysLeft: number;
  alerts: ReturnType<typeof getAlerts>;
};

export const toJobView = (job: Job): JobView => {
  const status = getAutoStatus(job);
  return {
    ...job,
    statusAuto: status,
    statusEffective: status,
    businessDaysLeft: businessDaysLeft(job.dueDateISO),
    alerts: getAlerts(job)
  };
};

export const getAllViews = (jobs: Job[]) => jobs.map(toJobView);
export const getDueSoon = (jobs: Job[]) => jobs.filter((j) => !j.isCompleted && isWithinNextBusinessDays(j.dueDateISO, 5)).map(toJobView);
export const getOverdue = (jobs: Job[]) => jobs.filter((j) => !j.isCompleted && isOverdue(j.dueDateISO)).map(toJobView);
export const getCompleted = (jobs: Job[]) => jobs.filter((j) => j.isCompleted).map(toJobView);

export const applySearchFilterSort = (
  jobs: JobView[],
  opts: { search: string; writer: string; status: string; due: string; sortBy: string; sortDir: "asc" | "desc" }
) => {
  const search = opts.search.toLowerCase();
  const filtered = jobs.filter((j) => {
    const matchesSearch = !search || [j.propertyName, j.clientName, j.jobNumber].some((v) => v.toLowerCase().includes(search));
    const matchesWriter = opts.writer === "All" || j.reportWriter === opts.writer;
    const matchesStatus = opts.status === "All" || j.statusEffective === opts.status;
    const matchesDue =
      opts.due === "All" ||
      (opts.due === "Due Soon" && j.businessDaysLeft >= 0 && j.businessDaysLeft <= 5) ||
      (opts.due === "Overdue" && j.businessDaysLeft < 0) ||
      (opts.due === "Today" && j.businessDaysLeft === 0);
    return matchesSearch && matchesWriter && matchesStatus && matchesDue;
  });

  const sortFactor = opts.sortDir === "asc" ? 1 : -1;
  filtered.sort((a, b) => {
    const compareMap = {
      dueDate: parseISODateOnly(a.dueDateISO).getTime() - parseISODateOnly(b.dueDateISO).getTime(),
      fee: a.fee - b.fee,
      writer: a.reportWriter.localeCompare(b.reportWriter),
      dateEntered: new Date(a.dateEnteredISO).getTime() - new Date(b.dateEnteredISO).getTime()
    };
    return (compareMap[opts.sortBy as keyof typeof compareMap] || 0) * sortFactor;
  });

  return filtered;
};
