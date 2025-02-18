import h5py
import csv

# Path to your HDF5 file
file_path = r"ecg_tracings.hdf5"

try:
    with h5py.File(file_path, 'r') as hdf_file:
        # Check if 'tracings' exists and inspect it
        if 'tracings' in hdf_file:
            tracings_dataset = hdf_file['tracings']
            
            # Extract the first tracing and remove the first and last 582 rows
            first_tracing = tracings_dataset[1][582:-582]  # First tracing with rows removed

            # Define the CSV file name
            csv_file_name = "Second_Tracing.csv"

            # Write the first tracing to a CSV file
            with open(csv_file_name, mode='w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                
                # Write the header with specific labels
                header = ["DI", "DII", "DIII", "AVL", "AVF", "AVR", "V1", "V2", "V3", "V4", "V5", "V6"]
                writer.writerow(header)

                # Write each row of the tracing, excluding rows where all values are 0
                for row in first_tracing:
                    if any(value != 0 for value in row):
                        writer.writerow(row)

            print(f"First tracing saved to {csv_file_name}")
        else:
            print("Dataset 'tracings' not found in the HDF5 file.")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")