import { Outlet } from "react-router-dom";
import { Sidebar } from "./Sidebar";
import { JobDetailDrawer } from "../components/JobDetailDrawer";

export function AppShell() {
  return (
    <div className="shell">
      <Sidebar />
      <main className="main">
        <Outlet />
      </main>
      <JobDetailDrawer />
    </div>
  );
}
