# Design Decisions

Decisions made to answer the instructor feedback on the Requirements Collection (82/100) and User Stories (89/100). **Proposed** rows still need instructor confirmation.

| # | Question | Decision | Status |
|---|---|---|---|
| D1 | What kind of patient is registered? Can an outpatient be admitted later? | `Patient` is one concrete class. Inpatient status is an active `Admission` record. Any registered patient can be admitted later and keeps the same ID, medical record, appointments and bills. | Decided |
| D2 | Where does polymorphism go once Patient is concrete? | `Bill` is abstract; `OutpatientBill` and `InpatientBill` override `calculate_base_charge()`. Abstract classes: `Person`, `Staff`, `Bill`, `PricingStrategy` (NFR-06 updated). | Decided |
| D3 | How does the system know which doctor is using it? | After choosing Doctor or Nurse, the CLI asks for a staff ID and accepts it only if the staff type matches. Simulated identity selection, not authentication or security. | Decided |
| D4 | What counts as a conflicting appointment? | Same doctor, same date, same one-hour slot, where the existing appointment is Scheduled. Cancelled frees the slot; Completed never blocks. A patient also cannot hold two Scheduled appointments in one slot. | Decided |
| D5 | What happens when a reschedule is rejected? | The new slot is checked first; on failure the original stays Scheduled. On success the original is Cancelled and the new one Scheduled in one save. | Decided |
| D6 | Can a patient have several active admissions? | No — at most one active admission per patient and per room. | Decided |
| D7 | How is length of stay counted? | Billable days = max(1, ceil((discharge − admission) / 24 h)). | Proposed |
| D8 | How are treatment charges entered? | The receptionist adds itemized charges (description, amount ≥ 0) before the inpatient bill is finalized; inpatient bills only after discharge. | Proposed |
| D9 | Senior discount rule? | Age 65 or older on the bill date; 10% off the total. | Proposed |
| D10 | Which room statuses can a nurse set? | `AVAILABLE`, `OCCUPIED`, `MAINTENANCE`. Only admit/discharge set or clear `OCCUPIED`; a nurse can toggle Available ↔ Maintenance only when the room is free. | Proposed |
| D11 | UC8 did not include the FR-23 reports. | UC8 = billing and occupancy reports (FR-21, FR-22); new UC9 = scheduling reports (FR-23). | Decided |
| D12 | Are clinical entries linked to a doctor and visit? | Every diagnosis and prescription stores doctor ID, timestamp and optional appointment ID. | Decided |
| D13 | What happens to a removed doctor's appointments? | Staff with future Scheduled appointments or an active admission cannot be removed. | Proposed |
| D14 | FR-15 names a design pattern. | FR-15 states only the behavior; the Strategy pattern is the design constraint NFR-07. | Decided |
