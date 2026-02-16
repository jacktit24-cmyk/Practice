import type { JobView } from "../state/selectors";

export function DueTimeline({ jobs }: { jobs: JobView[] }) {
  const buckets = {
    Today: jobs.filter((j) => j.businessDaysLeft === 0).length,
    "This Week": jobs.filter((j) => j.businessDaysLeft >= 1 && j.businessDaysLeft <= 5).length,
    "Next Week": jobs.filter((j) => j.businessDaysLeft >= 6 && j.businessDaysLeft <= 10).length,
    Later: jobs.filter((j) => j.businessDaysLeft > 10).length
  };
  const max = Math.max(...Object.values(buckets), 1);
  return (
    <div className="timeline">
      {Object.entries(buckets).map(([name, value]) => (
        <div key={name} className="timeline-row">
          <span>{name}</span>
          <div className="bar-wrap"><div className="bar" style={{ width: `${(value / max) * 100}%` }} /></div>
          <strong>{value}</strong>
        </div>
      ))}
    </div>
  );
}
