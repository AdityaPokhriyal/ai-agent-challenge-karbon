# run_parser_test.py
import sys
import pandas as pd
from importlib import import_module

def run_test(bank_name: str):
    """
    Dynamically imports and tests a parser.
    Exits with code 0 on success, 1 on failure.
    """
    try:
        # Define file paths based on the bank name
        pdf_path = f"data/{bank_name}/{bank_name} sample.pdf"
        csv_path = f"data/{bank_name}/result.csv"
        parser_module_path = f"custom_parsers.{bank_name}_parser"

        # Load the ground truth data
        expected_df = pd.read_csv(csv_path)

        # Dynamically import the agent-generated parser
        parser_module = import_module(parser_module_path)
        
        # Run the parser function
        # The agent must generate a function with this exact name and signature 
        actual_df = parser_module.parse(pdf_path)

        # The core test: compare DataFrames 
        if expected_df.equals(actual_df):
            print("Test Passed: Output matches the expected CSV.")
            sys.exit(0)
        else:
            print("Test Failed: DataFrame mismatch.")
            print("\nExpected DataFrame head:")
            print(expected_df.head())
            print("\nActual DataFrame head:")
            print(actual_df.head())
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed with error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_parser_test.py <bank_name>")
        sys.exit(1)
    
    bank = sys.argv[1]
    run_test(bank)