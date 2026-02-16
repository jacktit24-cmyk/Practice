import { TopBar } from "../layout/TopBar";
import { useJobsStore } from "../state/useJobsStore";

export function SettingsPage() {
  const { settings, updateSettings } = useJobsStore();
  return (
    <>
      <TopBar title="Settings" />
      <section className="panel settings-grid">
        <label>
          Business day calculation
          <select value={settings.businessDaysExcludeWeekends ? "exclude" : "include"} onChange={(e) => updateSettings({ businessDaysExcludeWeekends: e.target.value === "exclude" })}>
            <option value="exclude">Exclude weekends</option>
            <option value="include">Include weekends</option>
          </select>
        </label>
        <label>
          Daily prompt time
          <input type="time" value={settings.dailyPromptTime} onChange={(e) => updateSettings({ dailyPromptTime: e.target.value })} />
        </label>
        <label>
          Dedupe strategy
          <select value={settings.dedupeStrategy} onChange={() => updateSettings({ dedupeStrategy: "last-row-wins" })}><option value="last-row-wins">Last row wins</option></select>
        </label>
        <label>
          Theme density
          <select value={settings.density} onChange={(e) => updateSettings({ density: e.target.value as "comfortable" | "compact" })}>
            <option value="comfortable">Comfortable</option>
            <option value="compact">Compact</option>
          </select>
        </label>
      </section>
    </>
  );
}
