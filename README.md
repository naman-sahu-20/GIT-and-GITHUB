# Hospital Patient Data Analyzer

A Python-based command-line application for managing, cleaning, and analyzing hospital patient records. This tool uses `pandas` for data manipulation and `matplotlib` for data visualization, providing an easy-to-use interactive menu to evaluate patient lengths of stay, demographic distributions, and department metrics.

## Features

- **Automated Data Generation**: Automatically creates a dummy `patients.csv` file to ensure the application works out-of-the-box for testing.
- **Data Visualization**: Generates a bar chart detailing patient distribution across different age groups.
- **Data Cleaning**: Automatically handles missing values (e.g., filling missing ages with the median) and removes duplicate patient records.
- **CRUD Operations**: Add new patient records, delete existing ones, and view the entire dataset in real-time.
- **Data Analytics**:
  - Calculate total patients per department.
  - Compute the length of stay automatically using admission and discharge dates.
  - Analyze average lengths of stay grouped by specific patient test cases.

## Dependencies

To run this project, you will need Python 3.x installed along with the following libraries:
- `pandas`
- `matplotlib`
- `numpy`

You can install the required libraries using pip:
```bash
pip install pandas matplotlib numpy
```

## How to Run

1. Clone or download this repository.
2. Ensure you have the required dependencies installed.
3. Run the script from your terminal:
```bash
python Code.py
```
4. Follow the on-screen prompts to navigate the interactive menu.

## Menu Options

1. **View Department count**: Displays the number of patients in each department.
2. **View Length of stay**: Shows the length of stay for specific test constraints (e.g., patient P4).
3. **View Stay and age groups**: Calculates average stay times and displays a bar chart of age group distributions (0-40, 41-60, 61+).
4. **Delete a patient record**: Remove a patient by their `Patient_ID`.
5. **View all patient data**: Prints the current dataset to the console.
6. **Add a patient record**: Interactive prompts to add a new patient to the CSV.
7. **Clean Dataset**: Removes duplicate rows and fills missing age fields using the median age.
8. **RESET DATA**: Restores `patients.csv` to the original dummy dataset for fresh testing.
9. **Exit**: Closes the application.