import argparse

def create_parser():
    parser = argparse.ArgumentParser(description='General Data Converter.')
    parser.add_argument('--input-file', required=True, help='The path to the input file to convert.')
    parser.add_argument('--output-dir', required=True, help='The directory to output the converted file to.')
    parser.add_argument('--output-format', required=True, help='The format to convert the input file to.')

    return parser
