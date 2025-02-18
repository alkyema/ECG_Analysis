import os
import shutil
import pandas as pd 

df = pd.read_csv(r"C:\Users\Satwik\Downloads\ECG\Working\output.csv")

rand_zero = df['Name'].tolist()
print(rand_zero)
# Define directories
source_directory = r"C:\Users\Satwik\Downloads\ECG\Working\dataset"
destination_directory = r"C:\Users\Satwik\Downloads\ECG\Working\filtered_dataset"

# Ensure the destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# List of filenames (without .csv extension) to be copied Replace with actual filenames
# Iterate through files in the source directory
for file in os.listdir(source_directory):
    file_name = file.replace(".csv", "")  # Normalize filename
    file_name = file_name.replace("_", "")  # Normalize filename
    # print(file_name in rand_zero)
    print(f"Checking: {file_name}")  # Debugging print

    if file_name in rand_zero:
        shutil.copy(os.path.join(source_directory, file), os.path.join(destination_directory, f"{file_name}.csv"))
        rand_zero.remove(file_name)
        print(f"Copied: {file}")
    else:
        print(f"Skipped: {file}")
print(rand_zero)
