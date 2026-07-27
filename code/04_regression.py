import pandas as pd 
import numpy as np 
import statsmodels.api as sm

Crime = pd.read_excel("CrimeData1.xlsx")
print(Crime)


y = Crime["Property Crime Rate"] 
x= Crime["Gini"] 
x = sm.add_constant(x) 

model = sm.OLS(y, x).fit()

print(model.summary())

y = Crime["Property Crime Rate"]
x = Crime[["Gini", "Pov_Rate", "Med_Income", "Unemp_Rate", "Pct_SP_HH", "Pct_NonWhite", "Pop_Density", "Young_Male", "W", "NE", "S", "MW"]]
x = sm.add_constant(x) 

modelMLR = sm.OLS(y, x).fit()
print(modelMLR.summary())

# Fixed Effects Model 

from linearmodels.panel import PanelOLS 

Crime = Crime.set_index(["State", "Year"])

FEmodel = PanelOLS.from_formula("Q('Property Crime Rate') ~ 1 + Gini + Q('Pov_Rate') + Q('Unemp_Rate') + Q('Pct_NonWhite') + Q('Pop_Density') + Q('Young_Male') + EntityEffects + TimeEffects", data=Crime).fit(cov_type="clustered", cluster_entity=True)

print(FEmodel.summary)
