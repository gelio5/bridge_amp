import numpy as np


from utils import extract_data_from_directory, prepare_exp_data


def main():
    cycles_exp_1 = np.array([5, 10, 15, 20] + [(i + 11) * 2 for i in range(12)])
    top_mean_values_exp_1 = np.array([15, 17, 23, 253, 0, 358, 410, 461, 491, 523, 583, 616, 655, 685, 731, 775])
    bottom_mean_values_exp_1 = np.array([15, 17, 23, 255, 0, 358, 412, 463, 501, 540, 604, 642, 689, 730, 791, 848])

    prepare_exp_data(cycles_exp_1, top_mean_values_exp_1, bottom_mean_values_exp_1, "exp_1")

    cycles_exp_2 = np.array([5, 10, 15] + [i + 16 for i in range(30)])
    top_mean_values_exp_2 = np.array(
        [
            44,
            39,
            46,
            49,
            56,
            0,
            69,
            86,
            101,
            113,
            129,
            142,
            157,
            177,
            191,
            203,
            227,
            244,
            252,
            259,
            281,
            291,
            312,
            328,
            336,
            363,
            374,
            381,
            397,
            413,
            428,
            444,
            461,
        ]
    )
    bottom_mean_values_exp_2 = np.array(
        [
            43,
            38,
            43,
            46,
            50,
            0,
            73,
            93,
            108,
            122,
            140,
            155,
            170,
            194,
            209,
            223,
            251,
            265,
            277,
            283,
            313,
            319,
            344,
            362,
            372,
            401,
            415,
            428,
            443,
            463,
            480,
            499,
            523,
        ]
    )
    prepare_exp_data(cycles_exp_2, top_mean_values_exp_2, bottom_mean_values_exp_2, "exp_2")

    cycles_exp_3 = np.array([5, 10, 15] + [i + 16 for i in range(30)])
    top_mean_values_exp_3 = np.array(
        [
            34,
            0,
            79,
            109,
            139,
            145,
            162,
            173,
            204,
            220,
            239,
            256,
            271,
            281,
            294,
            307,
            320,
            338,
            352,
            368,
            386,
            400,
            419,
            431,
            447,
            461,
            473,
            484,
            505,
            512,
            540,
            558,
            573,
        ]
    )
    bottom_mean_values_exp_3 = np.array(
        [
            34,
            0,
            91,
            122,
            157,
            156,
            171,
            194,
            208,
            234,
            252,
            270,
            284,
            297,
            311,
            176,
            340,
            361,
            377,
            395,
            415,
            430,
            452,
            467,
            487,
            503,
            520,
            533,
            556,
            560,
            599,
            630,
            642,
        ]
    )
    prepare_exp_data(cycles_exp_3, top_mean_values_exp_3, bottom_mean_values_exp_3, "exp_3")

    exp_4_data_directory = "./realtime_amplification_exp_04/Images/L001"
    exp_4_data = extract_data_from_directory(exp_4_data_directory)
    cycles_exp_4 = np.array([i + 1 for i in range(len(exp_4_data))])
    top_mean_values_exp_4 = np.array([i["top"] for i in exp_4_data])
    bottom_mean_values_exp_4 = np.array([i["bottom"] for i in exp_4_data])
    prepare_exp_data(cycles_exp_4, top_mean_values_exp_4, bottom_mean_values_exp_4, "exp_4")

    exp_5_data_directory = "./realtime_amplification_exp_05/Images/L001"
    exp_5_data = extract_data_from_directory(exp_5_data_directory)
    cycles_exp_5 = np.array([i + 1 for i in range(len(exp_5_data))])
    top_mean_values_exp_5 = np.array([i["top"] for i in exp_5_data])
    bottom_mean_values_exp_5 = np.array([i["bottom"] for i in exp_5_data])
    prepare_exp_data(cycles_exp_5, top_mean_values_exp_5, bottom_mean_values_exp_5, "exp_5")

    exp_6_data_directory = "./realtime_amplification_exp_06/Images/L001"
    exp_6_data = extract_data_from_directory(exp_6_data_directory)
    cycles_exp_6 = np.array([i + 1 for i in range(len(exp_6_data))])
    top_mean_values_exp_6 = np.array([i["top"] for i in exp_6_data])
    bottom_mean_values_exp_6 = np.array([i["bottom"] for i in exp_6_data])
    prepare_exp_data(cycles_exp_6, top_mean_values_exp_6, bottom_mean_values_exp_6, "exp_6")


if __name__ == "__main__":
    main()
