import os
import pandas as pd
import json
from src.data_converter.formats import json

def test_read_json():
    # Create a test JSON file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_json('test.json', orient='records')

    # Use the function to read the JSON
    data = json.read_json('test.json')

    # Check that the data matches
    pd.testing.assert_frame_equal(data, df)

    # Clean up
    os.remove('test.json')


def test_write_json():
    # Create some test data
    df = pd.DataFrame({
        'C': [7, 8, 9],
        'D': [10, 11, 12]
    })

    # Use the function to write the JSON
    json.write_json(df, 'test.json')

    # Check that the data matches
    with open('test.json') as json_file:
        data = json.load(json_file)
    assert data == json.loads(df.to_json(orient='records'))

    # Clean up
    os.remove('test.json')
