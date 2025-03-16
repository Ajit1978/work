import pandas as pd

# Load the mmData.csv file
df_mm = pd.read_csv("mmData.csv")

df_main = pd.DataFrame({
    "Stone Shape": ["RD", "Cushion", "MARQUISE", "OVAL", "MARQUISE"],
    "Stone Qlty": ["E VS2", "E VS2", "E VS2", "E VS2", "E VS2"],
    "Sieve / MM": [2.7, 3.50, 5.20, 3.80, 6.20]
})

# Merge based on "Stone Shape" and "Sieve / MM"
merged_df = df_main.merge(df_mm, left_on=["Stone Shape", "Sieve / MM"], right_on=["Stone Shape", "Sieve /  MM"], how="left")

# Drop duplicate column if exists
merged_df.drop(columns=["Sieve /  MM"], inplace=True)

# Save to CSV
output_file = "merged_output.csv"
merged_df.to_csv(output_file, index=False)

print(f"Merged data saved to {output_file}")