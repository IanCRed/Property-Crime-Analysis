import pandas as pd 
Crime1 = pd.read_excel("CrimeData1.xlsx")

print(Crime1.groupby(["Year"]).agg({"Property Crime Rate": "mean", "Gini": "mean", "Unemp_Rate": "mean"}))

print(Crime1.groupby(["State"])["Property Crime Rate"].mean().sort_values(ascending = False))

print(Crime1.describe()[["Property Crime Rate", "Gini", "Unemp_Rate"]])

Crime1.info()

import numpy as np 

print(Crime1[["Property Crime Rate", "Gini", "Pov_Rate", "Med_Income", "Unemp_Rate", "Pct_SP_HH", "Pct_NonWhite", "Pop_Density", "Young_Male"]].corr())

Crime2 = Crime1[["Property Crime Rate", "Gini", "Pov_Rate", "Med_Income", "Unemp_Rate", "Pct_SP_HH", "Pct_NonWhite", "Pop_Density", "Young_Male"]]

Crimecorr = Crime2.corr().round(2)
print(Crimecorr.to_string())
Crimecorr.to_excel("CrimeCorrelation.xlsx")