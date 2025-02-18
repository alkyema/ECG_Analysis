import h5py
import csv
import os

# Path to your HDF5 file
file_path = r"ecg_tracings.hdf5"

# Directory to save the CSV files
output_dir = "dataset"
os.makedirs(output_dir, exist_ok=True)

try:
    with h5py.File(file_path, 'r') as hdf_file:
        # Check if 'tracings' exists and inspect it
        if 'tracings' in hdf_file:
            tracings_dataset = hdf_file['tracings']

            # Iterate over all tracings and save each as a separate CSV file
            for i in range(tracings_dataset.shape[0]):
                # Extract the tracing and remove the first and last 582 rows
                tracing = tracings_dataset[i][582:-582]

                # Define the CSV file name
                csv_file_name = os.path.join(output_dir, f"patient_{i + 1}.csv")

                # Write the tracing to a CSV file
                with open(csv_file_name, mode='w', newline='') as csv_file:
                    writer = csv.writer(csv_file)

                    # Write the header with specific labels
                    header = ["DI", "DII", "DIII", "AVL", "AVF", "AVR", "V1", "V2", "V3", "V4", "V5", "V6"]
                    writer.writerow(header)

                    # Write each row of the tracing, excluding rows where all values are 0
                    for row in tracing:
                        if any(value != 0 for value in row):
                            writer.writerow(row)

            print(f"All tracings saved to folder: {output_dir}")
        else:
            print("Dataset 'tracings' not found in the HDF5 file.")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")