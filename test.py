import pandas as pd

# Read the CSV files
bill_df = pd.read_csv('bill.csv')
rr_df = pd.read_csv('rr.csv')
ll_df = pd.read_csv('ll.csv')

# Create mapping dictionaries
rr_sieve_to_weight = {str(row['Avg MM']).strip(): row['AVG WT'] for _, row in rr_df.iterrows()}
ll_rate_map = dict(zip(ll_df['MM Size'].astype(str), ll_df['ALTR USA Cost/ct']))

# Function to map Sieve/MM to Stone Size
def map_stone_size(sieve_mm):
    sieve_str = str(sieve_mm).strip()
    return rr_sieve_to_weight.get(sieve_str, '')

# Function to map MM Size to Stone Rate
def map_stone_rate(sieve_mm):
    mm_str = str(sieve_mm).strip()
    return ll_rate_map.get(mm_str, '')

# Find the correct column names
sieve_column = [col for col in bill_df.columns if 'Sieve' in col][0]
stone_size_column = [col for col in bill_df.columns if 'Stone Size' in col][0]
stone_rate_column = [col for col in bill_df.columns if 'Stone Rate' in col][0]

# Apply mappings
bill_df[stone_size_column] = bill_df[sieve_column].apply(map_stone_size)
bill_df[stone_rate_column] = bill_df[sieve_column].apply(map_stone_rate)

# Save the updated dataframe
bill_df.to_csv('updated_bill.csv', index=False)

print("CSV file updated successfully. Check 'updated_bill.csv'.")

# Optional: Print unmatched values
unmatched_size = bill_df[bill_df[stone_size_column] == ''][sieve_column].unique()
unmatched_rate = bill_df[bill_df[stone_rate_column] == ''][sieve_column].unique()
print("Unmatched Sieve/MM (Size):", unmatched_size)
print("Unmatched Sieve/MM (Rate):", unmatched_rate)