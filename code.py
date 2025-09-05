import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

smokers = pd.read_csv("smokers.csv")
fatalities = pd.read_csv("fatalities.csv")

df = pd.merge(smokers, fatalities, on=["Year", "Sex"], how="inner")

df = df.rename(columns={
    "16 and Over": "Tobacco_Use",
    "Value": "Mortality_Rate"
})

df = df[["Year", "Sex", "Tobacco_Use", "Mortality_Rate"]]

print("\nMerged Data Sample:")
print(df.head())

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="Year", y="Tobacco_Use", hue="Sex", ci=None)
plt.title("Tobacco Use Trend by Sex (2004–2015)")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="Year", y="Mortality_Rate", hue="Sex", ci=None)
plt.title("Mortality Trend by Sex (2004–2015)")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x="Tobacco_Use", y="Mortality_Rate", hue="Sex", style="Year", palette="viridis")
plt.title("Tobacco Use vs Mortality Rate by Sex")
plt.show()

print("\nCorrelation between Tobacco Use and Mortality Rate:")
print(df.groupby("Sex")[["Tobacco_Use", "Mortality_Rate"]].corr().unstack().iloc[:,1])

