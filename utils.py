import os
import re

import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

from aproximation_models import ApproximationModels


def prepare_exp_data(cycles, top_values, bottom_values, exp_name):
    model = ApproximationModels.polynomial_4
    df = pd.DataFrame(
        {"cycles": cycles, "top_mean_values": top_values, "bottom_mean_values": bottom_values, "experiment": exp_name}
    )
    df["top_gradient"] = df["top_mean_values"].diff() / df["cycles"].diff()
    df["bottom_gradient"] = df["bottom_mean_values"].diff() / df["cycles"].diff()

    popt, _ = curve_fit(model, df["cycles"], df["top_mean_values"])
    df["top_mean_values_approximated"] = model(df["cycles"], *popt)

    popt, _ = curve_fit(model, df["cycles"], df["bottom_mean_values"])
    df["bottom_mean_values_approximated"] = model(df["cycles"], *popt)

    df["top_approximated_gradient"] = df["top_mean_values_approximated"].diff() / df["cycles"].diff()
    df["bottom_approximated_gradient"] = df["bottom_mean_values_approximated"].diff() / df["cycles"].diff()

    df.to_csv(f"{exp_name}.csv", index=False)


def get_ordered_folders(root_directory):
    pattern = re.compile(r"^C(\d+)\.1$")

    folders = []

    for root, dirs, files in os.walk(root_directory):
        for dir_name in dirs:
            if pattern.match(dir_name):
                folders.append(dir_name)

    folders.sort(key=lambda x: int(pattern.match(x).group(1)))

    return folders


def parse_expose_log(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

    headers = re.findall(r"(\w+ \w+)", lines[0])

    data = []

    for line in lines[2:]:
        values = re.findall(r"(\d{8}) (\d{4})", line)
        if values:
            data.append(dict(zip(headers, values)))

    return data


def extract_data_from_directory(directory):
    all_data = []
    folders = get_ordered_folders(directory)
    for folder in folders:
        path_to_data = os.path.join(os.path.join(directory, folder), "expose_log.txt")
        parsed_data = parse_expose_log(path_to_data)
        if parsed_data:
            result = {
                "top": int(parsed_data[0]["us code"][1]),
                "bottom": int(parsed_data[1]["us code"][1]),
            }
        else:
            result = {"top": 0, "bottom": 0}
        all_data.append(result)

    return all_data


def parse_rt_data_from_directory(directory, chanel):
    all_data = []
    channels = {"a": 4, "c": 6, "g": 8, "t": 10}
    path_to_data = os.path.join(directory, "rt.rt")
    with open(path_to_data, "r") as file:
        lines = file.readlines()

    for i in range(0, len(lines), 2):
        point = {
            "top": int(lines[i].split(";")[channels[chanel]]),
            "bottom": int(lines[i + 1].split(";")[channels[chanel]]),
        }
        all_data.append(point)

    return all_data
