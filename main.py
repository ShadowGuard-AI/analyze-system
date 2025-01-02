import pandas as pd
import argparse
import logging
import sys

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_argparse():
    """
    Sets up the command-line interface.
    """
    parser = argparse.ArgumentParser(
        description="Analyze-system: A basic system security audit tool focused on data analysis and reporting."
    )
    parser.add_argument(
        "--input",
        type=str,
        required=True,
        help="Path to the input CSV file containing system logs or data to analyze."
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Path to the output file where the analysis report will be saved."
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging."
    )
    return parser

def analyze_data(input_file, output_file):
    """
    Core functionality to analyze system data from a CSV file and generate a report.

    Args:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the output report.
    """
    try:
        logging.info("Reading input CSV file...")
        data = pd.read_csv(input_file)

        logging.info("Performing data analysis...")
        summary = {
            "Total Rows": len(data),
            "Null Values": data.isnull().sum().to_dict(),
            "Column Data Types": data.dtypes.to_dict()
        }

        logging.info("Writing analysis report to output file...")
        with open(output_file, "w") as f:
            f.write("System Security Audit Report\n")
            f.write("============================\n")
            for key, value in summary.items():
                f.write(f"{key}: {value}\n")

        logging.info("Analysis complete. Report saved successfully.")
    
    except FileNotFoundError:
        logging.error(f"File not found: {input_file}")
        sys.exit(1)
    except pd.errors.EmptyDataError:
        logging.error("Input file is empty or corrupt.")
        sys.exit(1)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main entry point for the tool.
    """
    parser = setup_argparse()
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    logging.info("Starting analyze-system tool...")
    analyze_data(args.input, args.output)

if __name__ == "__main__":
    main()