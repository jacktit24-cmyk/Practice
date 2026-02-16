import { useEffect } from "react";
import { RouterProvider } from "react-router-dom";
import { router } from "./router";
import { useJobsStore } from "../state/useJobsStore";

export default function App() {
  const hydrate = useJobsStore((s) => s.hydrate);
  useEffect(() => {
    hydrate();
  }, [hydrate]);

  return <RouterProvider router={router} />;
}
