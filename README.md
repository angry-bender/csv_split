# CSV Chunk Splitter

This script splits a large CSV file into smaller chunks using `pandas`, making it easier to process and manage big data files.

## Features

- Automatically detects and splits CSV files based on row count
- Preserves headers in each output chunk
- Customizable chunk size
- Saves output chunks with sequential naming (e.g., chunk_1.csv, chunk_2.csv)

## Requirements

Install dependencies with:

`pip install -r requirements.txt`

## Usage

`python split_csv.py <input.csv>`

If you want to change chunk size from default 500
`python split_csv.py <input.csv> --chunk_size_mb <default 500>`

## Credits
This project was inspired by mungingdata.com’s guide on splitting CSVs with pandas, which provided the core logic for chunking large datasets in Python. - https://www.mungingdata.com/python/split-csv-write-chunk-pandas/




