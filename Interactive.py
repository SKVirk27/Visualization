import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

# Load your data
df = pd.read_csv('/Users/simranjitvirk/Downloads/Project2/WHO_Asia_Cancer_with_Regions.csv')

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
     html.H1("Cancer Impact in Asian Countries", style={'textAlign': 'center', 'color': '#007bff'}),
    html.Div(id='introduction', children=[
        dcc.Markdown("""
            ###### Introduction:
            This study addresses the profound health implications of cancer across Asia, identifying key trends and disparities by region. Using comprehensive data, we explore cancer mortality rates, healthcare access, and spending patterns to inform targeted strategies against this disease.
            
            ###### Visualization Aim:
            Our interactive graphs offer insights into cancer prevalence by region and country, made possible with dropdown selectors. This visual tool aids stakeholders in pinpointing critical needs and prioritizing interventions.
            
            ###### Data Insights:
            The `who_asia_cancer_data` set aggregates vital statistics, such as cancer-specific mortality, healthcare spending, and professional access, shedding light on the healthcare-cancer nexus.
            
            ###### Emerging Trends:
            Preliminary findings reveal a strong link between health investment and cancer mortality rates, emphasizing the need for robust healthcare systems.
            
            ###### Conclusion:
            Early data points to the pivotal role of healthcare investment in combating cancer, underlining that such commitments are key to improving outcomes, beyond the measure of national wealth.
        """, style={'backgroundColor': '#f8f9fa', 'borderLeft': '5px solid #007bff', 'padding': '10px', 'margin': '10px 0px'}),
    ]),
   
    html.Div([
        html.Label("Select a Region (Optional):"),
        dcc.Dropdown(
            id='region-dropdown',
            options=[{'label': 'All', 'value': 'All'}] +
                     [{'label': region, 'value': region} for region in df['Region'].unique()],
            value='All'
        ),
    ]),
    html.Div([
        html.Label("Select a Cancer Type:"),
        dcc.Dropdown(
            id='cancer-type-dropdown',
            options=[{'label': i, 'value': i} for i in df.columns if 'cancer' in i.lower()],
            value='Breast_cancer_deaths_per_100_000_women'
        ),
    ]),
    dcc.Graph(id='my-graph'),
    # You can add more content here if needed
])

# Define the callback to update graph
@app.callback(
    Output('my-graph', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('cancer-type-dropdown', 'value')]
)
def update_figure(selected_region, selected_cancer):
    if selected_region == 'All':
        # If 'All' is selected, don't filter on region
        filtered_df = df
    else:
        # Otherwise, filter the dataframe based on the selected region
        filtered_df = df[df['Region'] == selected_region]

    # Update the figure based on the filtered dataframe
    fig = px.bar(
        filtered_df,
        x='Country',
        y=selected_cancer,
        title=f"{selected_cancer} Rates in Asian Countries",
        color='Country'  # This will give each country a unique color
    )
    fig.update_layout(xaxis={'categoryorder':'total descending'})  # Optional: Sort bars
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
