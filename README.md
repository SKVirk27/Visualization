## Cancer Impact in Asian Countries Dashboard

### Overview

This interactive dashboard presents a comprehensive analysis of cancer's impact across various Asian countries. Utilizing data from the World Health Organization (WHO), it offers insights into cancer mortality rates, healthcare access, and spending patterns across different regions. The dashboard is designed to help stakeholders identify key trends and disparities, enabling targeted strategies for combating cancer.

### Features

- **Interactive Visualization**: Users can select different regions and cancer types to visualize specific data.
- **Data Insights**: Aggregated data provides a detailed look at cancer-specific mortality, healthcare spending, and professional access.
- **Emerging Trends**: Highlights the relationship between healthcare investment and cancer mortality rates.

### Libraries Used

- **Dash**: For creating the web application.
- **Pandas**: For data manipulation.
- **Plotly**: For creating interactive graphs.
- **Dash Bootstrap Components**: For enhanced UI components.

### Installation

To run this application, you need to have the following Python libraries installed:

```bash
pip install dash==2.0.0
pip install pandas==1.3.3
pip install plotly==5.3.1
pip install dash-bootstrap-components==1.0.1
```

### Running the Application

To run the application, use the following command:

```bash
gunicorn app:server
```

### Project Structure

```plaintext
project/
├── app.py
├── WHO_Asia_Cancer_with_Regions.csv
└── README.md
```

### Code Explanation

#### 1. Load and Preprocess Data

The dataset `WHO_Asia_Cancer_with_Regions.csv` is loaded and preprocessed to extract relevant columns for the analysis.

```python
import pandas as pd

df = pd.read_csv('/Users/simranjitvirk/Downloads/Project2/WHO_Asia_Cancer_with_Regions.csv')
```

#### 2. Initialize Dash App

The Dash application is initialized with Bootstrap for styling.

```python
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
```

#### 3. Define Layout

The layout includes a header, an introduction section, and two dropdowns for selecting the region and cancer type. It also includes a graph component to display the data.

```python
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
            options=[{'label': 'All', 'value': 'All'}] + [{'label': region, 'value': region} for region in df['Region'].unique()],
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
])
```

#### 4. Callback for Interactive Graph

The callback updates the graph based on the selected region and cancer type.

```python
from dash.dependencies import Input, Output
import plotly.express as px

@app.callback(
    Output('my-graph', 'figure'),
    [Input('region-dropdown', 'value'),
     Input('cancer-type-dropdown', 'value')]
)
def update_figure(selected_region, selected_cancer):
    if selected_region == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['Region'] == selected_region]

    fig = px.bar(
        filtered_df,
        x='Country',
        y=selected_cancer,
        title=f"{selected_cancer} Rates in Asian Countries",
        color='Country'
    )
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    return fig
```

#### 5. Run the App

To run the app, use the following command in your terminal:

```python
if __name__ == '__main__':
    app.run_server(debug=True)
```

### Conclusion

This project provides an interactive tool to visualize the impact of cancer across Asian countries. It highlights the importance of healthcare investment and its correlation with cancer mortality rates. By exploring this dashboard, stakeholders can identify critical areas for intervention and improve healthcare strategies to combat cancer more effectively.
