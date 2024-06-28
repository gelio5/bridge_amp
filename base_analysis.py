import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.optimize import curve_fit

from utils import extract_data_from_directory


def polynomial_model(x, a, b, c, d, e):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e


def process_data(base_x_data, base_y_data, name, fig):
    base_y_diff = np.gradient(base_y_data, base_x_data)
    popt, _ = curve_fit(polynomial_model, base_x_data, base_y_data)
    a, b, c, d, e = popt
    y_approximated = polynomial_model(base_x_data, a, b, c, d, e)

    y_approximated_diff = np.gradient(y_approximated, base_x_data)

    fig.add_trace(
        go.Scatter(x=base_x_data, y=base_y_data, mode="lines", name=name, legendgroup=1),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=base_x_data, y=base_y_diff, mode="lines", name=name, legendgroup=2),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=base_x_data, y=y_approximated, mode="lines", name=name, legendgroup=3),
        row=1,
        col=2,
    )
    fig.add_trace(
        go.Scatter(x=base_x_data, y=y_approximated_diff, mode="lines", name=name, legendgroup=4),
        row=2,
        col=2,
    )


def main():
    cycles_exp_1 = np.array([5, 10, 15, 20] + [(i + 11) * 2 for i in range(12)])
    top_mean_values_exp_1 = np.array([15, 17, 23, 253, 0, 358, 410, 461, 491, 523, 583, 616, 655, 685, 731, 775])
    bottom_mean_values_exp_1 = np.array([15, 17, 23, 255, 0, 358, 412, 463, 501, 540, 604, 642, 689, 730, 791, 848])

    df_exp_1_raw = pd.DataFrame(
        {
            "cycles": cycles_exp_1,
            "top_mean_values": top_mean_values_exp_1,
            "bottom_mean_values": bottom_mean_values_exp_1,
            "experiment": "exp_1",
        }
    )
    df_exp_1_raw.to_csv("exp_1_raw.csv", index=False)
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

    exp_4_data_directory = "./realtime_amplification_exp_04/Images/L001"
    exp_4_data = extract_data_from_directory(exp_4_data_directory)
    cycles_exp_4 = np.array([i + 1 for i in range(len(exp_4_data))])
    top_mean_values_exp_4 = np.array([i["top"] for i in exp_4_data])
    bottom_mean_values_exp_4 = np.array([i["bottom"] for i in exp_4_data])

    exp_5_data_directory = "./realtime_amplification_exp_05/Images/L001"
    exp_5_data = extract_data_from_directory(exp_5_data_directory)
    cycles_exp_5 = np.array([i + 1 for i in range(len(exp_5_data))])
    top_mean_values_exp_5 = np.array([i["top"] for i in exp_5_data])
    bottom_mean_values_exp_5 = np.array([i["bottom"] for i in exp_5_data])

    exp_6_data_directory = "./realtime_amplification_exp_06/Images/L001"
    exp_6_data = extract_data_from_directory(exp_6_data_directory)
    cycles_exp_6 = np.array([i + 1 for i in range(len(exp_6_data))])
    top_mean_values_exp_6 = np.array([i["top"] for i in exp_6_data])
    bottom_mean_values_exp_6 = np.array([i["bottom"] for i in exp_6_data])

    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Исходные данные",
            "Апроксимированные данные",
            "Производная исходных данных",
            "Производная после аппроксимации",
        ),
    )

    process_data(cycles_exp_1, top_mean_values_exp_1, "Exp. 1 Top", fig)
    process_data(cycles_exp_1, bottom_mean_values_exp_1, "Exp. 1 Bottom", fig)
    process_data(cycles_exp_2, top_mean_values_exp_2, "Exp. 2 Top", fig)
    process_data(cycles_exp_2, bottom_mean_values_exp_2, "Exp. 2 Bottom", fig)
    process_data(cycles_exp_3, top_mean_values_exp_3, "Exp. 3 Top", fig)
    process_data(cycles_exp_3, bottom_mean_values_exp_3, "Exp. 3 Bottom", fig)
    process_data(cycles_exp_4, top_mean_values_exp_4, "Exp. 4 Top", fig=fig)
    process_data(cycles_exp_4, bottom_mean_values_exp_4, "Exp. 4 Bottom", fig)
    process_data(cycles_exp_5, top_mean_values_exp_5, "Exp. 5 Top", fig)
    process_data(cycles_exp_5, bottom_mean_values_exp_5, "Exp. 5 Bottom", fig)
    process_data(cycles_exp_6, top_mean_values_exp_6, "Exp. 6 Top", fig)
    process_data(cycles_exp_6, bottom_mean_values_exp_6, "Exp. 6 Bottom", fig)
    fig.update_layout(
        title="Интегральные показатели проведения мостиковой амплификации в реальном времени",
        xaxis_title="Цикл амплификации",
        yaxis_title="99 процентиль яркости",
        legend_tracegroupgap=160,
        hovermode="x unified",
    )

    fig.show()


if __name__ == "__main__":
    main()
