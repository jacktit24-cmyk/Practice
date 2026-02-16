import type { JobView } from "../state/selectors";
import { formatCurrency, parseISODateOnly } from "../services/businessDays";

export function KpiTiles({ jobs }: { jobs: JobView[] }) {
  const now = new Date();
  const thisMonth = now.getMonth();
  const thisYear = now.getFullYear();
  const active = jobs.filter((j) => !j.isCompleted);
  const dueThisWeek = active.filter((j) => j.businessDaysLeft >= 0 && j.businessDaysLeft <= 5).length;
  const overdue = active.filter((j) => j.businessDaysLeft < 0).length;
  const pipeline = active.reduce((sum, j) => sum + j.fee, 0);
  const monthFees = active
    .filter((j) => {
      const d = parseISODateOnly(j.dueDateISO);
      return d.getMonth() === thisMonth && d.getFullYear() === thisYear;
    })
    .reduce((sum, j) => sum + j.fee, 0);

  const items = [
    ["Total Active Jobs", active.length.toString()],
    ["Jobs Due This Week", dueThisWeek.toString()],
    ["Overdue Jobs", overdue.toString()],
    ["Fees in Pipeline", formatCurrency(pipeline)],
    ["Fees Due This Month", formatCurrency(monthFees)]
  ];

  return <div className="kpi-grid">{items.map(([k, v]) => <div className="kpi" key={k}><span>{k}</span><strong>{v}</strong></div>)}</div>;
}
