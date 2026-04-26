# Fiscal Anomaly Detector

## Project Overview
This project aims to optimize the fiscal closing process by identifying potential inconsistencies in tax documents (ICMS, Sped, Reinf) before the final audit.

## Objective
Reduce the time spent on manual conferences by using Machine Learning to detect anomalies in fiscal data patterns.

## Roadmap
- [x] Initial setup
- [ ] Data simulation and exploration (Chapter 2 - Hands-On ML)
- [ ] Data cleaning and pipeline creation
- [ ] Model training for anomaly detection

## Practical Example (Anomaly Detection)

The system identifies fiscal inconsistencies by calculating the **Real Rate** of each invoice and comparing it against a business rule threshold (12%).

**Case Study: Invoice ID 956**
- **Vendor:** Supplier Enterprise 10 Ltd
- **Invoice Value:** R$ 14.587,22
- **Expected Tax (12%):** R$ 1.750,46
- **Actual Tax Found:** **R$ 2.625,70** (An 18% rate)

**Result:** The algorithm flagged this record as an anomaly because the 18% rate exceeded our 13% safety threshold. This record was automatically moved to the `audit_report_needed.csv` for immediate human review.