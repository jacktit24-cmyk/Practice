import { useMemo, useState } from "react";
import { useJobsStore } from "../state/useJobsStore";
import { getAllViews } from "../state/selectors";

export function PromptCenter() {
  const [open, setOpen] = useState(false);
  const jobs = useJobsStore((s) => s.jobs);
  const setSelected = useJobsStore((s) => s.setSelectedJob);
  const promptJobs = useMemo(() => getAllViews(jobs).filter((j) => j.alerts.some((a) => ["FOLLOW_UP", "INFO_CHECK", "FRONT_END"].includes(a.type))), [jobs]);

  return (
    <div>
      <button className="btn-secondary" onClick={() => setOpen((o) => !o)}>🔔 Daily Check-in ({promptJobs.length})</button>
      {open && (
        <div className="alerts-panel">
          {promptJobs.length === 0 ? <p>All clear today.</p> : promptJobs.map((j) => <button key={j.id} className="alert-item" onClick={() => setSelected(j.id)}>{j.propertyName} · {j.alerts[0]?.message}</button>)}
        </div>
      )}
    </div>
  );
}
