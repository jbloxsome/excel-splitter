# Excel Splitter
A small Python script for splitting large Excel files into smaller chunks.

## Usage
### Parameters
- --input-file 
    The relative path to the original excel spreadsheet.

- --output-dir
    The relative path to the directory to write the chunks to.

- --num-chunks
    The number of chunks to split the file into.

### Example
```
python main.py --input-file ./spreadsheet.xlsx --output-dir ./outputs --num-chunks 100
```