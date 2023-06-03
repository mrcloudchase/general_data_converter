import pytest
from src.data_converter.argparser import create_parser

def test_create_parser_no_args():
    """
    Test that the parser works as expected when no arguments are given.
    """
    parser = create_parser()
    with pytest.raises(SystemExit):
        parser.parse_args([])

def test_create_parser_with_args():
    """
    Test that the parser works as expected when arguments are given.
    """
    parser = create_parser()
    args = parser.parse_args(['--input-file', 'input.csv', '--output-dir', '.', '--output-format', 'json'])
    
    assert args.input_file == 'input.csv'
    assert args.output_dir == '.'
    assert args.output_format == 'json'
