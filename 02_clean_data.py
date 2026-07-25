import pandas as pd 
Crime_Clean = pd.read_excel("CrimeProject1_Data.xlsx")
print(Crime_Clean.tail())
Crime_Clean = Crime_Clean.drop(663)
print(Crime_Clean.tail())
Crime_Clean.rename(columns={"Gini ": "Gini"}, inplace=True)

Crime_Clean.to_excel("CrimeData1.xlsx", index=False)

print(Crime_Clean.dtypes)