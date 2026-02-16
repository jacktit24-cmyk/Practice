import { TopBar } from "../layout/TopBar";
import { useJobsStore } from "../state/useJobsStore";
import { getCompleted } from "../state/selectors";
import { JobListTable } from "../components/JobListTable";
import { EmptyState } from "../components/EmptyState";

export function CompletedPage() {
  const { jobs, setSelectedJob } = useJobsStore();
  const completed = getCompleted(jobs);
  return <><TopBar title="Completed" />{completed.length ? <JobListTable jobs={completed} onOpen={setSelectedJob} /> : <EmptyState title="No completed jobs" description="Completed jobs will appear here." />}</>;
}
