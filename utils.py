import os
import re

import pandas as pd
import numpy as np


def prepare_exp_data(cycles, top_values, bottom_values, exp_name):
    df = pd.DataFrame({
        'cycles': cycles,
        'top_mean_values': top_values,
        'bottom_mean_values': bottom_values,
        'experiment': exp_name
    })
    df["top_gradient"] = df["top_mean_values"].diff() / df["cycles"].diff()
    df["bottom_gradient"] = df["bottom_mean_values"].diff() / df["cycles"].diff()

    df['top_mean_values_interpolated'] = df['top_mean_values'].replace(0, np.nan)
    df['bottom_mean_values_interpolated'] = df['bottom_mean_values'].replace(0, np.nan)

    df['top_mean_values_interpolated'] = df['top_mean_values_interpolated'].interpolate(method="spline")
    df['bottom_mean_values_interpolated'] = df['bottom_mean_values_interpolated'].interpolate(method="spline")

    df['top_interpolated_gradient'] = df["top_mean_values_interpolated"].diff() / df["cycles"].diff()
    df['bottom_interpolated_gradient'] = df["bottom_mean_values_interpolated"].diff() / df["cycles"].diff()

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
