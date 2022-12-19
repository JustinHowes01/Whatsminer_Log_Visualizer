import re


def long_miner_state_log_reader(log_file):
    write_file_headers = (
        "'Total TH/s' "
        "'SM0' 'TH/s' 'Freq' 'Env Temp' 'Chip Temp' "
        "'SM1' 'TH/s' 'Freq' 'Env Temp' 'Chip Temp' "
        "'SM2' 'TH/s' 'Freq' 'Env Temp' 'Chip Temp' "
        "'Fan 1 Speed' 'Fan 2 Speed' "
        "'PSU Fan' 'PSU Wattage' 'PSU Voltage' "
    )

    lines = log_file.readlines()
    write_file_formatted_data = []

    for i in range(len(lines)):
        miner_data = lines[i]

        if 'Miner' in miner_data:
            continue

        miner_data = re.sub('\d\d-\d\d \d\d:\d\d:\d\d ', '', miner_data)
        miner_data = re.sub('\n', '', miner_data)
        miner_data = miner_data.split("|")

        if len(miner_data) < 5:
            continue

        if len(miner_data) != 6:
            miner_data.insert(3, "0,0")

        sm0 = miner_data[0].split(",")
        sm1 = miner_data[1].split(",")
        sm2 = miner_data[2].split(",")

        if len(sm0) < 4:
            sm0.append('0')
        if len(sm1) < 4:
            sm1.append('0')
        if len(sm2) < 4:
            sm2.append('0')

        fan_speeds = miner_data[3].split(",")

        psu = miner_data[5].split(",")

        if int(psu[1]) > 4000:
            psu[1] = '0'

        hashrate = round((float(sm0[0]) / 1000) + (float(sm1[0]) / 1000) + (float(sm2[0]) / 1000), 2)

        write_file_formatted_data.append(
            "'%s'" % hashrate  # Total Hashrate of the miner
            +
            " | "

            "'SM0' "  # Hashboard SM0
            "'%s' "   # TH/s
            "'%s' "   # Hashboard Frequency
            "'%s' "   # Hashboard Environmental Temperature
            "'%s'"    # Hashboard Chip Temperature
            % (round(float(sm0[0]) / 1000, 2), sm0[1], sm0[2], sm0[3])
            +
            " | "

            "'SM1' "  # Hashboard SM1
            "'%s' "   # TH/s
            "'%s' "   # Hashboard Frequency
            "'%s' "   # Hashboard Environmental Temperature
            "'%s'"    # Hashboard Chip Temperature
            % (round(float(sm1[0]) / 1000, 2), sm1[1], sm1[2], sm1[3])
            +
            " | "

            "'SM2' "  # Hashboard SM2
            "'%s' "   # TH/s
            "'%s' "   # Hashboard Frequency
            "'%s' "   # Hashboard Environmental Temperature
            "'%s'"    # Hashboard Chip Temperature
            % (round(float(sm2[0]) / 1000, 2), sm2[1], sm2[2], sm2[3])
            +
            " | "

            "'%s' "  # In fan speed
            "'%s'"   # Out fan speed
            % (fan_speeds[0], fan_speeds[1])
            +
            " | "

            "'%s' "  # PSU fan speed
            "'%s' "  # PSU wattage
            "'%s'"   # PSU voltage
            % (psu[0], psu[1], psu[2])
        )

    return write_file_headers, write_file_formatted_data
