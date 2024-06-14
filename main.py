import numpy as np
from scipy.interpolate import interp1d
import plotly.graph_objects as go
from plotly.subplots import make_subplots

cycles_exp_1 = np.array([5, 10, 15, 20] + [(i + 11) * 2 for i in range(12)])
top_mean_values_exp_1 = np.array([15, 17, 23, 253, 0, 358, 410, 461, 491, 523, 583, 616, 655, 685, 731, 775])
bottom_mean_values_exp_1 = np.array([15, 17, 23, 255, 0, 358, 412, 463, 501, 540, 604, 642, 689, 730, 791, 848])

cycles_exp_2 = np.array([5, 10, 15] + [i + 16 for i in range(30)])
top_mean_values_exp_2 = np.array([44, 39, 46, 49, 56, 0, 69, 86, 101, 113, 129, 142, 157, 177, 191, 203, 227, 244,
                                  252, 259, 281, 291, 312, 328, 336, 363, 374, 381, 397, 413, 428, 444, 461, ])
bottom_mean_values_exp_2 = np.array([43, 38, 43, 46, 50, 0, 73, 93, 108, 122, 140, 155, 170, 194, 209, 223, 251, 265,
                                     277, 283, 313, 319, 344, 362, 372, 401, 415, 428, 443, 463, 480, 499, 523])

cycles_exp_3 = np.array([5, 10, 15] + [i + 16 for i in range(30)])
top_mean_values_exp_3 = np.array([34, 0, 79, 109, 139, 145, 162, 173, 204, 220, 239, 256, 271, 281, 294, 307, 320,
                                  338, 352, 368, 386, 400, 419, 431, 447, 461, 473, 484, 505, 512, 540, 558, 573])
bottom_mean_values_exp_3 = np.array([34, 0, 91, 122, 157, 156, 171, 194, 208, 234, 252, 270, 284, 297, 311, 176, 340,
                                     361, 377, 395, 415, 430, 452, 467, 487, 503, 520, 533, 556, 560, 599, 630, 642])

exp_1_top_diff = np.gradient(top_mean_values_exp_1, cycles_exp_1)
exp_1_bottom_diff = np.gradient(bottom_mean_values_exp_1, cycles_exp_1)
exp_2_top_diff = np.gradient(top_mean_values_exp_2, cycles_exp_2)
exp_2_bottom_diff = np.gradient(bottom_mean_values_exp_2, cycles_exp_2)
exp_3_top_diff = np.gradient(top_mean_values_exp_3, cycles_exp_3)
exp_3_bottom_diff = np.gradient(bottom_mean_values_exp_3, cycles_exp_3)


# exp_1_top_interpolation_f_cubic = interp1d(x, y, kind='cubic')


def main():
    fig = make_subplots(rows=2, cols=2, subplot_titles=(
        "Исходные данные", "Интерполированные данные", "Производная исходных данных", "Производная после интерполяции"))

    fig.add_trace(go.Scatter(x=cycles_exp_1, y=top_mean_values_exp_1, mode='lines+markers', name='Exp. 1 top'), row=1,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_1, y=bottom_mean_values_exp_1, mode='lines+markers', name='Exp. 1 bottom'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_2, y=top_mean_values_exp_2, mode='lines+markers', name='Exp. 2 top'), row=1,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_2, y=bottom_mean_values_exp_2, mode='lines+markers', name='Exp. 2 bottom'),
                  row=1, col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_3, y=top_mean_values_exp_3, mode="lines+markers", name="Exp. 3 top"), row=1,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_3, y=bottom_mean_values_exp_3, mode="lines+markers", name="Exp. 3 bottom"),
                  row=1,
                  col=1)

    fig.add_trace(go.Scatter(x=cycles_exp_1, y=exp_1_top_diff, mode="lines+markers", name="Exp. 1 top diff"), row=2,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_1, y=exp_1_bottom_diff, mode="lines+markers", name="Exp. 1 bottom diff"),
                  row=2,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_2, y=exp_2_top_diff, mode="lines+markers", name="Exp. 2 top diff"), row=2,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_2, y=exp_2_bottom_diff, mode="lines+markers", name="Exp. 2 bottom diff"),
                  row=2,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_3, y=exp_3_top_diff, mode="lines+markers", name="Exp. 3 top diff"), row=2,
                  col=1)
    fig.add_trace(go.Scatter(x=cycles_exp_3, y=exp_3_bottom_diff, mode="lines+markers", name="Exp. 3 bottom diff"),
                  row=2,
                  col=1)

    fig.update_layout(
        title='Интегральные показатели проведения мостиковой амплификации в реальном времени',
        xaxis_title='Цикл амплификации',
        yaxis_title='99 процентиль яркости'
    )

    fig.show()


if __name__ == '__main__':
    main()
