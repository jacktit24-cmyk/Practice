export type PromptAnswer = {
  value: boolean | null;
  answeredAtISO: string | null;
};

export type InfoAnswer = PromptAnswer & {
  lastPromptedOn: string | null;
};

export type JobStatus =
  | "Completed"
  | "Overdue"
  | "Due Soon"
  | "Front-End Pending"
  | "Awaiting Info"
  | "In Progress"
  | "New";

export type AlertType = "FOLLOW_UP" | "INFO_CHECK" | "FRONT_END" | "DUE_WARNING" | "OVERDUE";
export type AlertSeverity = "INFO" | "WARN" | "URGENT";

export type Alert = {
  id: string;
  type: AlertType;
  severity: AlertSeverity;
  message: string;
  jobId: string;
  createdOn: string;
  dismissed?: boolean;
};

export type Job = {
  id: string;
  propertyName: string;
  clientName: string;
  jobNumber: string;
  reportWriter: string;
  fee: number;
  dueDateISO: string;
  dateEnteredISO: string;
  createdAtISO: string;
  updatedAtISO: string;
  contactedPropertyContact: PromptAnswer;
  propertyContactReplied: PromptAnswer;
  infoReceived: InfoAnswer;
  frontEndComplete: PromptAnswer;
  frontEndIncompleteReason: string | null;
  isCompleted: boolean;
  completedAtISO: string | null;
  importBatchId: string;
  importConflicts?: string[];
};

export type ImportRowError = {
  rowNumber: number;
  message: string;
};

export type UserSettings = {
  businessDaysExcludeWeekends: boolean;
  dailyPromptTime: string;
  dedupeStrategy: "last-row-wins";
  density: "comfortable" | "compact";
  defaultView: "board" | "list";
};

export type UIState = {
  search: string;
  writerFilter: string;
  statusFilter: JobStatus | "All";
  dueFilter: "All" | "Due Soon" | "Overdue" | "Today";
  sortBy: "dueDate" | "fee" | "writer" | "dateEntered";
  sortDir: "asc" | "desc";
  allJobsView: "board" | "list";
};
