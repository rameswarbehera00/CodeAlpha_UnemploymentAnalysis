import os
import pandas as pd

# 1. Path to data
data_path = os.path.join("data", "Unemployment in India.csv")

# 2. Load the CSV
df = pd.read_csv(data_path)

print("--- RAW SHAPE ---")
print(f"Total rows: {df.shape[0]}, Total columns: {df.shape[1]}")

# 3. Strip whitespace from column names
# .str.strip() removes leading and trailing spaces from each column title
df.columns = df.columns.str.strip()
print("\nCleaned Column Names:")
print(df.columns.tolist())

# 4. Drop completely empty rows
# how='all' ensures we only drop rows where EVERY column is null (the 28 blank rows)
df = df.dropna(how="all")
print(f"\nShape after dropping empty rows: {df.shape}")

# 5. Clean string whitespace inside values
df["Frequency"] = df["Frequency"].str.strip()
df["Area"] = df["Area"].str.strip()
df["Region"] = df["Region"].str.strip()

# 6. Convert 'Date' to proper datetime format
# dayfirst=True ensures '31-05-2019' is parsed as 31st May 2019, not an error
df["Date"] = pd.to_datetime(df["Date"].str.strip(), dayfirst=True)

# 7. Extract Month and Year for easier trend grouping
df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month_name()

# 8. Inspect the cleaned dataset
print("\n--- CLEANED DATA INFO ---")
print(df.info())

print("\n--- FIRST 5 CLEANED ROWS ---")
print(df.head())

# 9. Save cleaned dataset for visualization steps
output_dir = "data"
clean_path = os.path.join(output_dir, "Cleaned_Unemployment_India.csv")
df.to_csv(clean_path, index=False)
print(f"\nCleaned dataset saved to: {clean_path}")