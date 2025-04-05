# Employee Performance & Attrition Dashboard

This dashboard provides an interactive interface for exploring the employee attrition and performance analysis from the original Jupyter notebook. It integrates all visualizations and outputs into a cohesive, user-friendly dashboard using the Dash framework.

## Features

- **Interactive Visualizations**: All charts and graphs from the original notebook are now interactive
- **Organized by Topics**: Content is organized into tabs for easy navigation
- **Detailed Documentation**: Each section includes explanatory text about what the visualizations show
- **Responsive Design**: Works on different screen sizes
- **3D Visualization**: Includes the 3D PCA visualization for exploring multivariate relationships

## Dashboard Sections

1. **Overview**: Summary statistics and key metrics about employee attrition
2. **Demographics**: Analysis of how demographic factors relate to attrition
3. **Job Satisfaction**: Exploration of satisfaction metrics and their impact on attrition
4. **Performance**: Analysis of performance ratings and related factors
5. **3D Visualization**: Interactive 3D visualization of employee data using PCA

## Installation

1. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

2. Run the dashboard:
   ```
   python employee_dashboard.py
   ```
   
   Or open and run the Jupyter notebook:
   ```
   jupyter notebook employee_dashboard_notebook.ipynb
   ```

3. Open your browser and navigate to:
   - For Python script: http://127.0.0.1:8050/
   - For Jupyter notebook: The dashboard will display in the notebook output

## Data Story

This dashboard tells the story of employee attrition and performance at a company:

1. **Understanding Attrition Patterns**: The Overview and Demographics tabs help identify which departments, job roles, and demographic groups experience the highest attrition rates.

2. **Satisfaction Impact**: The Job Satisfaction tab explores how various satisfaction metrics (job, environment, relationship, work-life balance) correlate with employee retention.

3. **Performance Analysis**: The Performance tab examines the distribution of performance ratings and how they relate to factors like income, job involvement, and training.

4. **Multivariate Relationships**: The 3D visualization provides a holistic view of how multiple factors interact to influence attrition.

By exploring these sections, users can gain insights into the key factors driving employee attrition and performance, helping to inform HR strategies and interventions.