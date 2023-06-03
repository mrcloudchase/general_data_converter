import pandas as pd
import argparse

def create_parser():
    # Create the parser
    parser = argparse.ArgumentParser(prog='General Data Converter',
                                     description='Convert data between different formats.',
                                     epilog='Thank you for using the General Data Converter!')

    # Add the arguments
    parser.add_argument('--input-file',
                        type=str,
                        required=True,
                        help='The path to the input file')

    parser.add_argument('--output-dir',
                        type=str,
                        required=True,
                        help='The directory where the output should be written')

    parser.add_argument('--output-format',
                        type=str,
                        choices=['json', 'xml', 'csv', 'xlsx'],
                        required=True,
                        help='The format of the output file')

    # Parse the arguments
    args = parser.parse_args()

    # You can access the argument values like this:
    print(f"Input file: {args.input_file}")
    print(f"Output directory: {args.output_dir}")
    print(f"Output format: {args.output_format}")

    # Return the arguments
    return args

# Function to take xlsx input file from args and return a dictionary of DataFrames (one for each sheet)
def read_xlsx(input_file: str):
    # Read the input file
    data = pd.ExcelFile(input_file)

    # Return the data
    return data

# Main function
def main():
    # Create the parser
    parser = create_parser()

    # Read the input file
    data = read_xlsx(parser.input_file)

    # Write the data to the output directory in the output format
    output_file = os.path.join(parser.output_dir, f'output.{parser.output_format}')
    write_xlsx(data, output_file)

    

if __name__ == "__main__":
    main()
