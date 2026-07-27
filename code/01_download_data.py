import pandas as pd 
Crime = pd.read_excel("EC 490 Project Dataset State obs.xlsx", usecols="A:V")
print(Crime.tail())
Crime.to_excel("CrimeProject1_Data.xlsx", index=False)
