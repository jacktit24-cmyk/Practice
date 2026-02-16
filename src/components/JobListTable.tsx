import type { JobView } from "../state/selectors";
import { formatCurrency, formatDate } from "../services/businessDays";
import { DueBadge } from "./Badges";

export function JobListTable({ jobs, onOpen }: { jobs: JobView[]; onOpen: (id: string) => void }) {
  return (
    <table className="jobs-table">
      <thead>
        <tr>
          <th>Property</th><th>Client</th><th>Job #</th><th>Writer</th><th>Fee</th><th>Due</th><th>Status</th><th>Alerts</th>
        </tr>
      </thead>
      <tbody>
        {jobs.map((job) => (
          <tr key={job.id} onClick={() => onOpen(job.id)}>
            <td>{job.propertyName}</td>
            <td>{job.clientName}</td>
            <td><code>{job.jobNumber}</code></td>
            <td>{job.reportWriter}</td>
            <td>{formatCurrency(job.fee)}</td>
            <td>{formatDate(job.dueDateISO)} <DueBadge daysLeft={job.businessDaysLeft} /></td>
            <td>{job.statusEffective}</td>
            <td>{job.alerts.length}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
