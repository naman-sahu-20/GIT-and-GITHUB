# Project Summary: Hospital Patient Data Analysis System

## Purpose
The project demonstrates how Python can be used to clean and analyze basic hospital patient records with Pandas and visualize age-group distribution with Matplotlib.

## Workflow
1. Read CSV text into a DataFrame using `io.StringIO()` and `pd.read_csv()`.
2. Remove extra spaces from column names.
3. Remove duplicate records based on `Patient_ID`.
4. Replace missing ages with the median age.
5. Convert `Admit_Date` and `Discharge_Date` to datetime values.
6. Calculate `Length_of_Stay` as the difference between discharge and admission dates.
7. Generate department counts, patient stay statistics, age-group counts, and a bar chart.

## Functions
- **`load_and_clean_data()`** — prepares the patient data for analysis.
- **`menu_option_1()`** — reports department-wise patient counts and total patients.
- **`menu_option_2()`** — reports each patient's stay and the average stay.
- **`menu_option_3()`** — reports average stay, groups ages, and plots a bar chart.

## Libraries Used
- **Pandas:** reading, cleaning, grouping, and analyzing tabular data.
- **Matplotlib:** creating the age-group bar chart.
- **io:** treating a string as a file-like CSV input.

## Sample Test Data Outcomes
- **Test Case 1:** 3 patients; Cardiology has 2 and Ortho has 1. Average stay is approximately 3.67 days.
- **Test Case 2:** Patient P4 has a stay of 0 days; average stay is 0.00 days.
- **Test Case 3:** 1 duplicate record is removed. The missing age is filled with the median age of 45.
- **Test Case 4:** Reuses Test Case 1 data. Age groups are 0–40: 1, 41–60: 2, and 61+: 0.

## Conclusion
The project provides a small end-to-end example of loading, cleaning, analyzing, and visualizing structured data in Python. It is suitable for practicing Pandas DataFrames, missing-value handling, duplicate removal, date calculations, grouping, and basic plotting.

## Possible Improvements
- Add input validation for required columns and invalid dates.
- Handle empty datasets and cases where all ages are missing.
- Validate patient IDs and date order.
- Add a command-line menu so users can choose analysis options interactively.
