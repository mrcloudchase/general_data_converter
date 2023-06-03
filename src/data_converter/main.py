import os
from src.data_converter.formats import xml, csv, xlsx, json
from src.data_converter.argparser import create_parser

def convert_data(input_file: str, output_dir: str, output_format: str):
    # Determine the format of the input file based on its extension
    input_format = os.path.splitext(input_file)[1][1:]

    # Define a dictionary that maps format names to functions for reading and writing that format
    formats = {
        'csv': {
            'read': csv.read_csv,
            'write': csv.write_csv
        },
        'xlsx': {
            'read': xlsx.read_xlsx,
            'write': xlsx.write_xlsx
        },
        'xml': {
            'read': xml.read_xml,
            'write': xml.write_xml
        },
        'json': {
            'read': json.read_json,
            'write': json.write_json
        }
    }

    # Check if the input and output formats are supported
    if input_format not in formats or output_format not in formats:
        raise ValueError('Unsupported format')

    # Read the input file
    data = formats[input_format]['read'](input_file)

    # Write the data to the output directory in the output format
    output_file = os.path.join(output_dir, f'output.{output_format}')
    formats[output_format]['write'](data, output_file)

def main():
    parser = create_parser()
    args = parser.parse_args()

    convert_data(args.input_file, args.output_dir, args.output_format)

if __name__ == "__main__":
    main()
