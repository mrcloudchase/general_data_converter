import os
import pandas as pd
from src.data_converter.formats import xml

def test_read_xml():
    # Create a test XML file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_csv('test.xml', index=False)

    # Use the function to read the XML
    data = xml.read_xml('test.xml')

    # Check that the data matches
    pd.testing.assert_frame_equal(data, df)

    # Clean up
    os.remove('test.xml')


def test_write_xml():
    # Create some test data
    df = pd.DataFrame({
        'C': [7, 8, 9],
        'D': [10, 11, 12]
    })

    # Use the function to write the XML
    xml.write_xml(df, 'test.xml')

    # Check that the data matches
    data = pd.read_csv('test.xml')  # This assumes your XML -> DataFrame conversion is similar to CSV
    pd.testing.assert_frame_equal(data, df)

    # Clean up
    os.remove('test.xml')
