import type { JobView } from "../state/selectors";
import { JobCard } from "./JobCard";

const order = ["New", "In Progress", "Awaiting Info", "Front-End Pending", "Due Soon", "Overdue", "Completed"] as const;

export function Board({ jobs, onOpen, onComplete }: { jobs: JobView[]; onOpen: (id: string) => void; onComplete: (id: string) => void }) {
  return (
    <div className="board">
      {order.map((status) => {
        const col = jobs.filter((j) => j.statusEffective === status);
        return (
          <section className="column" key={status}>
            <header className="row-between">
              <h4>{status}</h4>
              <span>{col.length}</span>
            </header>
            {col.map((job) => (
              <JobCard key={job.id} job={job} onOpen={() => onOpen(job.id)} onComplete={() => onComplete(job.id)} />
            ))}
          </section>
        );
      })}
    </div>
  );
}
