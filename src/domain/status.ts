import type { Alert, Job, JobStatus } from "./types";
import { businessDaysLeft, isOverdue, toDateOnlyISO } from "../services/businessDays";

const ageDays = (dateEnteredISO: string, now = new Date()) => {
  const ms = now.getTime() - new Date(dateEnteredISO).getTime();
  return ms / (1000 * 60 * 60 * 24);
};

export const getAutoStatus = (job: Job, now = new Date()): JobStatus => {
  const age = ageDays(job.dateEnteredISO, now);
  const bLeft = businessDaysLeft(job.dueDateISO, now);

  if (job.isCompleted) return "Completed";
  if (isOverdue(job.dueDateISO, now)) return "Overdue";
  if (bLeft >= 0 && bLeft <= 5) return "Due Soon";
  if (age >= 7 && job.frontEndComplete.value !== true) return "Front-End Pending";
  if (job.infoReceived.value !== true) return "Awaiting Info";
  if (age < 2 && job.infoReceived.value === null && job.contactedPropertyContact.value === null) return "New";
  return "In Progress";
};

export const getAlerts = (job: Job, now = new Date()): Alert[] => {
  if (job.isCompleted) return [];
  const alerts: Alert[] = [];
  const dateKey = toDateOnlyISO(now);
  const age = ageDays(job.dateEnteredISO, now);
  const bLeft = businessDaysLeft(job.dueDateISO, now);

  if (age >= 2 && job.contactedPropertyContact.value !== true) {
    alerts.push({
      id: `${job.id}-followup`,
      type: "FOLLOW_UP",
      severity: "WARN",
      message: "Have you contacted the property contact?",
      jobId: job.id,
      createdOn: dateKey
    });
  }

  if (age >= 2 && job.contactedPropertyContact.value === true && job.propertyContactReplied.value !== true) {
    alerts.push({
      id: `${job.id}-reply`,
      type: "FOLLOW_UP",
      severity: "WARN",
      message: "Have they replied?",
      jobId: job.id,
      createdOn: dateKey
    });
  }

  if (job.infoReceived.value !== true) {
    alerts.push({
      id: `${job.id}-info`,
      type: "INFO_CHECK",
      severity: "INFO",
      message: "Have you received necessary information?",
      jobId: job.id,
      createdOn: dateKey
    });
  }

  if (age >= 7 && job.frontEndComplete.value !== true) {
    alerts.push({
      id: `${job.id}-frontend`,
      type: "FRONT_END",
      severity: "URGENT",
      message: "Is front end complete?",
      jobId: job.id,
      createdOn: dateKey
    });
  }

  if (isOverdue(job.dueDateISO, now)) {
    alerts.push({
      id: `${job.id}-overdue`,
      type: "OVERDUE",
      severity: "URGENT",
      message: "Job is overdue",
      jobId: job.id,
      createdOn: dateKey
    });
  } else if (bLeft <= 5) {
    alerts.push({
      id: `${job.id}-due`,
      type: "DUE_WARNING",
      severity: bLeft <= 2 ? "URGENT" : "WARN",
      message: `${bLeft} business day(s) remaining`,
      jobId: job.id,
      createdOn: dateKey
    });
  }

  return alerts;
};

export const getDueBadgeClass = (daysLeft: number) => {
  if (daysLeft < 0) return "badge-overdue";
  if (daysLeft === 1) return "badge-pulse";
  if (daysLeft === 2) return "badge-red";
  if (daysLeft === 3) return "badge-orange";
  if (daysLeft <= 5) return "badge-yellow";
  return "badge-neutral";
};
