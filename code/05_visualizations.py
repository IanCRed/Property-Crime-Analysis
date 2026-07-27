import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt

Crime = pd.read_excel("CrimeData1.xlsx")
print(Crime)

avg_propcrime = Crime.groupby("Year")["Property Crime Rate"].mean()

# Line Chart
plt.plot(avg_propcrime)
plt.title("Property Crime Rate Trend")
plt.xlabel("Year")
plt.ylabel("Property Crime Rate")
for year, rate in list(avg_propcrime.items())[::2]:
    plt.annotate(f'{rate:.1f}', xy=(year, rate), xytext=(0,7), textcoords="offset points", ha="center", va="bottom", fontsize=9)
plt.gca().set_ylim(top=avg_propcrime.max() * 1.1)
plt.show()


#Barchart 
avg_propcrime = Crime.groupby("Year")["Property Crime Rate"].mean()
x = avg_propcrime.index
y = avg_propcrime.values
plt.bar(x, y, color = "skyblue", edgecolor = "black")
plt.title("Property Crime Rate by Year")
plt.xlabel("Year")
plt.ylabel("Property Crime Rate")
plt.show()




# Plotting dots  

x = Crime["Gini"]
y = Crime["Property Crime Rate"]
plt.plot(x, y, "o")
plt.title("Property Crime Rate vs Gini")
plt.xlabel("Gini")
plt.ylabel("Property Crime Rate per 100k")
plt.show()

# Scatterplots 
x = Crime["Unemp_Rate"]
y = Crime["Property Crime Rate"]
plt.scatter(x, y, color = "red", edgecolor="black", alpha=0.7)
plt.title("Unemployment Rate vs Property Crime")
plt.xlabel("Unemployment Rate %")
plt.ylabel("Property Crime Rate per 100k")
plt.show()





import seaborn as sns 

sns.pairplot(Crime[["Property Crime Rate", "Gini", "Unemp_Rate"]])
plt.show()


#Histogram 

Crimecols = ["Property Crime Rate", "Gini", "Pov_Rate", "Med_Income", "Unemp_Rate", "Pct_SP_HH", "Pct_NonWhite", "Pop_Density", "Young_Male"]

Crime[Crimecols].hist(figsize=(14,10), bins=20)
plt.tight_layout()
plt.show()

# Histogram for Property Crime 
Crime["Property Crime Rate"].hist(figsize=(14,10), bins=20)
plt.title("Property Crime Histogram")
plt.xlabel("Property Crime Rate")
plt.ylabel("Count")
plt.show()


#Boxplot 
Crimecols2 = ["Property Crime Rate" , "Gini"]
sns.boxplot(data=Crime["Gini"])
plt.show()



# Correlation Heatmap 
Crime2 = Crime[["Property Crime Rate", "Gini", "Pov_Rate", "Med_Income", "Unemp_Rate", "Pct_SP_HH", "Pct_NonWhite", "Pop_Density", "Young_Male"]]
custom_cmap = sns.diverging_palette(10,10, sep=1, as_cmap=True)
sns.heatmap(Crime2.corr(numeric_only=True), annot=True, cmap=custom_cmap, vmin=-1,vmax=1)
plt.title("Correlation Heatmap")
plt.show()



#Interactive Plotly scatter 
import plotly.express as px
fig = px.scatter(Crime, x="Gini", y="Property Crime Rate", color= "Year", hover_name="State", trendline ="ols")
fig.show()



# Coefficient plot?
coef = FEmodel.params
err = 1.96 * FEmodel.std_errors

plt.figure(figsize=(8,6))
plt.errorbar(
    coef,
    coef.index,
    xerr=err,
    fmt="o"
)

plt.axvline(0,color="red")
plt.title("Fixed Effects Coefficients")
plt.tight_layout()
plt.show()
