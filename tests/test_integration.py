import os
import pandas as pd
from src.data_converter import main
import xml.etree.ElementTree as ET

def test_integration_csv_to_json():
    # Create a test CSV file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_csv('test.csv', index=False)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.csv', '--output-dir', '.', '--output-format', 'json'])
    main.convert_data(args.input_file, args.output_dir, args.output_format)

    # Check that the output JSON file was created correctly
    output_df = pd.read_json('test.json', orient='records', lines=True)
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.csv')
    os.remove('test.json')


def test_integration_csv_to_xlsx():
    # Create a test CSV file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_csv('test.csv', index=False)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.csv', '--output-dir', '.', '--output-format', 'xlsx'])
    main.convert_data(args)

    # Check that the output XLSX file was created correctly
    output_df = pd.read_excel('test.xlsx')
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.csv')
    os.remove('test.xlsx')


def test_integration_csv_to_xml():
    # Create a test CSV file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_csv('test.csv', index=False)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.csv', '--output-dir', '.', '--output-format', 'xml'])
    main.convert_data(args)

    # Check that the output XML file was created correctly
    output_df = pd.read_xml('test.xml')  # Assumes you've implemented a read_xml function in pandas
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.csv')
    os.remove('test.xml')

def test_integration_json_to_csv():
    # Create a test JSON file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_json('test.json', orient='records')

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.json', '--output-dir', '.', '--output-format', 'csv'])
    main.convert_data(args)

    # Check that the output CSV file was created correctly
    output_df = pd.read_csv('test.csv')
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.json')
    os.remove('test.csv')


def test_integration_json_to_xlsx():
    # Create a test JSON file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_json('test.json', orient='records')

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.json', '--output-dir', '.', '--output-format', 'xlsx'])
    main.convert_data(args)

    # Check that the output XLSX file was created correctly
    output_df = pd.read_excel('test.xlsx')
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.json')
    os.remove('test.xlsx')


def test_integration_json_to_xml():
    # Create a test JSON file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_json('test.json', orient='records')

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.json', '--output-dir', '.', '--output-format', 'xml'])
    main.convert_data(args)

    # Check that the output XML file was created correctly
    output_df = pd.read_xml('test.xml')  # Assumes you've implemented a read_xml function in pandas
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.json')
    os.remove('test.xml')

def test_integration_xlsx_to_csv():
    # Create a test XLSX file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_excel('test.xlsx', index=False)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.xlsx', '--output-dir', '.', '--output-format', 'csv'])
    main.convert_data(args)

    # Check that the output CSV file was created correctly
    output_df = pd.read_csv('test.csv')
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.xlsx')
    os.remove('test.csv')


def test_integration_xlsx_to_json():
    # Create a test XLSX file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_excel('test.xlsx', index=False)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.xlsx', '--output-dir', '.', '--output-format', 'json'])
    main.convert_data(args)

    # Check that the output JSON file was created correctly
    output_df = pd.read_json('test.json')
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.xlsx')
    os.remove('test.json')


def test_integration_xlsx_to_xml():
    # Create a test XLSX file
    df = pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6]
    })
    df.to_excel('test.xlsx', index=False)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.xlsx', '--output-dir', '.', '--output-format', 'xml'])
    main.convert_data(args)

    # Check that the output XML file was created correctly
    output_df = pd.read_xml('test.xml')  # Assumes you've implemented a read_xml function in pandas
    pd.testing.assert_frame_equal(df, output_df)

    # Clean up
    os.remove('test.xlsx')
    os.remove('test.xml')

def create_xml_file(filename, data):
    root = ET.Element("root")

    for row in data:
        item = ET.SubElement(root, "item")
        for key, value in row.items():
            ET.SubElement(item, key).text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def test_integration_xml_to_csv():
    # Create a test XML file
    data = [
        {'A': 1, 'B': 4},
        {'A': 2, 'B': 5},
        {'A': 3, 'B': 6}
    ]
    create_xml_file('test.xml', data)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.xml', '--output-dir', '.', '--output-format', 'csv'])
    main.convert_data(args)

    # Check that the output CSV file was created correctly
    assert os.path.isfile('test.csv')

    # Clean up
    os.remove('test.xml')
    os.remove('test.csv')


def test_integration_xml_to_json():
    # Create a test XML file
    data = [
        {'A': 1, 'B': 4},
        {'A': 2, 'B': 5},
        {'A': 3, 'B': 6}
    ]
    create_xml_file('test.xml', data)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.xml', '--output-dir', '.', '--output-format', 'json'])
    main.convert_data(args)

    # Check that the output JSON file was created correctly
    assert os.path.isfile('test.json')

    # Clean up
    os.remove('test.xml')
    os.remove('test.json')


def test_integration_xml_to_xlsx():
    # Create a test XML file
    data = [
        {'A': 1, 'B': 4},
        {'A': 2, 'B': 5},
        {'A': 3, 'B': 6}
    ]
    create_xml_file('test.xml', data)

    # Run the application
    args = main.create_parser().parse_args(['--input-file', 'test.xml', '--output-dir', '.', '--output-format', 'xlsx'])
    main.convert_data(args)

    # Check that the output XLSX file was created correctly
    assert os.path.isfile('test.xlsx')

    # Clean up
    os.remove('test.xml')
    os.remove('test.xlsx')
