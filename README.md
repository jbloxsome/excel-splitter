# Excel Splitter
A small Python script for splitting large Excel files into smaller chunks.

## Usage
### Parameters
- --src-file 
    The relative path to the original excel spreadsheet.

- --dst-dir
    The relative path to the directory to write the chunks to.

- --num-chunks
    The number of chunks to split the file into.

- --sheet-name
    The name of the sheet on the chunk files.

### Example
```
python main.py --src-file ./spreadsheet.xlsx --dst-dir ./outputs --num-chunks 100 --sheet-name 'Web Products - for the OW impor'
```