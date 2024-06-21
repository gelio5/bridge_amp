from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

external_stylesheets = [dbc.themes.SANDSTONE]
app = Dash(__name__, external_stylesheets=external_stylesheets)

df_exp_1 = pd.read_csv("exp_1.csv")
df_exp_2 = pd.read_csv("exp_2.csv")
df_exp_3 = pd.read_csv("exp_3.csv")
df_exp_4 = pd.read_csv("exp_4.csv")
df_exp_5 = pd.read_csv("exp_5.csv")
df_exp_6 = pd.read_csv("exp_6.csv")

df = pd.concat([df_exp_1, df_exp_2, df_exp_3, df_exp_4, df_exp_5, df_exp_6], ignore_index=True)

app.layout = dbc.Container([
    html.H1('Мостиковая амплификация в реальном времени', className="text-primary text-center fs-3"),

    dcc.Graph(
        id='raw-data-graph',
        figure={
            'data': [
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['top_mean_values'], 'type': 'line', 'name': 'exp_1_top'},
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['bottom_mean_values'], 'type': 'line', 'name': 'exp_1_bottom'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['top_mean_values'], 'type': 'line', 'name': 'exp_2_top'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['bottom_mean_values'], 'type': 'line', 'name': 'exp_2_bottom'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['top_mean_values'], 'type': 'line', 'name': 'exp_3_top'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['bottom_mean_values'], 'type': 'line', 'name': 'exp_3_bottom'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['top_mean_values'], 'type': 'line', 'name': 'exp_4_top'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['bottom_mean_values'], 'type': 'line', 'name': 'exp_4_bottom'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['top_mean_values'], 'type': 'line', 'name': 'exp_5_top'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['bottom_mean_values'], 'type': 'line', 'name': 'exp_5_bottom'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['top_mean_values'], 'type': 'line', 'name': 'exp_6_top'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['bottom_mean_values'], 'type': 'line', 'name': 'exp_6_bottom'},
            ],
            'layout': {
                'title': 'Raw Mean Values vs Cycles',
                'xaxis': {'title': 'Cycles'},
                'yaxis': {'title': 'Top Mean Values'}
            }
        }
    ),

    dcc.Graph(
        id='interpolated-data-graph',
        figure={
            'data': [
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['top_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_1_top'},
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['bottom_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_1_bottom'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['top_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_2_top'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['bottom_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_2_bottom'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['top_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_3_top'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['bottom_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_3_bottom'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['top_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_4_top'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['bottom_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_4_bottom'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['top_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_5_top'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['bottom_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_5_bottom'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['top_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_6_top'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['bottom_mean_values_interpolated'], 'type': 'line',
                 'name': 'exp_6_bottom'},
            ],
            'layout': {
                'title': 'Interpolated Mean Values vs Cycles',
                'xaxis': {'title': 'Cycles'},
                'yaxis': {'title': 'Interpolated Mean Values'}
            }
        }
    ),

    dcc.Graph(
        id='raw-data-gradient-graph',
        figure={
            'data': [
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['top_gradient'], 'type': 'line', 'name': 'exp_1_top'},
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['bottom_gradient'], 'type': 'line', 'name': 'exp_1_bottom'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['top_gradient'], 'type': 'line', 'name': 'exp_2_top'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['bottom_gradient'], 'type': 'line', 'name': 'exp_2_bottom'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['top_gradient'], 'type': 'line', 'name': 'exp_3_top'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['bottom_gradient'], 'type': 'line', 'name': 'exp_3_bottom'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['top_gradient'], 'type': 'line', 'name': 'exp_4_top'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['bottom_gradient'], 'type': 'line', 'name': 'exp_4_bottom'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['top_gradient'], 'type': 'line', 'name': 'exp_5_top'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['bottom_gradient'], 'type': 'line', 'name': 'exp_5_bottom'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['top_gradient'], 'type': 'line', 'name': 'exp_6_top'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['bottom_gradient'], 'type': 'line', 'name': 'exp_6_bottom'},
            ],
            'layout': {
                'title': 'Mean Values Gragient vs Cycles',
                'xaxis': {'title': 'Cycles'},
                'yaxis': {'title': 'Bottom Mean Values'}
            }
        }
    ),

    dcc.Graph(
        id='interpolated-gradient-graph',
        figure={
            'data': [
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['top_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_1_top'},
                {'x': df[df['experiment'] == 'exp_1']['cycles'],
                 'y': df[df['experiment'] == 'exp_1']['bottom_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_1_bottom'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['top_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_2_top'},
                {'x': df[df['experiment'] == 'exp_2']['cycles'],
                 'y': df[df['experiment'] == 'exp_2']['bottom_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_2_bottom'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['top_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_3_top'},
                {'x': df[df['experiment'] == 'exp_3']['cycles'],
                 'y': df[df['experiment'] == 'exp_3']['bottom_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_3_bottom'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['top_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_4_top'},
                {'x': df[df['experiment'] == 'exp_4']['cycles'],
                 'y': df[df['experiment'] == 'exp_4']['bottom_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_4_bottom'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['top_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_5_top'},
                {'x': df[df['experiment'] == 'exp_5']['cycles'],
                 'y': df[df['experiment'] == 'exp_5']['bottom_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_5_bottom'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['top_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_6_top'},
                {'x': df[df['experiment'] == 'exp_6']['cycles'],
                 'y': df[df['experiment'] == 'exp_6']['bottom_interpolated_gradient'], 'type': 'line',
                 'name': 'exp_6_bottom'},
            ],
            'layout': {
                'title': 'Interpolated Gradient vs Cycles',
                'xaxis': {'title': 'Cycles'},
                'yaxis': {'title': 'Interpolated Gradient Values'}
            }
        }
    ),
])

server = app.server

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0")