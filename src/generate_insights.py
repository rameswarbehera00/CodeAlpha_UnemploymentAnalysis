import os
import pandas as pd

# Load cleaned dataset
clean_path = os.path.join("data", "Cleaned_Unemployment_India.csv")
df = pd.read_csv(clean_path)
df["Date"] = pd.to_datetime(df["Date"])

# Partition periods
pre_covid = df[df["Date"] < pd.to_datetime("2020-04-01")]
post_covid = df[df["Date"] >= pd.to_datetime("2020-04-01")]

# 1. Macro Trends
pre_mean = pre_covid["Estimated Unemployment Rate (%)"].mean()
post_mean = post_covid["Estimated Unemployment Rate (%)"].mean()

# 2. Area breakdown post-covid
area_breakdown = post_covid.groupby("Area")["Estimated Unemployment Rate (%)"].mean()

# 3. Top 5 hardest-hit regions during lockdown
top_impacted = (
    post_covid.groupby("Region")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

print("=" * 60)
print("           UNEMPLOYMENT ANALYSIS SUMMARY REPORT             ")
print("=" * 60)
print(f"Pre-Lockdown Average Rate (May 2019 - Mar 2020): {pre_mean:.2f}%")
print(f"Lockdown Average Rate (Apr 2020 - Jun 2020)     : {post_mean:.2f}%")
print(f"Absolute Increase                                : +{post_mean - pre_mean:.2f}%")
print(f"Percentage Jump                                  : +{((post_mean - pre_mean) / pre_mean) * 100:.2f}%")
print("-" * 60)
print("AREA IMPACT (Apr - Jun 2020):")
print(f"  • Urban Average : {area_breakdown.get('Urban', 0):.2f}%")
print(f"  • Rural Average : {area_breakdown.get('Rural', 0):.2f}%")
print("-" * 60)
print("TOP 5 MOST AFFECTED STATES/UTs (Apr - Jun 2020):")
for rank, (region, rate) in enumerate(top_impacted.items(), 1):
    print(f"  {rank}. {region:<16}: {rate:.2f}%")
print("=" * 60)