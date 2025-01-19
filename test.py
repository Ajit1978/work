import csv
import pandas as pd

def generate_jewelry_csv(filename="Format.csv"):
    """
    Generate a CSV file with jewelry design specifications
    """
    # Define the data as a list of rows
    data = [
        ["Design Number", "Vendor Style No", "ALTR no.", "Picture", "Metal Kt / Color", "Metal Rate $ P. Oz", 
         "Metal Wt. in Gm", "Metal Rate in Gms", "Metal Cost", "Finding Cost", "Stone Shape", "Stone Qlty",
         "Sieve /  MM", "Stone Size", "Stone wt. Total", "Stone Rate", "Stone Cost", "Stone Pcs",
         "Setting Type", "Setting Rate", "Setting Charges", "Other Charges", "Charges", "", "Details",
         "Minimum Diam Wt", "Cost", "Price 1"],
        
        ["VD163D2-R6605", "D2-RF2A4948", "ZR1584E-210GD-A", "", "14KW", "$2,800", "3.98", "58.81", 
         "234.08", "", "RD", "FG VS2", "7.3", "1.5", "", "", "$0.00", "1", "prong", "", "$0.00",
         "CFP", "$10.10", "", "Semi / Comp", "0.6", "$332.75", ""],
        
        ["make directly from cad", "RM 5455", "ZR1584SM-60CZ-L", "", "", "", "", "", "", "", "RD",
         "E VS2", "1.2", "0.008", "0.18", "$120.00", "$21.60", "20", "prong", "$0.50", "$10.00",
         "J Back", "", "", "Duty/Ship", "", "$23.29", ""],
        
        ["", "SIZE US 6.5", "", "", "", "", "", "", "", "", "RD", "E VS2", "1.4", "0.013", "0.26",
         "$88.00", "$22.88", "20", "prong", "$0.50", "$10.00", "Dia. Han.", "$1.83", "", "Total Imp. Cost",
         "", "$356.04", "$715"],
        
        ["", "", "", "", "", "", "", "", "", "", "RD", "E VS2", "1.7", "0.02", "0.04", "$88.00",
         "$3.52", "2", "prong", "$0.50", "$1.00", "Miligrain", "", "", "Center", "1.5", "$450.84",
         "$1,027.00"],
        
        ["", "", "", "", "", "", "", "", "", "", "RD", "E VS2", "2", "0.032", "0.064", "$79.00",
         "$5.06", "2", "prong", "$0.50", "$1.00", "Two Tone", "", "", "Setting", "", "$24.00", "$30.00"],
        
        ["", "", "", "", "", "", "", "", "", "", "RD", "E VS2", "2.3", "0.051", "0.102", "$79.00",
         "$8.06", "2", "prong", "$0.75", "$1.50", "Solder", "", "", "", "", "", ""],
        
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
         "engraving", "", "", "", "", "", ""],
        
        ["Main Category", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
         "", "", "Rhoudium", "$2.00", "", "", "", "", ""],
        
        ["Sub Category", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
         "", "", "", "", "", "Total", "2.1", "$831", "$1,772"],
        
        ["Collection", "", "", "", "", "", "Total", "234.08", "0", "", "", "", "", "0.646", "",
         "$61.11", "47", "", "", "$23.50", "", "$13.93", "", "Net Margin", "", "", "", "53%"]
    ]
    
    # Write data to CSV file
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    print(f"CSV file '{filename}' has been generated successfully!")

# Run the function to generate the CSV
if __name__ == "__main__":
    generate_jewelry_csv()