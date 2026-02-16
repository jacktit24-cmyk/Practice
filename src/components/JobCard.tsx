import type { JobView } from "../state/selectors";
import { formatCurrency, formatDate } from "../services/businessDays";
import { BoolBadge, DueBadge } from "./Badges";

export function JobCard({ job, onOpen, onComplete }: { job: JobView; onOpen: () => void; onComplete: () => void }) {
  return (
    <article className="card" onClick={onOpen}>
      <div className="row-between">
        <h3>{job.propertyName}</h3>
        <DueBadge daysLeft={job.businessDaysLeft} />
      </div>
      <p>{job.clientName}</p>
      <div className="chip">{job.jobNumber}</div>
      <div className="meta-grid">
        <span>{formatCurrency(job.fee)}</span>
        <span>{formatDate(job.dueDateISO)}</span>
        <span>{job.reportWriter}</span>
      </div>
      <div className="status-row">
        <BoolBadge value={job.contactedPropertyContact.value} label="Contacted" />
        <BoolBadge value={job.propertyContactReplied.value} label="Replied" />
      </div>
      <button
        className="btn-secondary"
        onClick={(e) => {
          e.stopPropagation();
          onComplete();
        }}
      >
        {job.isCompleted ? "Uncomplete" : "Mark Completed"}
      </button>
    </article>
  );
}
