import pandas as pd
import numpy as np
import requests


df = pd.read_excel('/home/neosoft/Project1/Excel_1.xlsx')
status = pd.read_excel('/home/neosoft/Project1/Excel_2.xlsx')
df2 = pd.read_excel('/home/neosoft/Project1/Excel_3.xlsx')
print(df2.columns)
df2[['fname', 'lname']] = df2['name'].str.split(' ', expand=True)
print(df2[['fname', 'lname']])
df3 = df2.drop('name', axis=1)

all_data_st = pd.merge(df, status, how='outer')
#all_data_st.to_excel('/home/neosoft/Downloads/project/1&2.xlsx',header=True)
# print(all_data_st)
#output_columns = ['id', 'fname', 'lname', 'date_of_birth', 'email', 'gender', 'address', 'age', 'contact', 'city', 'country']
all_merge = pd.merge(all_data_st, df3, how='outer')
print(all_merge)
all_merge.to_excel('/home/neosoft/Project1/Combine.xlsx', index=False, header=True)

########################################################################################
# Read the Excel file into a DataFrame
file_path = '/home/neosoft/Project1/Combine.xlsx'
df0 = pd.read_excel(file_path)

# Convert the column to string
column_name = 'contact'
df0[column_name] = df[column_name].astype(str)

# Format the numbers as Indian contact numbers
def format_indian_contact_number(number):
    # Assuming the original numbers are 10 digits
    if len(number) == 12:
        return ('+91' + number)
    else:
        # Handle cases where the number might have a different length
        # You can customize this part based on your specific requirements
        return number

df0[column_name] = df0[column_name].apply(format_indian_contact_number)

# Write the DataFrame back to the Excel file
df0.to_excel('output_file.xlsx', index=False)
print(df0)
 #########################################################################################

#Read data from API
api_url = 'https://raw.githubusercontent.com/Shoaib720/user-raw-dummy-data/main/user-raw-data.json'
api_response = requests.get(api_url)
api_data = api_response.json()
api_df = pd.DataFrame(api_data['data'])

output_file1 = pd.read_excel('/home/neosoft/Project1/output_file.xlsx')

# Step 3: Concatenate Excel files and API data
#all_data = pd.merge([output_file1, api_df],index=False)
all_data = pd.merge(output_file1, api_df, how='inner')

print(all_data)
all_data.to_excel('/home/neosoft/Project1/allcombine.xlsx', index=False)

all_data_no_duplicates = all_data.drop_duplicates()
print("DataFrame after removing duplicates:")
print(all_data_no_duplicates)

# Step 6: Create a consolidated dataframe with non-null values from multiple dataframes
#consolidated_data = all_data_no_duplicates.groupby(all_data_no_duplicates.columns.tolist(), as_index=False).agg(lambda x: x.max())
consolidated_data = all_data_no_duplicates

# Step 7: Save the combined data to a Excel file
consolidated_data.to_excel('/home/neosoft/Project1/CombinedAll_data.xlsx', index=False)


# Step 7: Save the combined data to a Parquet file
consolidated_data.to_parquet('/home/neosoft/Project1/CombinedAll_data.parquet', index=False)


