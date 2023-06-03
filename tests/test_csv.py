import os
import pandas as pd
from src.data_converter.formats import csv

def test_read_csv():
    # Create a test CSV file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_csv('test.csv', index=False)

    # Use the function to read the CSV
    data = csv.read_csv('test.csv')

    # Check that the data matches
    pd.testing.assert_frame_equal(data, df)

    # Clean up
    os.remove('test.csv')


def test_write_csv():
    # Create some test data
    df = pd.DataFrame({
        'C': [7, 8, 9],
        'D': [10, 11, 12]
    })

    # Use the function to write the CSV
    csv.write_csv(df, 'test.csv')

    # Check that the data matches
    data = pd.read_csv('test.csv')
    pd.testing.assert_frame_equal(data, df)

    # Clean up
    os.remove('test.csv')
