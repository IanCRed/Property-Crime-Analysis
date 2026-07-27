# Property-Crime-Analysis
A statistical analysis of the effect of income inequality and labor market conditions on property crime in the United States 

## Data Pipeline and Methodology 
* [01_download_data.py](code/01_download_data.py) : Loads in the Excel dataset. 
* [02_clean_data.py](code/02_clean_data.py) : Handles data formatting and missing values.
* [03_exploratory_analysis.py](code/03_exploratory_analysis.py) : Conducts initial statistical distributions.
* [04_regression.py](code/04_regression.py) : Executes the core statistical regression modeling.
* [05_visualizations.py](code/05_visualizations.py): Generates the visuals shown below. 

## Visualizations 

### Interactive Dashboard 
Explore the interactive property crime vs income inequality dashboard here: 

[Interactive State Dashboard](https://iancred.github.io/Property-Crime-Analysis/property_crime_II_dashboard.html) 

### Property Crime U.S MAP
Geographic map illustrating property crime rate levels by state: 

[Choropleth Property Crime Map](https://iancred.github.io/Property-Crime-Analysis/output/Choropleth_map_PropCrime.html)

### Correlation Matrix 
Checking for strong correlation and multicollinearity. 
![Correlation Heatmap](<output/Correlation Heatmap.png>) 

### Variable Distributions 
Quick look at the shape of all variables.
![Histogram](<output/Histogram of all vars.png>) 

### BarChart 
Property Crime Rate Trend (2020/2021 ommited due to Covid Pandemic and FBI Data inconsistencies) 
![Bar Chart](<output/Prop Crime Bar Chart.png>)

### Scatterplots 
Analysis of relationships between key variables 

![Income Inequality](<output/Prop Crime vs Gini Scatterplot.png>) 

![Unemployment Rate](<output/Unemployment Rate vs Property Crime Scatterplot.png>) 

![Key Variables Comparison](<output/Pairplot Prop Crime GINI Unemp.png>) 


## Regression Models 

### Simple Linear Regression 
![Simple Linear Model Results](<regoutput/Simple OLS Results.png>)

### Multiple Linear Regression 
![Multiple Linear Model Results](<regoutput/MLR Results.png>)

### Fixed Effects Regression 
![Fixed Effects Model Results](<regoutput/FE Model Results improved code.png>)


## Power BI Dashboard 
(coming soon) 
