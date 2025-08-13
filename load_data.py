import pandas as pd

# Correct full CSV path
source_path = r"C:\Users\piyus\Downloads\archive (8)\medical_insurance.csv"

# Read the CSV file
df = pd.read_csv(source_path)

# Save to a new location
destination_path = "notebook/data/Medical_insurance.csv"
df.to_csv(destination_path, index=False)