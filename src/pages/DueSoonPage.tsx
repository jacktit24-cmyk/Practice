import { TopBar } from "../layout/TopBar";
import { useJobsStore } from "../state/useJobsStore";
import { getDueSoon } from "../state/selectors";
import { JobListTable } from "../components/JobListTable";
import { EmptyState } from "../components/EmptyState";

export function DueSoonPage() {
  const { jobs, setSelectedJob } = useJobsStore();
  const dueSoon = getDueSoon(jobs);
  return <><TopBar title="Due Soon" />{dueSoon.length ? <JobListTable jobs={dueSoon} onOpen={setSelectedJob} /> : <EmptyState title="No jobs due soon" description="Nothing within 5 business days." />}</>;
}
