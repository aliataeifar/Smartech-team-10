from dash import Dash, dcc, Output, Input
import dash_bootstrap_components as dbc
import dash_html_components as html
import os
import plotly.graph_objects as go

external_scripts = [
    {'src': 'https://code.jquery.com/jquery-3.6.0.min.js'}, {'src': 'https://cdn.datatables.net/v/dt/dt-1.13.4/datatables.min.js'} ]
external_stylesheets = [
    'assets/codes/custom.css', 'assets/codes/dataTable.css', ]

app = Dash(__name__, external_stylesheets=external_stylesheets,external_scripts=external_scripts)

question_div = html.Div()
question_text = html.H1('دنبال چه می گردی؟', id='question_text')
question_input = dbc.Input(placeholder='تایپ کنید', id='question_input')
question_btn = dbc.Button('نمایش نتایج', className='show_results')
my_graph = dcc.Graph(figure={})

my_btn = dbc.Button('نمایش نمودار', className='show_results')


@app.callback(
    Output(question_div, component_property='children'),
    Input(question_btn, component_property='n_clicks'),
        prevent_initial_call=True

)
def create_table(n_clicks):
    if n_clicks:
        rows = [
            html.Thead([html.Tr([html.Th('ردیف'), html.Th('عنوان'), html.Th('قیمت'), html.Th('تصویر')])])]
        nested_rows = []
        with open('titles.txt', encoding='utf-8') as f:
            titles = f.read().split('\n')
        with open('prices.txt') as f:
            prices = f.read().split('\n')
        with open('links.txt') as f:
            links = f.read().split('\n')
        image_list = os.listdir('assets/images')
        i = 1
        for t, p, l, image_name in zip(titles, prices, links, image_list):
            img = html.Img(src=app.get_asset_url(
                f'images/{image_name}'), width='100px', height='100px')
            d = html.Tr([html.Td(i), html.Td(html.A(t, href=l)), html.Td(
                p), html.Td(img)])
            i = i+1
            nested_rows.append(d)
        rows.append(html.Tbody(nested_rows))
        children = html.Table(rows, id='results_table')
        return children


@app.callback(
    Output(my_graph, component_property='figure'),
    Output(my_btn, component_property='n_clicks'),
    Input(my_btn, component_property='n_clicks'),
        prevent_initial_call=True

)
def show_images(n_clicks):
    if n_clicks:

        with open('prices.txt') as f:
            number_list = f.read().split('\n')

        number_list = list(map(int, number_list))
        print(number_list)
        figure = go.Figure(data=go.Scatter(
            x=list(range(0, len(number_list))), y=number_list))
        return figure, n_clicks


app.layout = dbc.Container([
    dbc.Row([question_text, question_input, question_btn]),
    dbc.Row([question_div]),
    dbc.Row([my_graph, my_btn])
], id='question_container')

if __name__ == '__main__':
    app.run_server(port='8000')
