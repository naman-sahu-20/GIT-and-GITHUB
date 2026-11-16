# Project Summary: Hospital Patient Data Analyzer

## Overview
The **Hospital Patient Data Analyzer** is a data processing script designed to streamline the management of basic hospital records. Written in Python, it serves as a lightweight ETL (Extract, Transform, Load) and analytics tool. It reads data from a CSV file, performs necessary transformations (such as datetime conversions and missing value imputations), and provides analytical outputs both in text and graphical formats.

## Data Structure
The application operates on a dataset (`patients.csv`) containing the following fields:
* `Patient_ID`: Unique identifier for the patient.
* `Age`: The patient's age.
* `Gender`: Male (M) or Female (F).
* `Department`: The hospital department (e.g., Cardiology, Ortho, ENT).
* `Admit_Date`: The date the patient was admitted (YYYY-MM-DD).
* `Discharge_Date`: The date the patient was discharged (YYYY-MM-DD).

*Note: The script dynamically calculates a `Length_of_Stay` feature in memory by taking the difference in days between the `Discharge_Date` and `Admit_Date`.*

## Core Test Cases & Functionality

The code implements specific test cases to evaluate data handling capabilities:

* **Test Case 1 (Department Grouping):** Handled via Menu Option 1. It utilizes `pandas.groupby()` to aggregate and count the number of patients actively assigned to each department.
* **Test Case 2 (Specific Value Retrieval):** Handled via Menu Option 2. It tests boundary conditions by locating a specific patient (`P4`) and calculating their unique length of stay and average stay.
* **Test Case 3 (Data Cleaning):** Handled via Menu Option 7. It demonstrates data sanitization by:
  1. Identifying `NaN` values in the `Age` column and filling them with the calculated dataset median.
  2. Utilizing `drop_duplicates` based on the `Patient_ID` subset to ensure data integrity.
* **Test Case 4 (Categorization & Visualization):** Handled via Menu Option 3. It filters specific patients (`P1`, `P2`, `P3`), calculates their average stay, and categorizes ages into standard bins (`0-40`, `41-60`, `61+`). It then leverages `matplotlib` to render a bar chart of this distribution.

## Technical Highlights
* **State Management:** Changes made through the CLI (Adding, Deleting, Cleaning) are immediately written back to `patients.csv`, ensuring data persistence across sessions.
* **Robust Error Handling:** Input operations (like adding a patient or parsing missing ages) utilize `try-except` blocks and `numpy.nan` to prevent application crashes during user data entry.