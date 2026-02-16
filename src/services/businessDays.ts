const isWeekend = (date: Date) => {
  const d = date.getDay();
  return d === 0 || d === 6;
};

export const toDateOnlyISO = (date: Date) => {
  const local = new Date(date.getTime() - date.getTimezoneOffset() * 60000);
  return local.toISOString().slice(0, 10);
};

export const parseISODateOnly = (iso: string) => {
  const [y, m, d] = iso.split("-").map(Number);
  return new Date(y, (m || 1) - 1, d || 1, 0, 0, 0, 0);
};

/**
 * Business-day definition for MVP:
 * - due today => 0
 * - start is today exclusive, due date inclusive.
 * - weekends excluded, holidays not excluded.
 */
export const businessDaysLeft = (dueDateISO: string, now = new Date()) => {
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const due = parseISODateOnly(dueDateISO);

  if (due.getTime() === today.getTime()) return 0;
  const direction = due > today ? 1 : -1;

  let cursor = new Date(today);
  let count = 0;

  while (cursor.getTime() !== due.getTime()) {
    cursor.setDate(cursor.getDate() + direction);
    if (!isWeekend(cursor)) {
      count += direction;
    }
  }

  return count;
};

export const isOverdue = (dueDateISO: string, now = new Date()) => {
  const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());
  const due = parseISODateOnly(dueDateISO);
  return due < today;
};

export const isWithinNextBusinessDays = (dueDateISO: string, days: number, now = new Date()) => {
  const left = businessDaysLeft(dueDateISO, now);
  return left >= 0 && left <= days;
};

export const formatCurrency = (value: number) =>
  new Intl.NumberFormat("en-US", { style: "currency", currency: "USD", maximumFractionDigits: 0 }).format(value);

export const formatDate = (isoDate: string) => parseISODateOnly(isoDate).toLocaleDateString();
