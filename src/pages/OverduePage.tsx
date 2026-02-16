import { TopBar } from "../layout/TopBar";
import { useJobsStore } from "../state/useJobsStore";
import { getOverdue } from "../state/selectors";
import { JobListTable } from "../components/JobListTable";
import { EmptyState } from "../components/EmptyState";

export function OverduePage() {
  const { jobs, setSelectedJob } = useJobsStore();
  const overdue = getOverdue(jobs);
  return <><TopBar title="Overdue" />{overdue.length ? <JobListTable jobs={overdue} onOpen={setSelectedJob} /> : <EmptyState title="No overdue jobs" description="Great work staying ahead." />}</>;
}
