import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Set clean aesthetic style
sns.set_theme(style="whitegrid")
os.makedirs("outputs", exist_ok=True)

# 1. Load cleaned data
clean_path = os.path.join("data", "Cleaned_Unemployment_India.csv")
df = pd.read_csv(clean_path)
df["Date"] = pd.to_datetime(df["Date"])

# -------------------------------------------------------------
# Chart 1: Time Series Trend (Impact of COVID-19 Lockdown)
# -------------------------------------------------------------
plt.figure(figsize=(12, 6))
sns.lineplot(
    data=df,
    x="Date",
    y="Estimated Unemployment Rate (%)",
    hue="Area",
    marker="o",
    ci=None
)
plt.axvline(
    pd.to_datetime("2020-03-24"),
    color="red",
    linestyle="--",
    linewidth=2,
    label="Lockdown Imposed (24 Mar 2020)"
)
plt.title("Impact of COVID-19 on Unemployment Rate in India (Rural vs Urban)", fontsize=14, fontweight="bold")
plt.xlabel("Timeline", fontsize=12)
plt.ylabel("Unemployment Rate (%)", fontsize=12)
plt.legend(title="Area / Event")
plt.tight_layout()
plt.savefig(os.path.join("outputs", "1_unemployment_timeline.png"), dpi=300)
plt.close()
print("Saved: outputs/1_unemployment_timeline.png")

# -------------------------------------------------------------
# Chart 2: Pre-COVID vs Post-COVID Comparison (Boxplot)
# -------------------------------------------------------------
df["Period"] = df["Date"].apply(lambda d: "Lockdown (Apr-Jun 2020)" if d >= pd.to_datetime("2020-04-01") else "Pre-Lockdown (May 2019-Mar 2020)")

plt.figure(figsize=(8, 6))
sns.boxplot(
    data=df,
    x="Period",
    y="Estimated Unemployment Rate (%)",
    palette="Set2"
)
plt.title("Distribution Shift: Pre vs Lockdown Unemployment Rate", fontsize=13, fontweight="bold")
plt.xlabel("Economic Period", fontsize=11)
plt.ylabel("Unemployment Rate (%)", fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join("outputs", "2_pre_vs_post_lockdown_distribution.png"), dpi=300)
plt.close()
print("Saved: outputs/2_pre_vs_post_lockdown_distribution.png")

# -------------------------------------------------------------
# Chart 3: Top 10 Most Affected States During Lockdown
# -------------------------------------------------------------
lockdown_df = df[df["Date"] >= pd.to_datetime("2020-04-01")]
top_states = (
    lockdown_df.groupby("Region")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=top_states,
    y="Region",
    x="Estimated Unemployment Rate (%)",
    palette="Reds_r"
)
plt.title("Top 10 States by Highest Average Unemployment (Apr-Jun 2020)", fontsize=13, fontweight="bold")
plt.xlabel("Average Unemployment Rate (%)", fontsize=11)
plt.ylabel("State / Region", fontsize=11)
plt.tight_layout()
plt.savefig(os.path.join("outputs", "3_top10_affected_states.png"), dpi=300)
plt.close()
print("Saved: outputs/3_top10_affected_states.png")

# -------------------------------------------------------------
# Chart 4: Correlation Heatmap
# -------------------------------------------------------------
plt.figure(figsize=(8, 6))
numeric_cols = [
    "Estimated Unemployment Rate (%)",
    "Estimated Employed",
    "Estimated Labour Participation Rate (%)"
]
corr_matrix = df[numeric_cols].corr()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation: Unemployment vs Employment vs Labour Participation", fontsize=12, fontweight="bold")
plt.tight_layout()
plt.savefig(os.path.join("outputs", "4_correlation_heatmap.png"), dpi=300)
plt.close()
print("Saved: outputs/4_correlation_heatmap.png")