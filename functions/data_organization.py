import re


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
        sm0_freqs_list.append(round(float(sm0_data[2]), 2))
        sm0_temps_list.append(sm0_data[3])
        sm0_chips_list.append(round(float(sm0_data[4]), 2))

    for sm1_data in sm1:
        sm1_data = sm1_data.split(' ')

        sm1_hashrates_list.append(round(float(sm1_data[1])))
        sm1_freqs_list.append(round(float(sm1_data[2]), 2))
        sm1_temps_list.append(sm1_data[3])
        sm1_chips_list.append(round(float(sm1_data[4]), 2))

    for sm2_data in sm2:
        sm2_data = sm2_data.split(' ')

        sm2_hashrates_list.append(round(float(sm2_data[1])))
        sm2_freqs_list.append(round(float(sm2_data[2]), 2))
        sm2_temps_list.append(sm2_data[3])
        sm2_chips_list.append(round(float(sm2_data[4]), 2))

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


def hashboard_freqs(sm0, sm1, sm2):
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
