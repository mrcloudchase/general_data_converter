import os
import pandas as pd
from src.data_converter.formats import xlsx

def test_read_xlsx():
    # Create a test XLSX file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_excel('test.xlsx', index=False)

    # Use the function to read the XLSX
    data = xlsx.read_xlsx('test.xlsx')

    # Check that the data matches
    pd.testing.assert_frame_equal(data, df)

    # Clean up
    os.remove('test.xlsx')


def test_write_xlsx():
    # Create some test data
    df = pd.DataFrame({
        'C': [7, 8, 9],
        'D': [10, 11, 12]
    })

    # Use the function to write the XLSX
    xlsx.write_xlsx(df, 'test.xlsx')

    # Check that the data matches
    data = pd.read_excel('test.xlsx')
    pd.testing.assert_frame_equal(data, df)

    # Clean up
    os.remove('test.xlsx')
