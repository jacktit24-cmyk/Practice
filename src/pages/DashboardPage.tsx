import { TopBar } from "../layout/TopBar";
import { CsvUpload } from "../components/CsvUpload";
import { useJobsStore } from "../state/useJobsStore";
import { getAllViews } from "../state/selectors";
import { KpiTiles } from "../components/KpiTiles";
import { DueTimeline } from "../components/DueTimeline";
import { EmptyState } from "../components/EmptyState";

export function DashboardPage() {
  const jobs = useJobsStore((s) => s.jobs);
  const views = getAllViews(jobs);

  return (
    <>
      <TopBar title="Dashboard" actions={<CsvUpload />} />
      {views.length === 0 ? <EmptyState title="No jobs yet" description="Upload a CSV to start tracking appraisal jobs." /> : (
        <>
          <KpiTiles jobs={views} />
          <section className="panel">
            <h3>Due Date Timeline</h3>
            <DueTimeline jobs={views.filter((j) => !j.isCompleted)} />
          </section>
        </>
      )}
    </>
  );
}
