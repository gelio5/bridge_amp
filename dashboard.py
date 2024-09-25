from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

external_stylesheets = [dbc.themes.SANDSTONE]
app = Dash(__name__, title="Realtime bridge amplification", external_stylesheets=external_stylesheets)

df_exp_1 = pd.read_csv("exp_1.csv")
df_exp_2 = pd.read_csv("exp_2.csv")
df_exp_3 = pd.read_csv("exp_3.csv")
df_exp_4 = pd.read_csv("exp_4.csv")
df_exp_5 = pd.read_csv("exp_5.csv")
df_exp_6 = pd.read_csv("exp_6.csv")
df_exp_7 = pd.read_csv("exp_7.csv")
df_exp_8 = pd.read_csv("exp_8.csv")
df_exp_9 = pd.read_csv("exp_9.csv")
df_exp_11 = pd.read_csv("exp_11.csv")
df_exp_12 = pd.read_csv("exp_12.csv")
df_exp_13 = pd.read_csv("exp_13.csv")
df_exp_14 = pd.read_csv("exp_14.csv")
df_exp_15 = pd.read_csv("exp_15.csv")
df_exp_16 = pd.read_csv("exp_16.csv")
df_exp_17 = pd.read_csv("exp_17.csv")
df_exp_18 = pd.read_csv("exp_18.csv")
df_exp_19 = pd.read_csv("exp_19.csv")
df_exp_20 = pd.read_csv("exp_20.csv")

df = pd.concat(
    [
        df_exp_1,
        df_exp_2,
        df_exp_3,
        df_exp_4,
        df_exp_5,
        df_exp_6,
        df_exp_7,
        df_exp_8,
        df_exp_9,
        df_exp_11,
        df_exp_12,
        df_exp_13,
        df_exp_14,
        df_exp_15,
        df_exp_16,
        df_exp_17,
        df_exp_18,
        df_exp_19,
        df_exp_20,
    ],
    ignore_index=True,
)

app.layout = dbc.Container(
    [
        html.H1("Мостиковая амплификация в реальном времени", className="text-primary text-center fs-3"),
        dcc.Graph(
            id="raw-data-graph",
            figure={
                "data": [
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['top_mean_values'], 'type': 'line', 'name': 'exp_1_top'},
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['bottom_mean_values'], 'type': 'line', 'name': 'exp_1_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_2_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_2_bottom",
                    },
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['top_mean_values'], 'type': 'line', 'name': 'exp_3_top'},
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['bottom_mean_values'], 'type': 'line', 'name': 'exp_3_bottom'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['top_mean_values'], 'type': 'line', 'name': 'exp_4_top'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['bottom_mean_values'], 'type': 'line', 'name': 'exp_4_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_5_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_5_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_6_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_6_bottom",
                    },
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['top_mean_values'], 'type': 'line', 'name': 'exp_7_top'},
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['bottom_mean_values'], 'type': 'line',
                     'name': 'exp_7_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_8_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_8_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_9_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_9_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_11_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_11_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_12_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_12_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_13_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_13_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_14_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_14_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_15_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_15_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_16_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_16_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_17_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_17_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_18_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_18_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_19_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_19_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["top_mean_values"],
                        "type": "line",
                        "name": "exp_20_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["bottom_mean_values"],
                        "type": "line",
                        "name": "exp_20_bottom",
                    },
                ],
                "layout": {
                    "title": "Raw Mean Values vs Cycles",
                    "xaxis": {"title": "Cycles"},
                    "yaxis": {"title": "Top Mean Values"},
                    "hovermode": "x unified",
                },
            },
        ),
        dcc.Graph(
            id="interpolated-data-graph",
            figure={
                "data": [
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['top_mean_values_approximated'], 'type': 'line',
                    #  'name': 'exp_1_top'},
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['bottom_mean_values_approximated'], 'type': 'line',
                    #  'name': 'exp_1_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_2_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_2_bottom",
                    },
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['top_mean_values_approximated'], 'type': 'line',
                    #  'name': 'exp_3_top'},
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['bottom_mean_values_approximated'], 'type': 'line',
                    #  'name': 'exp_3_bottom'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['top_mean_values_approximated'], 'type': 'line',
                    #  'name': 'exp_4_top'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['bottom_mean_values_approximated'], 'type': 'line',
                    #  'name': 'exp_4_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_5_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_5_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_6_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_6_bottom",
                    },
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['top_mean_values_approximated'], 'type': 'line',
                     'name': 'exp_7_top'},
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['bottom_mean_values_approximated'], 'type': 'line',
                     'name': 'exp_7_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_8_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_8_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_9_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_9_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_11_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_11_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_12_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_12_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_13_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_13_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_14_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_14_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_15_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_15_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_16_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_16_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_17_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_17_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_18_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_18_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_19_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_19_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["top_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_20_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["bottom_mean_values_approximated"],
                        "type": "line",
                        "name": "exp_20_bottom",
                    },
                ],
                "layout": {
                    "title": "Interpolated Mean Values vs Cycles",
                    "xaxis": {"title": "Cycles"},
                    "yaxis": {"title": "Interpolated Mean Values"},
                    "hovermode": "x unified",
                },
            },
        ),
        dcc.Graph(
            id="raw-data-gradient-graph",
            figure={
                "data": [
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['top_gradient'], 'type': 'line', 'name': 'exp_1_top'},
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['bottom_gradient'], 'type': 'line', 'name': 'exp_1_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["top_gradient"],
                        "type": "line",
                        "name": "exp_2_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_2_bottom",
                    },
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['top_gradient'], 'type': 'line', 'name': 'exp_3_top'},
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['bottom_gradient'], 'type': 'line', 'name': 'exp_3_bottom'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['top_gradient'], 'type': 'line', 'name': 'exp_4_top'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['bottom_gradient'], 'type': 'line', 'name': 'exp_4_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["top_gradient"],
                        "type": "line",
                        "name": "exp_5_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_5_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["top_gradient"],
                        "type": "line",
                        "name": "exp_6_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_6_bottom",
                    },
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['top_gradient'], 'type': 'line', 'name': 'exp_7_top'},
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['bottom_gradient'], 'type': 'line', 'name': 'exp_7_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["top_gradient"],
                        "type": "line",
                        "name": "exp_8_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_8_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["top_gradient"],
                        "type": "line",
                        "name": "exp_9_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_9_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["top_gradient"],
                        "type": "line",
                        "name": "exp_11_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_11_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["top_gradient"],
                        "type": "line",
                        "name": "exp_12_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_12_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["top_gradient"],
                        "type": "line",
                        "name": "exp_13_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_13_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["top_gradient"],
                        "type": "line",
                        "name": "exp_14_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_14_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["top_gradient"],
                        "type": "line",
                        "name": "exp_15_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_15_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["top_gradient"],
                        "type": "line",
                        "name": "exp_16_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_16_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["top_gradient"],
                        "type": "line",
                        "name": "exp_17_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_17_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["top_gradient"],
                        "type": "line",
                        "name": "exp_18_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_18_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["top_gradient"],
                        "type": "line",
                        "name": "exp_19_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_19_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["top_gradient"],
                        "type": "line",
                        "name": "exp_20_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["bottom_gradient"],
                        "type": "line",
                        "name": "exp_20_bottom",
                    },
                ],
                "layout": {
                    "title": "Mean Values Gragient vs Cycles",
                    "xaxis": {"title": "Cycles"},
                    "yaxis": {"title": "Bottom Mean Values"},
                    "hovermode": "x unified",
                },
            },
        ),
        dcc.Graph(
            id="interpolated-gradient-graph",
            figure={
                "data": [
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['top_approximated_gradient'], 'type': 'line',
                    #  'name': 'exp_1_top'},
                    # {'x': df[df['experiment'] == 'exp_1']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_1']['bottom_approximated_gradient'], 'type': 'line',
                    #  'name': 'exp_1_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_2_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_2"]["cycles"],
                        "y": df[df["experiment"] == "exp_2"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_2_bottom",
                    },
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['top_approximated_gradient'], 'type': 'line',
                    #  'name': 'exp_3_top'},
                    # {'x': df[df['experiment'] == 'exp_3']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_3']['bottom_approximated_gradient'], 'type': 'line',
                    #  'name': 'exp_3_bottom'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['top_approximated_gradient'], 'type': 'line',
                    #  'name': 'exp_4_top'},
                    # {'x': df[df['experiment'] == 'exp_4']['cycles'],
                    #  'y': df[df['experiment'] == 'exp_4']['bottom_approximated_gradient'], 'type': 'line',
                    #  'name': 'exp_4_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_5_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_5"]["cycles"],
                        "y": df[df["experiment"] == "exp_5"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_5_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_6_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_6"]["cycles"],
                        "y": df[df["experiment"] == "exp_6"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_6_bottom",
                    },
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['top_approximated_gradient'], 'type': 'line',
                     'name': 'exp_7_top'},
                    {'x': df[df['experiment'] == 'exp_7']['cycles'],
                     'y': df[df['experiment'] == 'exp_7']['bottom_approximated_gradient'], 'type': 'line',
                     'name': 'exp_7_bottom'},
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_8_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_8"]["cycles"],
                        "y": df[df["experiment"] == "exp_8"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_8_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_9_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_9"]["cycles"],
                        "y": df[df["experiment"] == "exp_9"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_9_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_11_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_11"]["cycles"],
                        "y": df[df["experiment"] == "exp_11"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_11_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_12_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_12"]["cycles"],
                        "y": df[df["experiment"] == "exp_12"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_12_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_13_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_13"]["cycles"],
                        "y": df[df["experiment"] == "exp_13"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_13_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_14_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_14"]["cycles"],
                        "y": df[df["experiment"] == "exp_14"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_14_bottom",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_15_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_15"]["cycles"],
                        "y": df[df["experiment"] == "exp_15"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_15_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_16_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_16"]["cycles"],
                        "y": df[df["experiment"] == "exp_16"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_16_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_17_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_17"]["cycles"],
                        "y": df[df["experiment"] == "exp_17"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_17_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_18_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_18"]["cycles"],
                        "y": df[df["experiment"] == "exp_18"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_18_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_19_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_19"]["cycles"],
                        "y": df[df["experiment"] == "exp_19"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_19_bottom",
                    },

                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["top_approximated_gradient"],
                        "type": "line",
                        "name": "exp_20_top",
                    },
                    {
                        "x": df[df["experiment"] == "exp_20"]["cycles"],
                        "y": df[df["experiment"] == "exp_20"]["bottom_approximated_gradient"],
                        "type": "line",
                        "name": "exp_20_bottom",
                    },
                ],
                "layout": {
                    "title": "Interpolated Gradient vs Cycles",
                    "xaxis": {"title": "Cycles"},
                    "yaxis": {
                        "title": "Interpolated Gradient Values",
                    },
                    "hovermode": "x unified",
                },
            },
        ),
    ]
)

server = app.server

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
