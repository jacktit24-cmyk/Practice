import { useJobsStore } from "../state/useJobsStore";
import { toJobView } from "../state/selectors";

export function JobDetailDrawer() {
  const { jobs, selectedJobId, setSelectedJob, answerPrompt, answerInfoReceived, setFrontEndReason } = useJobsStore();
  const job = jobs.find((j) => j.id === selectedJobId);
  if (!job) return null;
  const view = toJobView(job);

  return (
    <aside className="drawer">
      <button className="btn-link" onClick={() => setSelectedJob(null)}>Close</button>
      <h2>{view.propertyName}</h2>
      <p>{view.clientName} · #{view.jobNumber}</p>
      <h4>Daily Check-In</h4>
      <div className="prompt">
        <p>Have you contacted the property contact?</p>
        <button className="btn-secondary" onClick={() => answerPrompt(view.id, "contactedPropertyContact", true)}>Yes</button>
        <button className="btn-secondary" onClick={() => answerPrompt(view.id, "contactedPropertyContact", false)}>No</button>
      </div>
      <div className="prompt">
        <p>Have they replied?</p>
        <button className="btn-secondary" onClick={() => answerPrompt(view.id, "propertyContactReplied", true)}>Yes</button>
        <button className="btn-secondary" onClick={() => answerPrompt(view.id, "propertyContactReplied", false)}>No</button>
      </div>
      <div className="prompt">
        <p>Have you received necessary information?</p>
        <button className="btn-secondary" onClick={() => answerInfoReceived(view.id, true)}>Yes</button>
        <button className="btn-secondary" onClick={() => answerInfoReceived(view.id, false)}>No</button>
      </div>
      <div className="prompt">
        <p>Is front end complete?</p>
        <button className="btn-secondary" onClick={() => answerPrompt(view.id, "frontEndComplete", true)}>Yes</button>
        <button className="btn-secondary" onClick={() => answerPrompt(view.id, "frontEndComplete", false)}>No</button>
        {view.frontEndComplete.value === false && (
          <textarea
            placeholder="Why not? What do you need to do?"
            value={view.frontEndIncompleteReason ?? ""}
            onChange={(e) => setFrontEndReason(view.id, e.target.value)}
          />
        )}
      </div>
      {view.frontEndIncompleteReason && <p className="reason">Reason: {view.frontEndIncompleteReason}</p>}
    </aside>
  );
}
