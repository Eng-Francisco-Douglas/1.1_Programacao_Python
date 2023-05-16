import dash
import dash_core_components as dcc
import dash_html_components as html

# Cria o aplicativo Dash
app = dash.Dash(__name__)

# Define o layout da página
app.layout = html.Div(children=[
    html.H1(children='Dashboard Financeiro'),

    html.Div(children='''
        Exemplo de dashboard financeiro usando Python e Dash.
    '''),

    dcc.Graph(
        id='exemplo-grafico',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Receitas'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Despesas'},
            ],
            'layout': {
                'title': 'Exemplo de gráfico de receitas e despesas'
            }
        }
    )
])

# Executa o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)
