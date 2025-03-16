import pandas as pd
import numpy as np
import re

# Read the main CSV file - using a more robust approach
try:
    main_df = pd.read_csv('format.csv', skip_blank_lines=False)
except Exception as e:
    print(f"Error reading main file: {e}")
    print("Trying alternative parsing method...")
    
    # Alternative parsing method for problematic CSV
    with open('format.csv', 'r') as f:
        lines = f.readlines()
    
    # Get headers
    headers = lines[0].strip().split(',')
    
    # Process data
    data = []
    for line in lines[1:]:
        values = line.strip().split(',')
        # Ensure the row has the same number of columns as headers
        while len(values) < len(headers):
            values.append('')
        data.append(values[:len(headers)])
    
    main_df = pd.DataFrame(data, columns=headers)

# Read the mmData CSV file
mm_data_df = pd.read_csv('mmData.csv')

# Function to find the matching stone size
def find_stone_size(shape, sieve):
    if pd.isna(shape) or pd.isna(sieve):
        return np.nan
    
    # Normalize shape names for matching
    if isinstance(shape, str):
        shape_normalized = shape.upper().strip()
        if shape_normalized == 'RND':
            shape_normalized = 'RND'
    else:
        return np.nan
    
    # Convert sieve to float for comparison if it's a number
    try:
        sieve_value = float(sieve)
    except:
        sieve_value = sieve
    
    # Try to find a match
    for _, row in mm_data_df.iterrows():
        mm_shape = row['Stone Shape'].upper().strip()
        mm_sieve = row['Sieve /  MM']
        
        try:
            mm_sieve = float(mm_sieve)
        except:
            pass
        
        if mm_shape == shape_normalized and mm_sieve == sieve_value:
            return row['Stone Size']
    
    return np.nan

# Apply the function to each row
for i in range(len(main_df)):
    shape = main_df.iloc[i].get('Stone Shape')
    sieve = main_df.iloc[i].get('Sieve /  MM')
    
    if pd.notna(shape) and pd.notna(sieve):
        stone_size = find_stone_size(shape, sieve)
        if pd.notna(stone_size):
            main_df.loc[i, 'Stone Size'] = stone_size

# Save the updated file
main_df.to_csv('P_129977_updated.csv', index=False)

print("File updated successfully!")