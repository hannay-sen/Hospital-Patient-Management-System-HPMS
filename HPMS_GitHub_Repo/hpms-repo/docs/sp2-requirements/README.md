# Requirements Collection — HPMS

<u>Hospital Patient Management System (HPMS)</u>

CS487: Object-Oriented Design and Implementations

Team Members: Sumaya Sharmin, Shreya Hada Shrestha, Ritika Khatri,

Sahar Tahir, Thel Theint Theint Sen

Submission Date: October 7, 2026

**Project Title**

Hospital Patient Management System (HPMS)

**Stakeholder Summary**

| **Stakeholder** | **Responsibility**                                                               |
|-----------------|----------------------------------------------------------------------------------|
| Receptionist    | Register patients, book and cancel appointments, generate bills, record payments |
| Doctor          | View assigned appointments, record diagnoses, write prescriptions                |
| Nurse           | View patient records, admit and discharge inpatients                             |
| Administrator   | Create staff, view reports                                                       |
| Project Team    | Design, implement, and test the system                                           |
| Instructor      | Evaluate object-oriented analysis, design, and testing                           |

**Assumptions**

- The system serves one small hospital or clinic.

- Every patient, staff member, room, and appointment has a unique ID.

- A patient must be registered before an appointment or admission.

- Appointments use fixed one-hour time slots, and a doctor can have only one appointment per slot.

- A room holds one patient at a time.

- Rooms, departments, and a few doctors are loaded as fictional sample data.

- There is no login. The user selects a role from the main menu, and the menu shows that role's options.

- Prices (consultation fee, daily room rate, senior discount) are fixed in code or sample data.

- Storage uses JSON files, and the interface is a menu-driven command line.

- Only fictional data is used.

**Functional Requirements**

| **ID** | **Requirement**                                                                                              | **Priority** | **Use Case** | **Main Class**   |
|--------|--------------------------------------------------------------------------------------------------------------|--------------|--------------|------------------|
| FR-01  | The system shall register a new patient.                                                                     | Must Have    | UC1          | Patient          |
| FR-02  | The system shall search patients by name or ID.                                                              | Must Have    | UC1          | Hospital         |
| FR-03  | The system shall create doctors, nurses, and receptionists by role.                                          | Must Have    | UC7          | StaffFactory     |
| FR-04  | The system shall book an appointment for a patient and a doctor at a date and time (status "Scheduled").     | Must Have    | UC2          | Appointment      |
| FR-05  | The system shall reject a conflicting booking and show the doctor's available slots.                         | Must Have    | UC2          | Hospital         |
| FR-06  | The system shall cancel an appointment (status "Cancelled").                                                 | Must Have    | UC3          | Appointment      |
| FR-07  | The system shall let a doctor view assigned appointments.                                                    | Must Have    | UC4          | Doctor           |
| FR-08  | The system shall let a doctor record a diagnosis in the patient's medical record.                            | Must Have    | UC4          | MedicalRecord    |
| FR-09  | The system shall let a doctor write a prescription (medication, dosage, instructions).                       | Must Have    | UC4          | Prescription     |
| FR-10  | The system shall let doctors and nurses view a patient's medical history.                                    | Must Have    | UC4, UC5     | MedicalRecord    |
| FR-11  | The system shall admit a patient to an available room and reject an occupied room.                           | Must Have    | UC5          | Inpatient, Room  |
| FR-12  | The system shall discharge a patient and free the room.                                                      | Must Have    | UC5          | Inpatient, Room  |
| FR-13  | The system shall generate an outpatient bill (consultation fee).                                             | Must Have    | UC6          | Bill             |
| FR-14  | The system shall generate an inpatient bill (daily rate x days stayed + treatment charges).                  | Must Have    | UC6          | Bill             |
| FR-15  | The system shall apply a pricing rule through the Strategy pattern (StandardPricing, SeniorDiscountPricing). | Must Have    | UC6          | PricingStrategy  |
| FR-16  | The system shall record a payment, reject negative or excessive amounts, and update the balance.             | Must Have    | UC6          | Bill             |
| FR-17  | The system shall save all records to JSON and reload them on startup.                                        | Must Have    | All          | Storage layer    |
| FR-18  | The system shall update patient information.                                                                 | Should Have  | UC1          | Patient          |
| FR-19  | The system shall reschedule an appointment (cancel and rebook with a conflict check).                        | Should Have  | UC3          | Appointment      |
| FR-20  | The system shall mark an appointment "Completed".                                                            | Should Have  | UC4          | Appointment      |
| FR-21  | The system shall report unpaid bills.                                                                        | Should Have  | UC8          | Hospital         |
| FR-22  | The system shall report room occupancy.                                                                      | Should Have  | UC8          | Hospital         |
| FR-23  | The system shall report daily appointments and patients by doctor.                                           | Could Have   | UC8          | Hospital         |
| FR-24  | The system shall provide menu screens to manage departments and rooms.                                       | Could Have   | UC7          | Department, Room |
| FR-25  | The system shall update and remove staff records.                                                            | Could Have   | UC7          | Staff            |
| FR-26  | The system shall let a nurse update room status.                                                             | Could Have   | UC5          | Room             |

**Non-Functional Requirements**

| **ID** | **Requirement**                                                                                                                | **Priority** |
|--------|--------------------------------------------------------------------------------------------------------------------------------|--------------|
| NFR-01 | The command-line menus shall be simple and clear.                                                                              | Must Have    |
| NFR-02 | The system shall validate required input.                                                                                      | Must Have    |
| NFR-03 | The system shall show clear error messages for invalid input.                                                                  | Must Have    |
| NFR-04 | The system shall prevent duplicate IDs.                                                                                        | Must Have    |
| NFR-05 | Medical records and bill balances shall be non-public attributes changed only through validated methods (e.g., add_payment()). | Must Have    |
| NFR-06 | Person, Patient, Staff, and PricingStrategy shall be abstract base classes (Python abc).                                       | Must Have    |
| NFR-07 | The design shall use the Strategy pattern (pricing) and the Factory pattern (staff).                                           | Must Have    |
| NFR-08 | The code shall be split into model, service, storage, and interface layers.                                                    | Must Have    |
| NFR-09 | Every Must Have requirement shall have at least one pytest test.                                                               | Must Have    |
| NFR-10 | UML diagrams shall match the final code.                                                                                       | Should Have  |

**Business Rules**

| **ID** | **Business Rule**                                                                    |
|--------|--------------------------------------------------------------------------------------|
| BR-01  | A patient must be registered before an appointment or admission.                     |
| BR-02  | A doctor cannot have two appointments at the same date and time.                     |
| BR-03  | An appointment status is Scheduled, Completed, or Cancelled.                         |
| BR-04  | A patient can be admitted only to an unoccupied room, and discharge frees it.        |
| BR-05  | Inpatient bill = daily room rate x length of stay + treatment charges.               |
| BR-06  | Outpatient bill = consultation fee.                                                  |
| BR-07  | A payment cannot be negative or exceed the outstanding balance.                      |
| BR-08  | Only doctors record diagnoses and prescriptions (enforced by the menu, not a login). |

**Main Use Cases**

| **ID** | **Use Case**                         | **Primary Actor** | **Result**                                                   |
|--------|--------------------------------------|-------------------|--------------------------------------------------------------|
| UC1    | Register Patient                     | Receptionist      | A new patient record is stored                               |
| UC2    | Book Appointment                     | Receptionist      | A conflict-free appointment is created                       |
| UC3    | Cancel or Reschedule Appointment     | Receptionist      | Appointment is cancelled or moved                            |
| UC4    | Record Diagnosis and Prescription    | Doctor            | Medical record is updated                                    |
| UC5    | Admit and Discharge Patient          | Nurse             | Patient is admitted or discharged; room is occupied or freed |
| UC6    | Generate Bill and Record Payment     | Receptionist      | Bill is created and payment recorded                         |
| UC7    | Manage Staff, Departments, and Rooms | Administrator     | Staff, department, and room records are maintained           |
| UC8    | View Reports                         | Administrator     | Unpaid bills and room occupancy are displayed                |

**Sample Use-Case Specification**

**Use Case:** Book Appointment (UC2)

**Primary Actor:** Receptionist

**Precondition:** The patient and doctor are registered.

**Main Flow:**

> 1\. The receptionist selects "Book Appointment."
>
> 2\. The receptionist selects a patient, a doctor, and a date and time.
>
> 3\. The system checks the doctor's schedule.
>
> 4\. The slot is free, so the system creates the appointment with status "Scheduled."
>
> 5\. The system displays a confirmation.

**Alternative Flows:**

- The doctor is already booked: the system rejects the request and displays the doctor's available slots.

- The patient or doctor ID does not exist: the system displays an error.

**Postcondition:** The appointment is saved and linked to one patient and one doctor.

**Proposed Object-Oriented Classes**

| **Class**                                                      | **Main Responsibilities**                                          |
|----------------------------------------------------------------|--------------------------------------------------------------------|
| Person (abstract)                                              | Common ID, name, date of birth, contact details                    |
| Patient (abstract), Inpatient, Outpatient                      | Owns a MedicalRecord; inpatients are assigned a Room               |
| Staff (abstract), Doctor, Nurse, Receptionist                  | Staff ID, department, shift; get_duties() differs by type          |
| Appointment                                                    | Links one Patient and one Doctor at a date and time, with a status |
| Room, Department                                               | Room number, daily rate, occupancy; department groups staff        |
| MedicalRecord, Prescription                                    | Diagnoses; medication, dosage, instructions                        |
| Bill, PricingStrategy (StandardPricing, SeniorDiscountPricing) | Charges, payments, balance; pricing rules                          |
| StaffFactory, Hospital                                         | Creates staff by role; Hospital manages all records                |

**Relationships:**

- Person is the base class of Patient and Staff.

- A Patient owns one MedicalRecord, which holds many Prescriptions.

- An Inpatient is assigned to one Room.

- A Department groups many Staff.

- An Appointment links one Patient and one Doctor.

- A Bill uses a PricingStrategy.

- Hospital manages all records.

**Sample Acceptance Criteria**

**Requirement:** Book an appointment without conflicts (FR-04, FR-05)

**Accepted when:**

- A registered patient and a doctor can be selected.

- A free slot creates an appointment with status "Scheduled."

- A booked slot is rejected and the doctor's available slots are shown.

- Two appointments for one doctor at the same date and time are never stored.

**Requirement:** Record a payment (FR-16)

**Accepted when:**

- A valid payment reduces the balance.

- A negative payment is rejected.

- A payment larger than the balance is rejected.

- The updated balance is saved.

**Out-of-Scope Requirements (Will Not Have)**

- SQLite storage

- Tkinter GUI

- Login and permission enforcement

- Online payment processing

- Insurance claims

- Laboratory or pharmacy systems

- Telemedicine

- Integration with external hospital systems

- Real patient information
