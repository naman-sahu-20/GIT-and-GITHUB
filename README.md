# Hospital Patient Data Analysis System

## Overview
This Python project reads hospital patient records from CSV-formatted text, cleans the data, calculates each patient's length of stay, summarizes department and age-group counts, and displays a bar chart.

## Features
- Loads CSV text into a Pandas DataFrame.
- Removes duplicate records using `Patient_ID` (keeps the first record).
- Fills missing `Age` values with the median age.
- Converts admission and discharge dates to datetime values.
- Calculates `Length_of_Stay` in days.
- Counts patients by department and reports the total.
- Displays each patient's length of stay and the average stay.
- Groups patients into age ranges (`0-40`, `41-60`, and `61+`) and plots the distribution.

## Requirements
- Python 3
- pandas
- matplotlib

Install the required packages:

```bash
python -m pip install pandas matplotlib
```

## How to Run
1. Save the program in a file, for example `hospital_analysis.py`.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python hospital_analysis.py
```

The script includes sample test data and runs the test cases when executed directly.

## Main Functions

### `load_and_clean_data(csv_data)`
Reads CSV text, trims column names, removes duplicate patient IDs, fills missing ages, converts date columns, and calculates length of stay. Returns a cleaned DataFrame.

### `menu_option_1(df)`
Displays the number of patients in each department and the total number of patients.

### `menu_option_2(df)`
Displays each patient's length of stay and the overall average stay.

### `menu_option_3(df)`
Displays the average stay, counts patients in each age group, and shows a Matplotlib bar chart.

## Data Format
The input CSV is expected to contain these columns:

| Column | Description |
|---|---|
| `Patient_ID` | Unique patient identifier |
| `Age` | Patient age |
| `Gender` | Patient gender |
| `Department` | Hospital department |
| `Admit_Date` | Admission date |
| `Discharge_Date` | Discharge date |

Dates should be parseable by Pandas, such as `YYYY-MM-DD`.

## Notes and Limitations
- Duplicate detection uses `Patient_ID`; the first row for an ID is retained.
- Missing ages are filled using the median of the remaining records.
- The current program expects the required columns to exist and dates to be valid.
- It does not currently validate negative ages, missing IDs, or discharge dates earlier than admission dates.
- This is a learning/demo project using sample data, not a clinical decision-support system.
