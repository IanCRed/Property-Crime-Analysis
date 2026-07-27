# Property-Crime-Analysis
An statistical analysis of the effect of income inequality and labor market conditions on property crime in the United States 

## Data Pipeline and Methodology 
* [01_download_data.py](01_download_data.py) : Loads in the Excel dataset. 
* [02_clean_data.py](02_clean_data.py) : Handles data formatting and missing values.
* [03_exploratory_analysis.py](03_exploratory_analysis.py) : Conducts initial statistical distributions.
* [04_regression.py](04_regression.py) : Executes the core statistical regression modeling.
* [05_visualizations.py](05_visualizations.py): Generates the visuals shown below. 

## Visualizations 

### Interactive Dashboard 
Explore the interactive property crime vs income inequality dashboard here: 

**https://iancred.github.io/Property-Crime-Analysis/property_crime_II_dashboard.html** 


### Correlation Matrix 
Checking for strong correlation and multicollinearity. 
![Correlation Heatmap](<Correlation Heatmap.png>) 

### Variable Distributions 
Quick look at the shape of all variables.
![Histogram](<Histogram of all vars.png>) 

### BarChart 
Property Crime Rate Trend (2020/2021 ommited due to Covid Pandemic and FBI Data inconsistencies) 
![Bar Chart](<Prop Crime Bar Chart.png>)

### Scatterplots 
Analysis of relationships between key variables 

![Income Inequality](<Prop Crime vs Gini Scatterplot.png>) 

![Unemployment Rate](<Unemployment Rate vs Property Crime Scatterplot.png>) 

![Key Variables Comparison](<Pairplot Prop Crime GINI Unemp.png>) 


## Regression Models 

## Power BI Dashboard 
(coming soon) 
