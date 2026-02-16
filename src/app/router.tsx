import { createBrowserRouter } from "react-router-dom";
import { AppShell } from "../layout/AppShell";
import { DashboardPage } from "../pages/DashboardPage";
import { AllJobsPage } from "../pages/AllJobsPage";
import { DueSoonPage } from "../pages/DueSoonPage";
import { OverduePage } from "../pages/OverduePage";
import { CompletedPage } from "../pages/CompletedPage";
import { SettingsPage } from "../pages/SettingsPage";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <AppShell />,
    children: [
      { index: true, element: <DashboardPage /> },
      { path: "jobs", element: <AllJobsPage /> },
      { path: "due-soon", element: <DueSoonPage /> },
      { path: "overdue", element: <OverduePage /> },
      { path: "completed", element: <CompletedPage /> },
      { path: "settings", element: <SettingsPage /> }
    ]
  }
]);
