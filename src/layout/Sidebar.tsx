import { NavLink } from "react-router-dom";

const items = [
  ["/", "Dashboard"],
  ["/jobs", "All Jobs"],
  ["/due-soon", "Due Soon"],
  ["/overdue", "Overdue"],
  ["/completed", "Completed"],
  ["/settings", "Settings"]
];

export function Sidebar() {
  return (
    <aside className="sidebar">
      <h1>Appraisal Workflow</h1>
      <nav>
        {items.map(([to, label]) => (
          <NavLink key={to} to={to} className={({ isActive }) => (isActive ? "nav active" : "nav")} end={to === "/"}>
            {label}
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}
