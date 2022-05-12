import pandas as pd
import numpy as np
import argparse
import os

# helper function to split a large dataframe into smaller chunks
def split(df, num_chunks):
    return np.array_split(df, num_chunks)

def main(src_file, dst_dir, num_chunks, sheet_name):
    # create the destination directory if it doesn't already exist
    os.makedirs(dst_dir, exist_ok=True)

    # read the excel sheet into a dataframe
    df = pd.read_excel(src_file)

    # split the large dataframe into 160 dataframes, each with a maximum of 100 rows
    dfs = split(df, num_chunks=num_chunks)

    # write the chunks to excel files
    index = 1
    total_processed_rows = 0

    print(f'{src_file} contains {len(df)} rows.')

    for _df in dfs:
        _df.to_excel(f'{dst_dir}/{index}.xlsx', index=False, sheet_name=sheet_name)
        index += 1
        total_processed_rows += len(_df)

    print(f'Finished processing {total_processed_rows} rows. Saved chunks to {dst_dir}.')

parser = argparse.ArgumentParser()

parser.add_argument('--src-file', help='The relative path to the src excel file.', required=True)
parser.add_argument('--dst-dir', help='The relative path to the destination directory to save the file chunks too.', required=True)
parser.add_argument('--num-chunks', help='The number of chunks to split the file into.', required=True, type=int)
parser.add_argument('--sheet-name', help='The name of the sheet on the chunk files.', default='Sheet1')

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.src_file, args.dst_dir, args.num_chunks, args.sheet_name)