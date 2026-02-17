<div align="center">

# Graduate Program Appointment Tracking & Reporting Dashboard

A real-time dashboard that helps visualizes gruaduate student appointments within the School of Engineering. The dashboard helps monitor and report about the status of these appointments to their respective owners and peers.

</div>


## Overview

The dashboard is a web-based application that helps graduate chairs and deans monitor student appointments within GLAAS (Graduate and Lecturer Academic Appointment System). As of now, there is no way for them to see the transparency of these appointments in regards to what step of the process they are in (ex. delayed, approved, pending). This application is suppose to help present that data in a visually appealing dashboard with certain roles having role specific access.

### Goals

- Show case appointment statuses (Pending, Approved, Delayed)
- Role-based access:
  - Chairs -> View appointments within their graduate group
  - Deans -> View all appointments within School of Engineering
  - Faculty/Staff -> Student-view access
- Showcasing TA history with important information like number of semesters served, FTE assignments, etc.
- Reducing the amount of delays in appointment approvals so students will be paid
- Improving communication between the parties involved in this process
- Implementing a reports/notification system to report/notify on a timed basis

### Features

- [x] Role-based dashboards (Chair, Dean, Faculty, etc)
- [x] Real-time appointment status tracking (Pending / Approved / Delayed)
- [x] Showcasing TA history
- [x] Filtering/sorting based on time of appointment / status of appointment
- [ ] Automated reminder/report notifications
- [ ] Sending requests for funding for faculty
- [ ] Accessibility on phone

### Software Stack / Technologies Used

- Language: Javascript/HTML (Frontend), Python (Backend - TBD)
- Framework: React
- Database: TBD
- UI Design: Figma (Prototype / Mockup)
- Authentication: UC Merced Single Sign-On (SSO)
- Data Sources:
  - GLAAS database
  - Box 

## Quickstart

Summary for developers with links to setup, build, test instructions in wiki or docs.

### Instructions

1. Click "Use this template" on GitHub to create your private repository.
2. Clone your repo locally.
3. Fill in the metadata table above.
4. Create an initial branch (e.g., `setup`), never commit directly to `main` (unless instructed).
5. Open an Issue for each lab / feature before starting work.
6. Use Pull Requests to merge changes (each PR should reference at least one Issue).

## Structure

Include: what constitutes passing (e.g., all tests green, coverage threshold).

## Coding & Collaboration Conventions

- Use semantic commit messages (see `CONTRIBUTING.md` for full details).
- Open an Issue for every distinct unit of work (lab task, feature, bug, refactor, research).
- Create branches from `main` named after the Issue: `<type>/short-kebab` (e.g., `feat/scheduler-phase1`).
- Commit changes incrementally with semantic commit messages.
- Open a Pull Request early (draft) and link the Issue.
- Request peer review (if required) before merging.
- Squash merge or rebase to keep `main` linear (unless told otherwise).
