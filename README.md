![Honeycomb frame close up tilted to the light, the empty cells showing as a plain pale patch among the capped and open cells around them](intro-banner.png)

# analyze-system

![Apiary in flat daylight with a beekeeper holding one honeycomb frame up at the centre, rows of hive boxes standing in order behind with one red strap across the nearest box and further frames leaning at the bench](banner.png)

![Wooden honeycomb frame held up to the light, its wax cells in three kinds across the frame: dark capped cells, open cells of amber honey, and a patch of pale empty cells](logo.png)

![The slipway in three bands: surf falling back, a wet sheen climbing the rails, the winch cable stirring in the foreground](scene.svg)




![Major section divider](sep-heavy.svg)

> Flare post notice: this tool runs no security checks despite its name. It reads a CSV file and reports a count, nothing more.

> Flare post notice: both --input and --output are required for every run. One names the CSV to read, the other names the report file to write.

## Project description

The `analyze-system` tool is a CSV summary reporter focused on data analysis and reporting. It provides a command-line interface that reads a CSV file and writes a summary report with the row count, the null values per column, and the column data types.


![Major section divider](sep-heavy.svg)

## Installation instructions

To run the `analyze-system` tool, you will need Python 3 installed. Clone this repository, then install the one dependency listed in requirements.txt:

```sh
pip install -r requirements.txt
```


![Major section divider](sep-heavy.svg)

## Usage examples

To use the `analyze-system` tool, you can run the following command:

```sh
python main.py --input INPUT.csv --output REPORT.txt [--verbose]
```

The following options are available:

* `-h`, `--help`: Show help message and exit
* `--input`: Path to the input CSV file containing system logs or data to analyze (required)
* `--output`: Path to the output file where the analysis report will be saved (required)
* `--verbose`: Enable verbose logging

For example, to generate a report in the file `my-report.txt` from `data.csv`, you can run:

```sh
python main.py --input data.csv --output my-report.txt
```

The report contains the row count, the null values per column, and the column data types of the input file. No security checks are run on the host itself.


![Major section divider](sep-heavy.svg)

## Security warnings

The `analyze-system` tool is not a security audit tool and runs no security checks. Its report is a summary of the input CSV only: row count, null values per column, and column data types. It says nothing about the security status of a system.


![Major section divider](sep-heavy.svg)

## License

The `analyze-system` tool is licensed under the GNU General Public License v3.0 and licensed to CY83R-3X71NC710N.
