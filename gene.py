import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
from dash.dependencies import Input, Output, State

# Load the data
df = pd.read_csv('gene.csv')

# Define the app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.Img(src="http://127.0.0.1:5000/static/images/logo.jpg", alt='Logo', style={'float': 'left', 'height': '100px'}),
    html.Img(src="http://127.0.0.1:5000/static/images/uni.jpg", alt='University', style={'display': 'block', 'margin': 'auto', 'height': '100px'}),
    html.Nav(style={'text-align': 'center'}, children=[
        html.Ul(style={'display': 'inline-block'}, children=[
            html.Li(style={'display': 'inline-block', 'margin-right': '300px'}, children=[
                html.A('Home', href='http://127.0.0.1:5000', style={'font-size': '30px', 'font-weight': 'bold', 'text-decoration': 'none', 'color': 'black'})
            ]),
            html.Li(style={'display': 'inline-block', 'margin-right': '300px'}, children=[
                html.A('Analysis', href='http://127.0.0.1:5000/analysis', style={'font-size': '30px', 'font-weight': 'bold', 'text-decoration': 'none', 'color': 'black'})
            ]),
            html.Li(style={'display': 'inline-block'}, children=[
                html.A('Contact Us', href='http://127.0.0.1:5000/contact', style={'font-size': '30px', 'font-weight': 'bold', 'text-decoration': 'none', 'color': 'black'})
            ])
        ])
    ]),
    html.H1("Gene Data"),
    html.Div([
        dcc.Dropdown(
            id='dropdown',
            options=[{'label': 'Gene Symbol', 'value': 'gene_symbol'},
                     {'label': 'ENTREZ GENE ID', 'value': 'entrez_gene_id'}],
            value='gene_symbol',
            style={'width': '40%'}
        ),
        dcc.Input(id='search-box', type='text', placeholder='Enter a search term', style={'width': '40%'}),
        html.Button('Submit', id='submit-button', style={'marginLeft': '10px'})
    ], style={'display': 'flex', 'justifyContent': 'center'}),
    html.Br(),
    html.H3("Gene Information"),
    dash_table.DataTable(
        id='search-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        style_table={'overflowX': 'auto'},
        style_cell={
            'textAlign': 'center',
            'minWidth': '0px', 'maxWidth': '180px',
            'whiteSpace': 'normal',
            'textOverflow': 'ellipsis',
            'fontSize': '12pt'
        }
    )
])


# Define the callback
@app.callback(
    Output('search-table', 'data'),
    Input('submit-button', 'n_clicks'),
    State('dropdown', 'value'),
    State('search-box', 'value')
)
def update_table(n_clicks, dropdown_value, search_term):
    if not search_term:
        return []
    # Filter the dataframe based on the selected dropdown value and search term
    if dropdown_value == 'gene_symbol':
        sub_df = df[df['Gene Symbol'].str.contains(search_term, case=False)]
    else:
        sub_df = df[df['ENTREZ GENE ID'].astype(str).str.contains(search_term, case=False)]
    # Return the selected row as a dictionary
    return sub_df.to_dict('records')

# Run the app
if __name__ == '__main__':
    app.run_server(debug=False, port=9000)
