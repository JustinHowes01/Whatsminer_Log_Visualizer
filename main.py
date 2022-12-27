import customtkinter as ctk
from customtkinter import filedialog

import matplotlib.pyplot as plt

from functions import data_organization
from functions import log_reading_function


def log_file_retriever():
    # Open file select dialog to select the miner log
    filepath = filedialog.askopenfilename(title="Select the \"miner-state\" or \"long-miner-state log\"")
    read_file = open(filepath, "r")

    # Read the data in the file opened above
    file_header, file_data = log_reading_function.long_miner_state_log_reader(read_file)
    read_file.close()

    # Open/append read data to the output log to be graphed
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

    # Plot the data on the axes
    plt.subplot(2, 2, 1)
    plt.plot(hashrate_x, hashrate_y, label='Hashrate')
    plt.legend()
    plt.autoscale(True)

    # plot the data on the axes
    plt.subplot(2, 2, 2)
    plt.plot(wattage_x, wattage_y, label='PSU Wattage')
    plt.legend()
    plt.autoscale(True)

    # plot the data on the axes
    plt.subplot(2, 2, 3)
    plt.plot(chip_temp_x, chip_temp_y1, label='SM0 Chip Temp')
    plt.plot(chip_temp_x, chip_temp_y2, label='SM1 Chip Temp')
    plt.plot(chip_temp_x, chip_temp_y3, label='SM2 Chip Temp')
    plt.legend()
    plt.autoscale(True)

    # plot the data on the axes
    plt.subplot(2, 2, 4)
    plt.plot(freq_x, freq_y1, label='SM0 Frequency')
    plt.plot(freq_x, freq_y2, label='SM1 Frequency')
    plt.plot(freq_x, freq_y3, label='SM2 Frequency')
    plt.legend()
    plt.autoscale(True)

    plt.show()


def output_file_hashrate(file):
    # Unpack the data from the output file
    (
        hashrate_hashboard_avg,
        sm0_hashrates, sm0_freqs, sm0_temps, sm0_chips,
        sm1_hashrates, sm1_freqs, sm1_temps, sm1_chips,
        sm2_hashrates, sm2_freqs, sm2_temps, sm2_chips,
        psu_wattages
    ) = data_organization.output_file_unpacker(file)

    # Organize the data for the hashrate graph
    hashrate_x, hashrate_y = data_organization.overall_hashrate(hashrate_hashboard_avg)

    # Create a figure and axes for the hashrate graph
    fig1, ax1 = plt.subplots()

    # Plot the data on the axes
    ax1.plot(hashrate_x, hashrate_y, label='Hashrate')
    ax1.legend()

    plt.autoscale(True)
    plt.show()


def output_file_wattage(file):
    # Unpack the data from the output file
    (
        hashrate_hashboard_avg,
        sm0_hashrates, sm0_freqs, sm0_temps, sm0_chips,
        sm1_hashrates, sm1_freqs, sm1_temps, sm1_chips,
        sm2_hashrates, sm2_freqs, sm2_temps, sm2_chips,
        psu_wattages
    ) = data_organization.output_file_unpacker(file)

    # Organize the data for the wattage graph
    wattage_x, wattage_y = data_organization.overall_wattage(psu_wattages)

    # Create a figure and axes for the wattage graph
    fig3, ax3 = plt.subplots()

    # Plot the data on the axes
    ax3.plot(wattage_x, wattage_y, label='PSU Wattage')
    ax3.legend()

    plt.autoscale(True)
    plt.show()


def output_file_chip_temps(file):
    # Unpack the data from the output file
    (
        hashrate_hashboard_avg,
        sm0_hashrates, sm0_freqs, sm0_temps, sm0_chips,
        sm1_hashrates, sm1_freqs, sm1_temps, sm1_chips,
        sm2_hashrates, sm2_freqs, sm2_temps, sm2_chips,
        psu_wattages
    ) = data_organization.output_file_unpacker(file)

    # Organize the data for the chip temperature graph
    (
        chip_temp_x, chip_temp_y1, chip_temp_y2, chip_temp_y3
    ) = data_organization.hashboard_chip_temps(sm0_chips, sm1_chips, sm2_chips)

    # Create a figure and axes for the chip temperature graph
    fig2, ax2 = plt.subplots()

    # Plot the data on the axes
    ax2.plot(chip_temp_x, chip_temp_y1, label='SM0 Chip Temp')
    ax2.plot(chip_temp_x, chip_temp_y2, label='SM1 Chip Temp')
    ax2.plot(chip_temp_x, chip_temp_y3, label='SM2 Chip Temp')
    ax2.legend()

    plt.autoscale(True)
    plt.show()


def output_file_frequency(file):
    # Unpack the data from the output file
    (
        hashrate_hashboard_avg,
        sm0_hashrates, sm0_freqs, sm0_temps, sm0_chips,
        sm1_hashrates, sm1_freqs, sm1_temps, sm1_chips,
        sm2_hashrates, sm2_freqs, sm2_temps, sm2_chips,
        psu_wattages
    ) = data_organization.output_file_unpacker(file)

    # Organize the data for the frequency graph
    (
        freq_x, freq_y1, freq_y2, freq_y3
    ) = data_organization.hashboard_freqs(sm0_freqs, sm1_freqs, sm2_freqs)

    # Create a figure and axes for the frequency graph
    fig4, ax4 = plt.subplots()

    # Plot the data on the axes
    ax4.plot(freq_x, freq_y1, label='SM0 Frequency')
    ax4.plot(freq_x, freq_y2, label='SM1 Frequency')
    ax4.plot(freq_x, freq_y3, label='SM2 Frequency')
    ax4.legend()

    plt.autoscale(True)
    plt.show()


# Create the main window
root = ctk.CTk()
root.title("Log Visualizer")

# Create the file selection button
file_output = ctk.CTkButton(
    root,
    text="Select File",
    command=log_file_retriever
)

# Place the file selection button at (15, 10) in pixels
file_output.place(x=15, y=10, width=115)

# Create the graph all button
graph_all_button = ctk.CTkButton(
    root,
    text="Graph All",
    command=lambda: output_file_graphing(open('functions/output_data.log'))
)

# Place the graph all button at (15, 70) in pixels
graph_all_button.place(x=15, y=70, width=115)

# Create the graph hashrate button
graph_hashrate_button = ctk.CTkButton(
    root,
    text="Graph Hashrate",
    command=lambda: output_file_hashrate(open('functions/output_data.log'))
)

# Place the graph hashrate button at (130, 10) in pixels
graph_hashrate_button.place(x=130, y=10, width=150)

# Create the graph wattage button
graph_wattage_button = ctk.CTkButton(
    root,
    text="Graph Wattage",
    command=lambda: output_file_wattage(open('functions/output_data.log'))
)

# Place the graph wattage button at (130, 50) in pixels
graph_wattage_button.place(x=130, y=50, width=150)

# Create the graph chip temps button
graph_chip_temps_button = ctk.CTkButton(
    root,
    text="Graph Chip Temps",
    command=lambda: output_file_chip_temps(open('functions/output_data.log'))
)

# Place the graph chip temps button at (130, 90) in pixels
graph_chip_temps_button.place(x=130, y=90, width=150)

# Create the graph frequency button
graph_frequency_button = ctk.CTkButton(
    root,
    text="Graph Frequency",
    command=lambda: output_file_frequency(open('functions/output_data.log'))
)

# Place the graph frequency button at (130, 130) in pixels
graph_frequency_button.place(x=130, y=130, width=150)

# Create the close button
close_frame_button = ctk.CTkButton(
    root,
    text="Close",
    command=root.destroy
)

# Place the close button at (15, 130) in pixels
close_frame_button.place(x=15, y=130, width=115)

# Set the size of the main window and start the main loop
root.geometry("280x175")
root.mainloop()
