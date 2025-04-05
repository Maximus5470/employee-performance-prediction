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
1. Clone the repository:
    ```sh
    git clonehttps://github.com/Rohithgg/employee-performance-prediction
    cd employee-performance-prediction
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Ensure the dataset `WA_Fn-UseC_-HR-Employee-Attrition.csv` is in the project directory.

2. Run the Dash app:
    ```sh
    python employee_dashboard.py
    ```

3. Open your web browser and go to http://127.0.0.1:8060 to view the dashboard.
4. you can also run the Jupyter Notebook `Employee_Attrition_and_Performance_Analysis.ipynb` for detailed analysis and visualizations.
5. for more vistualizations you can check the Tableau link [here](https://public.tableau.com/app/profile/gautham.sharma/viz/EmployeeAttritionProject_17437562521440/ExployeePerformance?publish=yes) and web page [over here](https://rohithgg.github.io/employee-performance-prediction/).

## Visualizations
The project includes various visualizations:


Animated Attrition Distribution - Shows attrition distribution with animation by department
Interactive 3D Scatter Plot - Visualizes employee attributes in 3D space
Animated Bar Chart - Displays attrition distribution across departments over time
Rotating 3D Scatter Plot - Shows the relationship between age, income, years at company, and attrition
Feature Importance Charts - Highlights the most influential factors for attrition and performance
Department and Role Analysis - Interactive charts showing attrition risk by department and job role

Note that the interactive visualizations require a web browser to view.
Tableau visualizations are also included for further analysis [here](https://public.tableau.com/app/profile/gautham.sharma/viz/EmployeeAttritionProject_17437562521440/ExployeePerformance?publish=yes).
You can check this website too [over here](https://rohithgg.github.io/employee-performance-prediction/)
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

## Demo
this is the demo of the project and how the visualizations are presented in the dashboard.
![Demo](2025-04-05 16-20-03.mp4)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributors

- Rohith Gona
- Gautham Sharma
