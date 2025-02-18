import h5py
import csv
import matplotlib.pyplot as plt
import os

file_path = r"ecg_tracings.hdf5"

base_plot_dir = "Tracing_Plots"
os.makedirs(base_plot_dir, exist_ok=True)


def plot_and_save_graph(tracing_idx, row_idx, row, header, tracing_plot_dir):
    """Function to plot and save an individual ECG graph."""
    if any(value != 0 for value in row):
        plt.figure(figsize=(10, 6))
        plt.plot(range(len(row)), row, marker='o')
        plt.title(f"ECG Plot for Tracing {tracing_idx + 1}, Row {row_idx + 1}")
        plt.xlabel("Channels")
        plt.ylabel("Amplitude")
        plt.grid()

        # Save the plot as an image file
        plot_file_name = os.path.join(tracing_plot_dir, f"graph_{row_idx + 1}.png")
        plt.savefig(plot_file_name)
        plt.close()


try:
    with h5py.File(file_path, 'r') as hdf_file:
        if 'tracings' in hdf_file:
            tracings_dataset = hdf_file['tracings']

            for tracing_idx, tracing in enumerate(tracings_dataset):
                trimmed_tracing = tracing[582:-582]

                tracing_plot_dir = os.path.join(base_plot_dir, f"Tracing_{tracing_idx + 1}_Plots")
                os.makedirs(tracing_plot_dir, exist_ok=True)

                csv_file_name = os.path.join(tracing_plot_dir, f"Tracing_{tracing_idx + 1}.csv")

                with open(csv_file_name, mode='w', newline='') as csv_file:
                    writer = csv.writer(csv_file)

                    header = ["DI", "DII", "DIII", "AVL", "AVF", "AVR", "V1", "V2", "V3", "V4", "V5", "V6"]
                    writer.writerow(header)

                    for row in trimmed_tracing:
                        if any(value != 0 for value in row):
                            writer.writerow(row)

                print(f"Tracing {tracing_idx + 1} saved to {csv_file_name}")

                # Sequentially plotting and saving graphs for each row
                for row_idx, row in enumerate(trimmed_tracing):
                    plot_and_save_graph(tracing_idx, row_idx, row, header, tracing_plot_dir)

                print(f"Tracing {tracing_idx + 1} plots saved to folder: {tracing_plot_dir}")

        else:
            print("Dataset 'tracings' not found in the HDF5 file.")

except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")
