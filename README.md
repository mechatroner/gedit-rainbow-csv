# gedit-rainbow-csv
Syntax highlighting rules for csv and tsv files in gtk (gedit)

Columns in csv/tsv file will be higlighted in different rainbow colors. This helps to understand data patterns in csv files more quickly. Every 10-th column is not highlighted (has default black color)

## csv/tsv autodetection
For rainbow syntax higlighting to work, csv/tsv file is not required to have \*.csv/\*.tsv extension. Plugin has csv autodetection mechanism if enabled.

## Installation Instructions:

1. Run `./install.py`
2. Launch gedit. Go to `Edit->Preferences->Plugins` and enable "Rainbow csv" plugin
3. Restart gedit

## Screenshots

![screenshot](https://raw.githubusercontent.com/mechatroner/gedit-rainbow-csv/master/screenshot.png)
