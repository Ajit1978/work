import pandas as pd

# Load the CSV files
format_df = pd.read_csv("format.csv")
mmdata_df = pd.read_csv("mmData.csv")

# Perform a VLOOKUP-like operation by merging data based on "Sieve / MM"
format_df = format_df.merge(mmdata_df[["Sieve /  MM", "AVG WT"]], 
                            left_on="Sieve /  MM", 
                            right_on="Sieve /  MM", 
                            how="left")

# Update the "Stone Size" column with the matched "AVG WT" values
format_df["Stone Size"] = format_df["AVG WT"]

# Drop the extra "AVG WT" column if necessary
format_df.drop(columns=["AVG WT"], inplace=True)

# Save the updated data to a new Excel file
format_df.to_excel("merged_data.xlsx", index=False)
