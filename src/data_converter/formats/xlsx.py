import pandas as pd

# Only read the first sheet
# def read_xlsx(file_path):
#     return pd.read_excel(file_path)

# Read all sheets
def read_xlsx(file_path):
    # Read the Excel file
    xlsx = pd.ExcelFile(file_path)
    
    # Create a dictionary to hold dataframes for each sheet
    df_dict = {}
    
    # Iterate over each sheet in the Excel file
    for sheet in xlsx.sheet_names:
        # Read the sheet into a dataframe
        df = pd.read_excel(xlsx, sheet_name=sheet)
        
        # Add the dataframe to the dictionary
        df_dict[sheet] = df
    
    # Return the dictionary of dataframes
    return df_dict

def write_xlsx(data, file_path):
    data.to_excel(file_path, index=False)
