import type { Job, UIState, UserSettings } from "../domain/types";

const KEYS = {
  jobs: "awm_jobs",
  settings: "awm_settings",
  ui: "awm_ui"
};

const read = <T,>(key: string, fallback: T): T => {
  try {
    const raw = localStorage.getItem(key);
    if (!raw) return fallback;
    return JSON.parse(raw) as T;
  } catch {
    return fallback;
  }
};

const write = (key: string, value: unknown) => localStorage.setItem(key, JSON.stringify(value));

export const storage = {
  getJobs: () => read<Job[]>(KEYS.jobs, []),
  saveJobs: (jobs: Job[]) => write(KEYS.jobs, jobs),
  getSettings: (fallback: UserSettings) => read<UserSettings>(KEYS.settings, fallback),
  saveSettings: (settings: UserSettings) => write(KEYS.settings, settings),
  getUI: (fallback: UIState) => read<UIState>(KEYS.ui, fallback),
  saveUI: (ui: UIState) => write(KEYS.ui, ui)
};
