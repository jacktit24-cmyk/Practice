import { TopBar } from "../layout/TopBar";
import { CsvUpload } from "../components/CsvUpload";
import { useJobsStore } from "../state/useJobsStore";
import { applySearchFilterSort, getAllViews } from "../state/selectors";
import { Board } from "../components/Board";
import { JobListTable } from "../components/JobListTable";
import { EmptyState } from "../components/EmptyState";

export function AllJobsPage() {
  const { jobs, ui, updateUI, setSelectedJob, markCompleted } = useJobsStore();
  const views = applySearchFilterSort(getAllViews(jobs), {
    search: ui.search,
    writer: ui.writerFilter,
    status: ui.statusFilter,
    due: ui.dueFilter,
    sortBy: ui.sortBy,
    sortDir: ui.sortDir
  });
  const writers = Array.from(new Set(jobs.map((j) => j.reportWriter))).sort();

  return (
    <>
      <TopBar
        title="All Jobs"
        actions={
          <>
            <CsvUpload />
            <button className="btn-secondary" onClick={() => updateUI({ allJobsView: ui.allJobsView === "board" ? "list" : "board" })}>
              {ui.allJobsView === "board" ? "List View" : "Board View"}
            </button>
          </>
        }
      />

      <section className="panel controls">
        <input placeholder="Search property/client/job#" value={ui.search} onChange={(e) => updateUI({ search: e.target.value })} />
        <select value={ui.writerFilter} onChange={(e) => updateUI({ writerFilter: e.target.value })}><option>All</option>{writers.map((w) => <option key={w}>{w}</option>)}</select>
        <select value={ui.statusFilter} onChange={(e) => updateUI({ statusFilter: e.target.value as typeof ui.statusFilter })}>
          {['All','New','In Progress','Awaiting Info','Front-End Pending','Due Soon','Overdue','Completed'].map((s)=><option key={s}>{s}</option>)}
        </select>
        <select value={ui.dueFilter} onChange={(e) => updateUI({ dueFilter: e.target.value as typeof ui.dueFilter })}>
          {['All','Today','Due Soon','Overdue'].map((s)=><option key={s}>{s}</option>)}
        </select>
      </section>

      {views.length === 0 ? (
        <EmptyState title="No jobs found" description="Upload a CSV or adjust filters." />
      ) : ui.allJobsView === "board" ? (
        <Board jobs={views} onOpen={setSelectedJob} onComplete={(id) => {
          const job = jobs.find((j) => j.id === id);
          if (job) markCompleted(id, !job.isCompleted);
        }} />
      ) : (
        <JobListTable jobs={views} onOpen={setSelectedJob} />
      )}
    </>
  );
}
