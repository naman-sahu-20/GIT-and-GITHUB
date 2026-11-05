import pandas as pd
import matplotlib.pyplot as plt

def analyze_patient_data(file_path):
    # 1. Load the CSV file
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return

    # 2. Clean missing, duplicate and invalid values
    # Remove duplicates
    initial_count = len(df)
    df.drop_duplicates(inplace=True)
    duplicates_removed = initial_count - len(df)
    print(f"Duplicates removed: {duplicates_removed}")

    # Fill missing Age with median
    if df['Age'].isnull().any():
        median_age = df['Age'].median()
        df['Age'].fillna(median_age, inplace=True)
        print(f"Missing Age filled with median: {median_age}")

    # Convert dates to datetime objects
    df['Admit_Date'] = pd.to_datetime(df['Admit_Date'])
    df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])

    # Calculate Length of Stay
    df['Length_of_Stay'] = (df['Discharge_Date'] - df['Admit_Date']).dt.days

    # 3. Department-wise analysis
    print("\n--- Department-wise Patient Load ---")
    dept_counts = df['Department'].value_counts()
    for dept, count in dept_counts.items():
        print(f"{dept}: {count}")
    print(f"Total patients: {len(df)}")

    # 4. Average Length of Stay
    avg_stay = df['Length_of_Stay'].mean()
    print(f"\nAverage stay: {avg_stay:.2f} days")

    # 5. Age-group distribution
    bins = [0, 40, 60, 100]
    labels = ['0-40', '41-60', '61+']
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)
    
    print("\n--- Age Group Distribution ---")
    age_counts = df['Age_Group'].value_counts().sort_index()
    for group, count in age_counts.items():
        print(f"{group}: {count}")

    # 6. Plotting
    plt.figure(figsize=(8, 5))
    age_counts.plot(kind='bar', color='skyblue')
    plt.title('Patient Distribution by Age Group')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Patients')
    plt.xticks(rotation=0)
    plt.show()

if __name__ == "__main__":
    # Replace 'patients.csv' with your actual file path
    analyze_patient_data('patients.csv')