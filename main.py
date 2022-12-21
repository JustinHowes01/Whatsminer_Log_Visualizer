import tkinter as tk
from tkinter import filedialog

import matplotlib.pyplot as plt

from functions import data_organization
from functions import log_reading_function


def log_file_retriever():
    filepath = filedialog.askopenfilename(title="Select the long-miner-state log")
    read_file = open(filepath, "r")

    file_header, file_data = log_reading_function.long_miner_state_log_reader(read_file)
    read_file.close()

    output_file = open('functions/output_data.log', 'w')
    output_file.write(file_header)

    output_file = open('functions/output_data.log', 'a')
    for data in file_data:
        output_file.write(f'\n{data}')

    output_file.close()


def output_file_graphing(file):
    (
        hashrate_hashboard_avg,
        sm0_hashrates, sm0_freqs, sm0_temps, sm0_chips,
        sm1_hashrates, sm1_freqs, sm1_temps, sm1_chips,
        sm2_hashrates, sm2_freqs, sm2_temps, sm2_chips,
        psu_wattages
    ) = data_organization.output_file_unpacker(file)

    hashrate_x, hashrate_y = data_organization.overall_hashrate(hashrate_hashboard_avg)

    (
        chip_temp_x, chip_temp_y1, chip_temp_y2, chip_temp_y3
    ) = data_organization.hashboard_chip_temps(sm0_chips, sm1_chips, sm2_chips)

    (
        freq_x, freq_y1, freq_y2, freq_y3
    ) = data_organization.hashboard_freqs(sm0_freqs, sm1_freqs, sm2_freqs)

    wattage_x, wattage_y = data_organization.overall_wattage(psu_wattages)

    plt.subplot(2, 2, 1)
    plt.plot(hashrate_x, hashrate_y, label='Hashrate')
    plt.autoscale(True)
    plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(chip_temp_x, chip_temp_y1, label='SM0 Chip Temp')
    plt.plot(chip_temp_x, chip_temp_y2, label='SM1 Chip Temp')
    plt.plot(chip_temp_x, chip_temp_y3, label='SM2 Chip Temp')
    plt.autoscale(True)
    plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(wattage_x, wattage_y, label='PSU Wattage')
    plt.autoscale(True)
    plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(freq_x, freq_y1, label='SM0 Frequency')
    plt.plot(freq_x, freq_y2, label='SM1 Frequency')
    plt.plot(freq_x, freq_y3, label='SM2 Frequency')
    plt.autoscale(True)
    plt.legend()

    plt.show()


root = tk.Tk()
root.title("Log Visualizer")

file_frame = tk.Frame(root)
file_frame.configure(pady='3')
file_frame.pack()

file_output = select_file_button = tk.Button(
    file_frame,
    text="Select File",
    command=lambda: log_file_retriever()
)
select_file_button.pack()

graph_frame = tk.Frame(root)
graph_frame.configure(pady='3')
graph_frame.pack()

graph_data_button = tk.Button(
    graph_frame,
    text="Graph Data",
    command=lambda: output_file_graphing(open('functions/output_data.log'))
)
graph_data_button.pack()

close_frame = tk.Frame(root)
close_frame.configure(pady='3')
close_frame.pack()

close_frame_button = tk.Button(
    close_frame,
    text="Close",
    command=root.destroy
)
close_frame_button.pack()

root.geometry("280x130")
root.mainloop()

quit()