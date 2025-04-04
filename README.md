# Employee Attrition and Performance Analysis

## Project Overview

This project provides advanced visualization and prediction capabilities for employee attrition and performance data. It analyzes factors affecting employee attrition and performance ratings using machine learning models and presents insights through interactive visualizations.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Visualizations](#visualizations)
- [Prediction Functionality](#prediction-functionality)
- [Sample Results](#sample-results)
- [License](#license)

## Features

- Predictive modeling for employee attrition risk
- Performance rating prediction
- Interactive 3D visualizations
- Animated data representations
- Feature importance analysis
- Department and job role-specific insights

## Technologies Used

- Python 3.x
- pandas - Data manipulation and analysis
- scikit-learn - Machine learning algorithms
- Plotly - Interactive visualizations
- Bokeh - Interactive plots
- Matplotlib & Seaborn - Statistical visualizations
- IPython - Enhanced interactive computing
- Tableau - For data visualization in Tableau

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/yourusername/employee-attrition-analysis.git
cd employee-attrition-analysis
pip install pandas numpy scikit-learn plotly bokeh matplotlib seaborn ipython
```
## Usage
Place your employee data in a CSV file named WA_Fn-UseC_-HR-Employee-Attrition.csv
Run the Jupyter notebook:
```bash
jupyter notebook employee-preformance-prediction.ipynb
```
## Visualizations
The project includes various visualizations:


Animated Attrition Distribution - Shows attrition distribution with animation by department
Interactive 3D Scatter Plot - Visualizes employee attributes in 3D space
Animated Bar Chart - Displays attrition distribution across departments over time
Rotating 3D Scatter Plot - Shows the relationship between age, income, years at company, and attrition
Feature Importance Charts - Highlights the most influential factors for attrition and performance
Department and Role Analysis - Interactive charts showing attrition risk by department and job role

Note that the interactive visualizations require a web browser to view.
Tableau visualizations are also included for further analysis [here](https://public.tableau.com/app/profile/gautham.sharma/viz/EmployeeAttritionProject_17437562521440/ExployeePerformance?publish=yes) .
## Prediction Functionality
The system can predict:

Attrition risk probability for employees
Binary attrition outcome (Yes/No)
Performance ratings
The predict_employee_outcomes() function takes employee data and returns predictions.

## Sample Results
The project generates several output files:

best_reg_model_feature_importance.png - Feature importance visualization
attrition_vs_satisfaction.png - Relationship between attrition and job satisfaction
3d_attrition_analysis.html - Interactive 3D analysis
performance_vs_satisfaction.html - Interactive performance vs. satisfaction plot
dept_attrition_risk.html - Department-wise attrition risk
role_attrition_risk.html - Role-wise attrition risk

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributors

- Rohith Gona
- Gautham Sharma