import numpy as np

from utils import prepare_exp_data, parse_rt_data_from_directory


def main():
    exp_1_data_directory = "./realtime_amplification_exp_01"
    exp_1_data = parse_rt_data_from_directory(exp_1_data_directory, "a")
    cycles_exp_1 = np.array([5, 10, 15, 20] + [(i + 11) * 2 for i in range(12)])
    top_mean_values_exp_1 = np.array([i["top"] for i in exp_1_data])
    bottom_mean_values_exp_1 = np.array([i["bottom"] for i in exp_1_data])
    prepare_exp_data(cycles_exp_1, top_mean_values_exp_1, bottom_mean_values_exp_1, "exp_1")

    exp_2_data_directory = "./realtime_amplification_exp_02"
    exp_2_data = parse_rt_data_from_directory(exp_2_data_directory, "a")
    cycles_exp_2 = np.array([5, 10, 15] + [i + 16 for i in range(30)])
    top_mean_values_exp_2 = np.array([i["top"] for i in exp_2_data])
    bottom_mean_values_exp_2 = np.array([i["bottom"] for i in exp_2_data])
    prepare_exp_data(cycles_exp_2, top_mean_values_exp_2, bottom_mean_values_exp_2, "exp_2")

    exp_3_data_directory = "./realtime_amplification_exp_03"
    exp_3_data = parse_rt_data_from_directory(exp_3_data_directory, "a")
    cycles_exp_3 = np.array([5, 10, 15] + [i + 16 for i in range(30)])
    top_mean_values_exp_3 = np.array([i["top"] for i in exp_3_data])
    bottom_mean_values_exp_3 = np.array([i["bottom"] for i in exp_3_data])
    prepare_exp_data(cycles_exp_3, top_mean_values_exp_3, bottom_mean_values_exp_3, "exp_3")

    exp_4_data_directory = "./realtime_amplification_exp_04"
    exp_4_data = parse_rt_data_from_directory(exp_4_data_directory, "a")
    cycles_exp_4 = np.array([i + 1 for i in range(len(exp_4_data))])
    top_mean_values_exp_4 = np.array([i["top"] for i in exp_4_data])
    bottom_mean_values_exp_4 = np.array([i["bottom"] for i in exp_4_data])
    prepare_exp_data(cycles_exp_4, top_mean_values_exp_4, bottom_mean_values_exp_4, "exp_4")

    exp_5_data_directory = "./realtime_amplification_exp_05"
    exp_5_data = parse_rt_data_from_directory(exp_5_data_directory, "a")
    cycles_exp_5 = np.array([i + 1 for i in range(len(exp_5_data))])
    top_mean_values_exp_5 = np.array([i["top"] for i in exp_5_data])
    bottom_mean_values_exp_5 = np.array([i["bottom"] for i in exp_5_data])
    prepare_exp_data(cycles_exp_5, top_mean_values_exp_5, bottom_mean_values_exp_5, "exp_5")

    exp_6_data_directory = "./realtime_amplification_exp_06"
    exp_6_data = parse_rt_data_from_directory(exp_6_data_directory, "a")
    cycles_exp_6 = np.array([i + 1 for i in range(len(exp_6_data))])
    top_mean_values_exp_6 = np.array([i["top"] for i in exp_6_data])
    bottom_mean_values_exp_6 = np.array([i["bottom"] for i in exp_6_data])
    prepare_exp_data(cycles_exp_6, top_mean_values_exp_6, bottom_mean_values_exp_6, "exp_6")

    exp_7_data_directory = "./realtime_amplification_exp_07"
    exp_7_data = parse_rt_data_from_directory(exp_7_data_directory, "g")
    cycles_exp_7 = np.array([i + 1 for i in range(len(exp_7_data))])
    top_mean_values_exp_7 = np.array([i["top"] for i in exp_7_data])
    bottom_mean_values_exp_7 = np.array([i["bottom"] for i in exp_7_data])
    prepare_exp_data(cycles_exp_7, top_mean_values_exp_7, bottom_mean_values_exp_7, "exp_7")

    exp_8_data_directory = "./realtime_amplification_exp_08"
    exp_8_data = parse_rt_data_from_directory(exp_8_data_directory, "g")
    cycles_exp_8 = np.array([i + 1 for i in range(len(exp_8_data))])
    top_mean_values_exp_8 = np.array([i["top"] for i in exp_8_data])
    bottom_mean_values_exp_8 = np.array([i["bottom"] for i in exp_8_data])
    prepare_exp_data(cycles_exp_8, top_mean_values_exp_8, bottom_mean_values_exp_8, "exp_8")

    exp_9_data_directory = "./realtime_amplification_exp_09"
    exp_9_data = parse_rt_data_from_directory(exp_9_data_directory, "g")
    cycles_exp_9 = np.array([i + 1 for i in range(len(exp_9_data))])
    top_mean_values_exp_9 = np.array([i["top"] for i in exp_9_data])
    bottom_mean_values_exp_9 = np.array([i["bottom"] for i in exp_9_data])
    prepare_exp_data(cycles_exp_9, top_mean_values_exp_9, bottom_mean_values_exp_9, "exp_9")

    exp_11_data_directory = "./realtime_amplification_exp_11"
    exp_11_data = parse_rt_data_from_directory(exp_11_data_directory, "g")
    cycles_exp_11 = np.array([i + 1 for i in range(len(exp_11_data))])
    top_mean_values_exp_11 = np.array([i["top"] for i in exp_11_data])
    bottom_mean_values_exp_11 = np.array([i["bottom"] for i in exp_11_data])
    prepare_exp_data(cycles_exp_11, top_mean_values_exp_11, bottom_mean_values_exp_11, "exp_11")

    exp_12_data_directory = "./realtime_amplification_exp_12"
    exp_12_data = parse_rt_data_from_directory(exp_12_data_directory, "g")
    cycles_exp_12 = np.array([i + 1 for i in range(len(exp_12_data))])
    top_mean_values_exp_12 = np.array([i["top"] for i in exp_12_data])
    bottom_mean_values_exp_12 = np.array([i["bottom"] for i in exp_12_data])
    prepare_exp_data(cycles_exp_12, top_mean_values_exp_12, bottom_mean_values_exp_12, "exp_12")

    exp_13_data_directory = "./realtime_amplification_exp_13"
    exp_13_data = parse_rt_data_from_directory(exp_13_data_directory, "g")
    cycles_exp_13 = np.array([i + 1 for i in range(len(exp_13_data))])
    top_mean_values_exp_13 = np.array([i["top"] for i in exp_13_data])
    bottom_mean_values_exp_13 = np.array([i["bottom"] for i in exp_13_data])
    prepare_exp_data(cycles_exp_13, top_mean_values_exp_13, bottom_mean_values_exp_13, "exp_13")


if __name__ == "__main__":
    main()
