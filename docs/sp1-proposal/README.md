# Project Proposal — HPMS

# Hospital Patient Management System (HPMS) 

**Course: CS487: Object-Oriented Design and Implementations**

**Team Members:** Sumaya Sharmin, Shreya Hada Shrestha, Ritika Khatri, Sahar Tahir,

Thel Theint Theint Sen

> **Submission Date:** September 30, 2026

## Introduction 

This project proposes the design and implementation of a Hospital Patient Management System (HPMS), a Python application that helps the staff of a small hospital or clinic manage patients, doctors, appointments, medical records, room admissions, and billing. The system will be used by four types of users: receptionists, doctors, nurses, and administrators. The main focus is to apply object-oriented analysis, design, and implementation to a real-world domain, moving from requirements to UML models to working, tested code.

## Problem Statement 

Many small hospitals and clinics still manage patient information with paper files or disconnected spreadsheets. Staff lose time searching for patient history, appointments are double-booked because nothing checks doctor availability, room occupancy is tracked inconsistently, and bills are calculated by hand, which leads to errors. A single computerized system can store patient information in one place, prevent scheduling conflicts, track room availability, keep medical records organized, and produce accurate bills automatically.

## Objectives 

- Register, update, search, and manage patient records.

- Manage doctors and staff and organize them by department.

- Schedule, reschedule, and cancel appointments while automatically preventing conflicts.

- Maintain each patient's medical history, diagnoses, and prescriptions.

- Admit and discharge inpatients and track room availability.

- Generate accurate bills for inpatients and outpatients and track payments.

- Apply the four object-oriented principles and appropriate design patterns in a clean, maintainable, and tested codebase.

## System Actors 

- **Receptionist:** Registers patients, books and cancels appointments, and handles billing and payments.

- **Doctor:** Views assigned appointments, records diagnoses, and writes prescriptions.

- **Nurse:** Views patient records, admits and discharges inpatients, and updates room status in the assigned ward.

- **Administrator:** Manages staff, departments, and rooms, and views reports.

## Proposed Features 

The system will include the following features:

1.  Patient registration, update, and search by name or ID

2.  Doctor, nurse, and receptionist management

3.  Department management

4.  Appointment scheduling with automatic conflict checking

5.  Medical records, diagnoses, and prescriptions

6.  Inpatient admission and discharge with room tracking

7.  Billing with configurable pricing rules and payment tracking

8.  Reports: daily appointments, patients by doctor, room occupancy, and unpaid bills

9.  Persistent data storage so records remain after the program is closed

## Main Use Cases 

The system will support the following main use cases:

- UC1 – Register Patient (Receptionist)

- UC2 – Book Appointment (Receptionist): the system checks the doctor's availability before confirming

- UC3 – Cancel or Reschedule Appointment (Receptionist)

- UC4 – Record Diagnosis and Prescription (Doctor)

- UC5 – Admit and Discharge Patient (Nurse)

- UC6 – Generate Bill and Record Payment (Receptionist)

- UC7 – Manage Staff, Departments, and Rooms (Administrator)

- UC8 – View Reports (Administrator)

**Example – UC2 Book Appointment:** The receptionist selects a patient, a doctor, and a date and time.

The system checks the doctor's schedule. If the slot is free, the appointment is created with status "Scheduled" and a confirmation is shown. If the doctor is already booked, the request is rejected and the doctor's available time slots are displayed.

## Object-Oriented Design 

### Main Classes 

The main classes will include:

- **Person (abstract):** common ID, name, date of birth, and contact details; base class of Patient and Staff

- **Patient (abstract):** owns a MedicalRecord; subclasses Inpatient (admitted to a Room) and Outpatient (consultation only)

- **Staff (abstract):** staff ID, department, and shift; subclasses Doctor, Nurse, and Receptionist

- **Appointment:** links one Patient and one Doctor at a date and time, with a status (Scheduled, Completed, Cancelled)

- **Room and Department:** room number, type, daily rate, and occupancy; a department groups staff members

- **MedicalRecord and Prescription:** a patient's diagnoses and the medication, dosage, and instructions prescribed

- **Bill and PricingStrategy:** charges, payments, and balance; pricing rules such as StandardPricing and SeniorDiscountPricing

- **StaffFactory and Hospital:** the factory creates staff by role; Hospital is the central class managing all records

### Object-Oriented Principles 

- **Encapsulation:** Medical records and bill balances will be stored in non-public attributes and changed only through validated methods. For example, a balance can only change through add_payment(), which rejects negative or excessive amounts.

- **Inheritance:** Shared attributes and methods are defined once in Person, Patient, and Staff and reused by their subclasses.

- **Abstraction:** Person, Patient, Staff, and PricingStrategy will be abstract base classes created with Python's abc module.

- **Polymorphism:** calculate_bill() works differently for inpatients (daily room rate times length of stay, plus treatment charges) and outpatients (consultation fee), and get_duties() differs for each staff type. Billing and reporting code can handle any patient or staff member without knowing its exact type.

### Design Patterns 

- **Strategy Pattern:** Pricing rules are separate classes, so new rules (such as a staff discount) can be added without changing the Bill or Patient classes.

- **Factory Pattern:** StaffFactory creates Doctor, Nurse, or Receptionist objects in one place, so the interface code does not depend on concrete staff classes.

### UML Diagrams 

The final report will include a use-case diagram, a class diagram, sequence diagrams for Book Appointment and Generate Bill, and an activity diagram for patient admission and discharge. The diagrams will be updated during implementation so they match the submitted code.

## System Architecture 

The system will use a layered architecture, where each layer depends only on the layer below it:

- **Model layer:** Domain classes such as Patient, Doctor, Room, and Appointment.

- **Service layer:** Business logic, such as appointment conflict checking, room assignment, and bill calculation.

- **Storage layer:** Saving and loading data using JSON files or an SQLite database.

- **Interface layer:** A menu-driven command-line interface, with an optional Tkinter GUI.

This separation makes the code easier to test, maintain, and extend; for example, the storage method can change without affecting the business logic.

## Scope of the Project 

The project will focus on the core operations of a small hospital or clinic: patient and staff management, appointment scheduling, medical records, inpatient admission with room tracking, billing, reports, and persistent storage.

It will not include online payment processing, insurance claims, laboratory or pharmacy systems, telemedicine, advanced authentication, or integration with external hospital systems. Only fictional sample data will be used; no real patient information will be stored.

## Proposed Technology 

- **Programming language:** Python 3

- **Design tools:** UML diagrams (draw.io, Lucidchart, or StarUML)

- **Storage:** JSON files or an SQLite database using Python's built-in sqlite3 module

- **User interface:** Menu-driven command-line interface, with an optional Tkinter GUI

- **Testing:** pytest unit, integration, and edge-case tests, with every functional requirement linked to at least one test

- **Version control:** Git and GitHub

## Testing Plan 

- **Unit testing:** Each class will be tested with pytest, including patient registration, appointment conflict detection, room assignment, bill calculation, and payment validation.

- **Integration testing:** Complete workflows will be tested, such as registering a patient, booking an appointment, admitting and discharging the patient, and generating a bill.

- **Edge case testing:** Invalid input will be tested, including duplicate IDs, overlapping appointments, admitting a patient to an occupied room, and negative or excessive payments.

- **Traceability:** Every functional requirement will be linked to at least one test case, and bugs found during testing will be documented along with how they were fixed.

## Risks and Mitigation 

- **Features take longer than planned:** Complete the core features first; treat the GUI and extra reports as optional.

- **Uneven workload among team members:** Assign clear module ownership and hold weekly progress meetings.

- **Code conflicts between team members:** Use Git branches and review code before merging.

- **Design changes during implementation:** Update UML diagrams so design and code stay consistent.

## Expected Outcome 

At the end of the semester, the project will provide a functional and tested prototype of a Hospital Patient Management System. Staff will be able to register patients, schedule appointments without conflicts, maintain medical records, admit and discharge inpatients with room tracking, and generate accurate bills. The project will also demonstrate how object-oriented analysis and design can be applied to solve a real-world problem.

## Work Plan 

- **Week 1:** Requirements gathering and role assignment

- **Week 2:** Use-case and class diagrams

- **Week 3:** Detailed system design, sequence and activity diagrams

- **Weeks 4–6:** Implementation of model classes, business logic, storage, reports, and interface

- **Week 7:** Testing, debugging, and UML update

- **Week 8:** Final report, GitHub documentation, and presentation

## Conclusion 

The Hospital Patient Management System is a practical and well-scoped project for applying the concepts learned in Object Oriented Design and Analysis. It provides meaningful opportunities to apply encapsulation, inheritance, abstraction, polymorphism, and design patterns, and will give our team experience in requirements analysis, UML modeling, class design, Python implementation, testing, and teamwork.
