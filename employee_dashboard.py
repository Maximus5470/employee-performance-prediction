import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

# Load the data
df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Create binary attrition column if it doesn't exist
if 'AttritionBinary' not in df.columns:
    df['AttritionBinary'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, 
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# App title
app.title = "Employee Performance & Attrition Dashboard"

# Define the layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H1("Employee Performance & Attrition Analysis", className="text-center mb-4 mt-4"),
            html.P("Interactive dashboard for analyzing employee attrition and performance factors", 
                   className="text-center mb-5")
        ], width=12)
    ]),
    
    # Tabs for different sections of the analysis
    dbc.Tabs([
        # Overview Tab
        dbc.Tab(label="Overview", children=[
            dbc.Row([
                dbc.Col([
                    html.H3("Dataset Overview", className="mt-3 mb-3"),
                    html.P("This dashboard analyzes a dataset of 1,470 employees with various attributes related to their work, "
                           "personal characteristics, and job satisfaction. The main focus is on understanding factors that "
                           "contribute to employee attrition and performance ratings."),
                    
                    html.Div(id="dataset-summary", className="mt-3")
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("Attrition by Department", className="mt-4 mb-2"),
                    dcc.Graph(id="attrition-by-department")
                ], width=6),
                
                dbc.Col([
                    html.H4("Attrition by Job Role", className="mt-4 mb-2"),
                    dcc.Graph(id="attrition-by-jobrole")
                ], width=6)
            ])
        ]),
        
        # Demographics Tab
        dbc.Tab(label="Demographics", children=[
            dbc.Row([
                dbc.Col([
                    html.H3("Employee Demographics", className="mt-3 mb-3"),
                    html.P("Explore how demographic factors relate to attrition and performance.")
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("Age Distribution", className="mt-3 mb-2"),
                    dcc.Graph(id="age-distribution")
                ], width=6),
                
                dbc.Col([
                    html.H4("Gender Distribution", className="mt-3 mb-2"),
                    dcc.Graph(id="gender-distribution")
                ], width=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("Education Field", className="mt-4 mb-2"),
                    dcc.Graph(id="education-field")
                ], width=6),
                
                dbc.Col([
                    html.H4("Marital Status", className="mt-4 mb-2"),
                    dcc.Graph(id="marital-status")
                ], width=6)
            ])
        ]),
        
        # Job Satisfaction Tab
        dbc.Tab(label="Job Satisfaction", children=[
            dbc.Row([
                dbc.Col([
                    html.H3("Job Satisfaction Analysis", className="mt-3 mb-3"),
                    html.P("Explore factors related to job satisfaction and their impact on attrition.")
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("Job Satisfaction vs. Attrition", className="mt-3 mb-2"),
                    dcc.Graph(id="job-satisfaction-attrition")
                ], width=6),
                
                dbc.Col([
                    html.H4("Work-Life Balance vs. Attrition", className="mt-3 mb-2"),
                    dcc.Graph(id="worklife-balance-attrition")
                ], width=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("Environment Satisfaction", className="mt-4 mb-2"),
                    dcc.Graph(id="environment-satisfaction")
                ], width=6),
                
                dbc.Col([
                    html.H4("Relationship Satisfaction", className="mt-4 mb-2"),
                    dcc.Graph(id="relationship-satisfaction")
                ], width=6)
            ])
        ]),
        
        # Performance Tab
        dbc.Tab(label="Performance", children=[
            dbc.Row([
                dbc.Col([
                    html.H3("Performance Analysis", className="mt-3 mb-3"),
                    html.P("Analyze factors affecting employee performance ratings.")
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("Performance Rating Distribution", className="mt-3 mb-2"),
                    dcc.Graph(id="performance-rating-dist")
                ], width=6),
                
                dbc.Col([
                    html.H4("Performance vs. Monthly Income", className="mt-3 mb-2"),
                    dcc.Graph(id="performance-income")
                ], width=6)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("Performance vs. Job Involvement", className="mt-4 mb-2"),
                    dcc.Graph(id="performance-job-involvement")
                ], width=6),
                
                dbc.Col([
                    html.H4("Performance vs. Training", className="mt-4 mb-2"),
                    dcc.Graph(id="performance-training")
                ], width=6)
            ])
        ]),
        
        # 3D Visualization Tab
        dbc.Tab(label="3D Visualization", children=[
            dbc.Row([
                dbc.Col([
                    html.H3("3D Data Visualization", className="mt-3 mb-3"),
                    html.P("Explore the relationships between multiple variables in 3D space.")
                ], width=12)
            ]),
            
            dbc.Row([
                dbc.Col([
                    html.H4("3D PCA Visualization", className="mt-3 mb-2"),
                    html.P("Principal Component Analysis (PCA) reduces the dimensionality of the data while preserving its variation."),
                    dcc.Graph(id="pca-3d-visualization", style={"height": "700px"})
                ], width=12)
            ])
        ])
    ])
], fluid=True)

# Callback for dataset summary
@app.callback(
    Output("dataset-summary", "children"),
    Input("dataset-summary", "id")
)
def update_dataset_summary(id):
    attrition_count = df['Attrition'].value_counts()
    attrition_pct = round(attrition_count / len(df) * 100, 1)
    
    return [
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Total Employees", className="card-title"),
                        html.H2(f"{len(df)}", className="card-text text-primary")
                    ])
                ])
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Attrition Rate", className="card-title"),
                        html.H2(f"{attrition_pct['Yes']}%", className="card-text text-danger")
                    ])
                ])
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Avg. Job Satisfaction", className="card-title"),
                        html.H2(f"{df['JobSatisfaction'].mean():.1f}/4", className="card-text text-success")
                    ])
                ])
            ], width=3),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H5("Avg. Performance Rating", className="card-title"),
                        html.H2(f"{df['PerformanceRating'].mean():.1f}/4", className="card-text text-info")
                    ])
                ])
            ], width=3)
        ])
    ]

# Callback for attrition by department
@app.callback(
    Output("attrition-by-department", "figure"),
    Input("attrition-by-department", "id")
)
def update_attrition_by_department(id):
    dept_attrition = df.groupby(['Department', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(dept_attrition, x='Department', y='Count', color='Attrition',
                 barmode='group', title='Attrition by Department',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'})
    return fig

# Callback for attrition by job role
@app.callback(
    Output("attrition-by-jobrole", "figure"),
    Input("attrition-by-jobrole", "id")
)
def update_attrition_by_jobrole(id):
    role_attrition = df.groupby(['JobRole', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(role_attrition, x='JobRole', y='Count', color='Attrition',
                 barmode='group', title='Attrition by Job Role',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'})
    fig.update_layout(xaxis={'categoryorder':'total descending'})
    return fig

# Callback for age distribution
@app.callback(
    Output("age-distribution", "figure"),
    Input("age-distribution", "id")
)
def update_age_distribution(id):
    fig = px.histogram(df, x='Age', color='Attrition', marginal='box',
                      title='Age Distribution by Attrition',
                      color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'})
    return fig

# Callback for gender distribution
@app.callback(
    Output("gender-distribution", "figure"),
    Input("gender-distribution", "id")
)
def update_gender_distribution(id):
    gender_attrition = df.groupby(['Gender', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(gender_attrition, x='Gender', y='Count', color='Attrition',
                 barmode='group', title='Attrition by Gender',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'})
    return fig

# Callback for education field
@app.callback(
    Output("education-field", "figure"),
    Input("education-field", "id")
)
def update_education_field(id):
    edu_attrition = df.groupby(['EducationField', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(edu_attrition, x='EducationField', y='Count', color='Attrition',
                 barmode='group', title='Attrition by Education Field',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'})
    return fig

# Callback for marital status
@app.callback(
    Output("marital-status", "figure"),
    Input("marital-status", "id")
)
def update_marital_status(id):
    marital_attrition = df.groupby(['MaritalStatus', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(marital_attrition, x='MaritalStatus', y='Count', color='Attrition',
                 barmode='group', title='Attrition by Marital Status',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'})
    return fig

# Callback for job satisfaction vs attrition
@app.callback(
    Output("job-satisfaction-attrition", "figure"),
    Input("job-satisfaction-attrition", "id")
)
def update_job_satisfaction_attrition(id):
    job_sat_attrition = df.groupby(['JobSatisfaction', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(job_sat_attrition, x='JobSatisfaction', y='Count', color='Attrition',
                 barmode='group', title='Job Satisfaction vs. Attrition',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'},
                 labels={'JobSatisfaction': 'Job Satisfaction (1-4 scale)'})
    return fig

# Callback for work-life balance vs attrition
@app.callback(
    Output("worklife-balance-attrition", "figure"),
    Input("worklife-balance-attrition", "id")
)
def update_worklife_balance_attrition(id):
    wlb_attrition = df.groupby(['WorkLifeBalance', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(wlb_attrition, x='WorkLifeBalance', y='Count', color='Attrition',
                 barmode='group', title='Work-Life Balance vs. Attrition',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'},
                 labels={'WorkLifeBalance': 'Work-Life Balance (1-4 scale)'})
    return fig

# Callback for environment satisfaction
@app.callback(
    Output("environment-satisfaction", "figure"),
    Input("environment-satisfaction", "id")
)
def update_environment_satisfaction(id):
    env_sat_attrition = df.groupby(['EnvironmentSatisfaction', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(env_sat_attrition, x='EnvironmentSatisfaction', y='Count', color='Attrition',
                 barmode='group', title='Environment Satisfaction vs. Attrition',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'},
                 labels={'EnvironmentSatisfaction': 'Environment Satisfaction (1-4 scale)'})
    return fig

# Callback for relationship satisfaction
@app.callback(
    Output("relationship-satisfaction", "figure"),
    Input("relationship-satisfaction", "id")
)
def update_relationship_satisfaction(id):
    rel_sat_attrition = df.groupby(['RelationshipSatisfaction', 'Attrition']).size().reset_index(name='Count')
    fig = px.bar(rel_sat_attrition, x='RelationshipSatisfaction', y='Count', color='Attrition',
                 barmode='group', title='Relationship Satisfaction vs. Attrition',
                 color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'},
                 labels={'RelationshipSatisfaction': 'Relationship Satisfaction (1-4 scale)'})
    return fig

# Callback for performance rating distribution
@app.callback(
    Output("performance-rating-dist", "figure"),
    Input("performance-rating-dist", "id")
)
def update_performance_rating_dist(id):
    perf_count = df['PerformanceRating'].value_counts().reset_index()
    perf_count.columns = ['PerformanceRating', 'Count']
    fig = px.bar(perf_count, x='PerformanceRating', y='Count',
                 title='Performance Rating Distribution',
                 color='PerformanceRating',
                 labels={'PerformanceRating': 'Performance Rating (1-4 scale)'})
    return fig

# Callback for performance vs income
@app.callback(
    Output("performance-income", "figure"),
    Input("performance-income", "id")
)
def update_performance_income(id):
    fig = px.box(df, x='PerformanceRating', y='MonthlyIncome',
                 title='Performance Rating vs. Monthly Income',
                 color='PerformanceRating',
                 labels={'PerformanceRating': 'Performance Rating (1-4 scale)'})
    return fig

# Callback for performance vs job involvement
@app.callback(
    Output("performance-job-involvement", "figure"),
    Input("performance-job-involvement", "id")
)
def update_performance_job_involvement(id):
    perf_job_inv = df.groupby(['PerformanceRating', 'JobInvolvement']).size().reset_index(name='Count')
    fig = px.bar(perf_job_inv, x='PerformanceRating', y='Count', color='JobInvolvement',
                 barmode='group', title='Performance Rating vs. Job Involvement',
                 labels={'PerformanceRating': 'Performance Rating (1-4 scale)',
                         'JobInvolvement': 'Job Involvement (1-4 scale)'})
    return fig

# Callback for performance vs training
@app.callback(
    Output("performance-training", "figure"),
    Input("performance-training", "id")
)
def update_performance_training(id):
    perf_training = df.groupby(['PerformanceRating', 'TrainingTimesLastYear']).size().reset_index(name='Count')
    fig = px.bar(perf_training, x='PerformanceRating', y='Count', color='TrainingTimesLastYear',
                 barmode='group', title='Performance Rating vs. Training Times Last Year',
                 labels={'PerformanceRating': 'Performance Rating (1-4 scale)'})
    return fig

# Callback for 3D PCA visualization
@app.callback(
    Output("pca-3d-visualization", "figure"),
    Input("pca-3d-visualization", "id")
)
def update_pca_3d_visualization(id):
    # Select numerical columns for PCA
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    numerical_cols = [col for col in numerical_cols if col not in ['EmployeeCount', 'StandardHours', 'EmployeeNumber', 'AttritionBinary']]
    
    # Standardize the data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[numerical_cols])
    
    # Apply PCA
    pca = PCA(n_components=3)
    pca_result = pca.fit_transform(scaled_data)
    
    # Create a DataFrame with PCA results
    pca_df = pd.DataFrame(data=pca_result, columns=['PC1', 'PC2', 'PC3'])
    pca_df['Attrition'] = df['Attrition']
    pca_df['Department'] = df['Department']
    pca_df['JobRole'] = df['JobRole']
    
    # Create 3D scatter plot
    fig = px.scatter_3d(
        pca_df, x='PC1', y='PC2', z='PC3',
        color='Attrition',
        symbol='Department',
        hover_data=['JobRole'],
        title='3D PCA Visualization of Employee Data',
        color_discrete_map={'Yes': '#FF4136', 'No': '#0074D9'}
    )
    
    # Update layout for better visualization
    fig.update_layout(
        scene=dict(
            xaxis_title='Principal Component 1',
            yaxis_title='Principal Component 2',
            zaxis_title='Principal Component 3'
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=8060)
