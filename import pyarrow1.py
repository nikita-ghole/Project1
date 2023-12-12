import pyarrow.parquet as pq
import pandas as pd

# Function to read Parquet file and return a Pandas DataFrame
def read_parquet(file_path):
    table = pq.read_table(file_path)
    df = table.to_pandas()
    return df

# Main function
def main():
    # Replace 'your_parquet_file.parquet' with the actual file path
    parquet_file_path = '/home/neosoft/Project1/CombinedAll_data.parquet'

    # Read Parquet file
    parquet_data = read_parquet(parquet_file_path)

    # Print top 5 rows along with all columns
    print(parquet_data.head(5))
    
    
if __name__ == "__main__":
    main()

parquet_file_path0 = '/home/neosoft/Project1/CombinedAll_data.parquet'
table = pq.read_table(parquet_file_path0)
print(table)
schema = table.schema
column_names = [field.name for field in schema]
print(column_names)