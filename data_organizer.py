import re
import matplotlib.pyplot as plt


def output_file_unpacker(lines):
    all_data = []
    run = 0

    for item in lines:
        if run != 0:
            item = re.sub("\n", "", item)
            item = re.sub("'", "", item)
            data = item.split(" | ")
            all_data.append(data)
        else:
            pass
        run += 1

    sm0, sm1, sm2 = [], [], []
    sm0_hashrates_list, sm1_hashrates_list, sm2_hashrates_list = [], [], []
    sm0_freqs_list, sm1_freqs_list, sm2_freqs_list = [], [], []
    sm0_temps_list, sm1_temps_list, sm2_temps_list = [], [], []
    sm0_chips_list, sm1_chips_list, sm2_chips_list = [], [], []
    hashrates, fan_speeds, psu = [], [], []
    psu_wattage_list = []

    for data in all_data:
        hashrates.append(float(data[0]))
        sm0.append(data[1])
        sm1.append(data[2])
        sm2.append(data[3])
        fan_speeds.append(data[4])
        psu.append(data[5])

    for sm0_data in sm0:
        sm0_data = sm0_data.split(' ')

        sm0_hashrates_list.append(round(float(sm0_data[1])))
        sm0_freqs_list.append(sm0_data[2])
        sm0_temps_list.append(sm0_data[3])
        sm0_chips_list.append(round(float(sm0_data[4]), 3))

    for sm1_data in sm1:
        sm1_data = sm1_data.split(' ')

        sm1_hashrates_list.append(round(float(sm1_data[1])))
        sm1_freqs_list.append(sm1_data[2])
        sm1_temps_list.append(sm1_data[3])
        sm1_chips_list.append(round(float(sm1_data[4]), 3))

    for sm2_data in sm2:
        sm2_data = sm2_data.split(' ')

        sm2_hashrates_list.append(round(float(sm2_data[1])))
        sm2_freqs_list.append(sm2_data[2])
        sm2_temps_list.append(sm2_data[3])
        sm2_chips_list.append(round(float(sm2_data[4]), 3))

    for psu_data in psu:
        psu_data = psu_data.split(' ')

        psu_wattage_list.append(int(psu_data[1]))

    return (
        hashrates,
        sm0_hashrates_list, sm0_freqs_list, sm0_temps_list, sm0_chips_list,
        sm1_hashrates_list, sm1_freqs_list, sm1_temps_list, sm1_chips_list,
        sm2_hashrates_list, sm2_freqs_list, sm2_temps_list, sm2_chips_list,
        psu_wattage_list
    )


def overall_hashrate(all_hashrate_data):
    x = []
    y = all_hashrate_data

    for num in range(len(all_hashrate_data)):
        x.append(num)

    return x, y


def hashboard_chip_temps(sm0, sm1, sm2):
    x = []
    y1 = sm0
    y2 = sm1
    y3 = sm2

    for num in range(len(sm0)):
        x.append(num)

    return x, y1, y2, y3


def overall_wattage(all_wattage_data):
    x = []
    y = all_wattage_data

    for num in range(len(all_wattage_data)):
        x.append(num)

    return x, y


if __name__ == "__main__":
    output_file = open('output_data.log', 'r')
    (
        hashrate_hashboard_avg,
        sm0_hashrates, sm0_freqs, sm0_temps, sm0_chips,
        sm1_hashrates, sm1_freqs, sm1_temps, sm1_chips,
        sm2_hashrates, sm2_freqs, sm2_temps, sm2_chips,
        psu_wattages
    ) = output_file_unpacker(output_file)

    hashrate_x, hashrate_y = overall_hashrate(hashrate_hashboard_avg)
    chip_temp_x, chip_temp_y1, chip_temp_y2, chip_temp_y3 = hashboard_chip_temps(sm0_chips, sm1_chips, sm2_chips)
    wattage_x, wattage_y = overall_wattage(psu_wattages)

    plt.subplot(2, 2, 1)
    plt.plot(hashrate_x[0::10], hashrate_y[0::10], label='Hashrate')

    plt.subplot(2, 2, 2)
    plt.plot(chip_temp_x[0::50], chip_temp_y1[0::50], label='SM0 Chip Temp')
    plt.plot(chip_temp_x[0::50], chip_temp_y2[0::50], label='SM1 Chip Temp')
    plt.plot(chip_temp_x[0::50], chip_temp_y3[0::50], label='SM2 Chip Temp')

    plt.subplot(2, 2, 3)
    plt.plot(wattage_x[0::50], wattage_y[0::50], label='PSU Wattage')

    plt.legend()
    plt.show()
