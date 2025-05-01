import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Caricamento del dataset preparato
df = pd.read_csv('spacex_launches_prepared.csv')

# Inizializzazione dell'app Dash
app = dash.Dash(__name__)

# Calcolo del sito con il più alto tasso di successo
success_rates = df.groupby('LaunchSite')['Class'].mean().reset_index()
highest_success_site = success_rates.loc[success_rates['Class'].idxmax(), 'LaunchSite']

# Layout del dashboard
app.layout = html.Div([
    html.H1("SpaceX Launch Dashboard"),
    
    # Pie chart: Conteggio dei successi per tutti i siti
    html.H2("Launch Success Count for All Sites"),
    dcc.Graph(id='success-pie-chart-all'),
    
    # Pie chart: Sito con il più alto tasso di successo
    html.H2("Launch Site with Highest Success Rate"),
    dcc.Graph(id='success-pie-chart-highest'),
    
    # Scatter plot: Payload vs. Launch Outcome con slider
    html.H2("Payload vs. Launch Outcome"),
    dcc.Graph(id='payload-scatter-plot'),
    dcc.RangeSlider(
        id='payload-slider',
        min=df['PayloadMass'].min(),
        max=df['PayloadMass'].max(),
        value=[df['PayloadMass'].min(), df['PayloadMass'].max()],
        marks={int(payload): str(int(payload)) for payload in df['PayloadMass'].unique() if payload % 2000 == 0},
        step=None
    )
])

# Callback per il pie chart di tutti i siti
@app.callback(
    Output('success-pie-chart-all', 'figure'),
    [Input('payload-slider', 'value')]
)
def update_pie_chart_all(payload_range):
    fig = px.pie(df, names='Class', title='Launch Success Count for All Sites',
                 labels={'Class': 'Outcome (0=Failure, 1=Success)'})
    return fig

# Callback per il pie chart del sito con il più alto tasso di successo
@app.callback(
    Output('success-pie-chart-highest', 'figure'),
    [Input('payload-slider', 'value')]
)
def update_pie_chart_highest(payload_range):
    site_df = df[df['LaunchSite'] == highest_success_site]
    fig = px.pie(site_df, names='Class', title=f'Launch Success for {highest_success_site}',
                 labels={'Class': 'Outcome (0=Failure, 1=Success)'})
    return fig

# Callback per lo scatter plot
@app.callback(
    Output('payload-scatter-plot', 'figure'),
    [Input('payload-slider', 'value')]
)
def update_scatter_plot(payload_range):
    filtered_df = df[(df['PayloadMass'] >= payload_range[0]) & (df['PayloadMass'] <= payload_range[1])]
    fig = px.scatter(filtered_df, x='PayloadMass', y='Outcome', color='Class',
                     title='Payload vs. Launch Outcome', labels={'Class': 'Success'})
    return fig

# Esecuzione dell'app
if __name__ == '__main__':
    app.run(debug=True)