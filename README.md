![Banner](banner.png)

# analyze-system

## Project description

The `analyze-system` tool is a CSV summary reporter focused on data analysis and reporting. It provides a command-line interface that reads a CSV file and writes a summary report with the row count, the null values per column, and the column data types.

## Installation instructions

To run the `analyze-system` tool, you will need Python 3 installed. Clone this repository, then install the one dependency listed in requirements.txt:

```
pip install -r requirements.txt
```

## Usage examples

To use the `analyze-system` tool, you can run the following command:

```
python main.py --input INPUT.csv --output REPORT.txt [--verbose]
```

The following options are available:

* `-h`, `--help`: Show help message and exit
* `--input`: Path to the input CSV file containing system logs or data to analyze (required)
* `--output`: Path to the output file where the analysis report will be saved (required)
* `--verbose`: Enable verbose logging

For example, to generate a report in the file `my-report.txt` from `data.csv`, you can run:

```
python main.py --input data.csv --output my-report.txt
```

The report contains the row count, the null values per column, and the column data types of the input file. No security checks are run on the host itself.

## Security warnings

The `analyze-system` tool is not a security audit tool and runs no security checks. Its report is a summary of the input CSV only: row count, null values per column, and column data types. It says nothing about the security status of a system.

## License

The `analyze-system` tool is licensed under the GNU General Public License v3.0 and licensed to CY83R-3X71NC710N.