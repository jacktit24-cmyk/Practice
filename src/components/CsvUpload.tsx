import { useState } from "react";
import { useJobsStore } from "../state/useJobsStore";

export function CsvUpload() {
  const importCsvText = useJobsStore((s) => s.importCsvText);
  const importErrors = useJobsStore((s) => s.importErrors);
  const [message, setMessage] = useState<string>("");

  return (
    <div>
      <label className="btn-primary" htmlFor="csv-upload">Upload CSV</label>
      <input
        id="csv-upload"
        type="file"
        accept=".csv,text/csv"
        style={{ display: "none" }}
        onChange={async (e) => {
          const file = e.target.files?.[0];
          if (!file) return;
          const text = await file.text();
          const result = importCsvText(text);
          setMessage(result.message);
        }}
      />
      {message && <p className="small-note">{message}</p>}
      {importErrors.length > 0 && <ul className="error-list">{importErrors.map((err) => <li key={err}>{err}</li>)}</ul>}
    </div>
  );
}
