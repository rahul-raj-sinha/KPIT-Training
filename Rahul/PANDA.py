import pandas as pd
 
mydataset = {
    'cars': ['Tata', 'Mahindra', 'Maruti'],
    'safety': [5, 3, 2]
}
print(mydataset)
 
pdf = pd.DataFrame(mydataset)
print(pdf)
 
print('*' * 60)
cars = ['tata', 'maruti', 'hyundai', 'honda']
print(cars)
 
psrs = pd.Series(cars)
print(psrs[0])
 
print(psrs.values)
print('*' * 60)
 
psrs1 = pd.Series(cars, index=['a', 'b', 'c', 'd'])
print(psrs1)
print('*' * 60)
 
score = {'Sachin: 85', 'Sehwag: 120', 'Dravid: 45', 'Sourav: 60'}
print(f"Scores: {score}")
 
plsrs = pd.Series(score)
print(plsrs)
 
print(f"Dravid: {plsrs['Dravid']}")





# # Data Manipulation using pandas
# import pandas as pd

# # Get user input for number of rows and columns
# rows = int(input("Enter the number of rows: "))
# cols = int(input("Enter the number of columns: "))

# # Initialize an empty DataFrame
# data = {}

# # Get user input for column names and data
# for j in range(cols):
#     col_name = input(f"Enter name for column {j+1}: ")
#     column_data = [float(input(f"Enter data for column {col_name}, row {i+1}: ")) for i in range(rows)]
#     data[col_name] = column_data

# # Create DataFrame
# df = pd.DataFrame(data)

# # Perform data manipulation
# df_sum = df.sum(axis=1)  # Sum of each row
# df_avg = df.mean(axis=0)  # Average of each column

# # Display results
# print("\nDataFrame:")
# print(df)
# print("\nSum of each row:")
# print(df_sum)
# print("\nAverage of each column:")
# print(df_avg)







# # Pandas Examples
# import pandas as pd

# # 1. Create a DataFrame from user input dictionary and display the first 5 rows
# data = {}
# num_cols = int(input("Enter the number of columns: "))
# num_rows = int(input("Enter the number of rows: "))

# for i in range(num_cols):
#     col_name = input(f"Enter name for column {i + 1}: ")
#     data[col_name] = [float(input(f"Enter data for column {col_name}, row {j + 1}: ")) for j in range(num_rows)]

# df = pd.DataFrame(data)
# print("\n1. DataFrame:")
# print(df.head())

# # 2. Load a CSV file into a DataFrame and display the summary statistics of numerical columns
# csv_file = input("Enter path to CSV file: ")
# df_csv = pd.read_csv(csv_file)
# print("\n2. Summary Statistics of Numerical Columns:")
# print(df_csv.describe())

# # 3. Merge two DataFrames along a specified column
# # Let's create two DataFrames from user inputs for demonstration
# data1 = {}
# data2 = {}
# merge_col = input("Enter common column name for merging: ")

# for i in range(2):
#     for j in range(num_rows):
#         col_name = input(f"Enter name for column {j + 1} in DataFrame {i + 1}: ")
#         if i == 0:
#             data1[col_name] = [float(input(f"Enter data for {col_name}, row {j + 1} in DataFrame {i + 1}: ")) for _ in range(num_rows)]
#         else:
#             data2[col_name] = [float(input(f"Enter data for {col_name}, row {j + 1} in DataFrame {i + 1}: ")) for _ in range(num_rows)]

# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)

# merged_df = pd.merge(df1, df2, on=merge_col)
# print("\n3. Merged DataFrame:")
# print(merged_df)

# # 4. Filter rows of a DataFrame based on a given condition
# filter_column = input("Enter column name to filter: ")
# filter_value = float(input("Enter value to filter: "))
# filtered_df = df_csv[df_csv[filter_column] == filter_value]
# print("\n4. Filtered DataFrame:")
# print(filtered_df)

# # 5. Create a pivot table from a DataFrame with multiple index levels and columns
# pivot_index = input("Enter name for pivot table index: ")
# pivot_columns = input("Enter name for pivot table columns: ")
# pivot_values = input("Enter name for pivot table values: ")
# pivot_table = df_csv.pivot_table(values=pivot_values, index=pivot_index, columns=pivot_columns)
# print("\n5. Pivot Table:")
# print(pivot_table)

# # 6. Load an Excel file into a DataFrame and perform data cleaning by handling missing values
# excel_file = input("Enter path to Excel file: ")
# df_excel = pd.read_excel(excel_file)
# cleaned_df = df_excel.fillna(method='ffill')  # Forward fill missing values
# print("\n6. Cleaned DataFrame:")
# print(cleaned_df)

# # 7. Group a DataFrame by one or more columns and perform aggregation functions
# group_by_cols = input("Enter column names to group by (comma separated): ").split(',')
# agg_func = input("Enter aggregation function (sum, mean, count, etc.): ")
# grouped_df = df_csv.groupby(group_by_cols).agg(agg_func)
# print("\n7. Grouped DataFrame:")
# print(grouped_df)

# # 8. Sort rows of a DataFrame based on one or more columns in ascending and descending order
# sort_cols = input("Enter column names to sort by (comma separated): ").split(',')
# sort_order = input("Enter sort order (asc or desc): ")
# sorted_df = df_csv.sort_values(by=sort_cols, ascending=(sort_order.lower() == 'asc'))
# print("\n8. Sorted DataFrame:")
# print(sorted_df)

# # 9. Create a new column in a DataFrame by applying a function to existing columns
# new_col_name = input("Enter name for new column: ")
# function_str = input("Enter function to apply (e.g., 'lambda x: x*2'): ")
# apply_function = eval(f"lambda x: {function_str}")
# df_csv[new_col_name] = df_csv.apply(lambda row: apply_function(row), axis=1)
# print("\n9. DataFrame with New Column:")
# print(df_csv)

# # 10. Perform a left join between two DataFrames on a common column
# # Let's use the merged_df and df_csv from previous questions for demonstration
# join_on_col = input("Enter common column name for left join: ")
# left_join_df = pd.merge(merged_df, df_csv, on=join_on_col, how='left')
# print("\n10. Left Join DataFrame:")
# print(left_join_df)

# # import pandas as pd

# # 11. Load a JSON file into a DataFrame and display the first 5 rows
# json_file = input("Enter path to JSON file: ")
# df_json = pd.read_json(json_file)
# print("\n11. DataFrame from JSON:")
# print(df_json.head())

# # 12. Merge two DataFrames using an outer join along a specified column
# column_to_merge_on = input("Enter column name for merging: ")
# df1 = pd.DataFrame(eval(input("Enter data for first DataFrame as a list of dictionaries: ")))
# df2 = pd.DataFrame(eval(input("Enter data for second DataFrame as a list of dictionaries: ")))
# merged_df = pd.merge(df1, df2, on=column_to_merge_on, how='outer')
# print("\n12. Merged DataFrame:")
# print(merged_df)

# # 13. Drop duplicate rows from a DataFrame based on a subset of columns
# subset_columns = input("Enter column names to consider for duplicate check (comma separated): ").split(',')
# df_duplicates = pd.DataFrame(eval(input("Enter data for DataFrame as a list of dictionaries: ")))
# df_duplicates_dropped = df_duplicates.drop_duplicates(subset=subset_columns)
# print("\n13. DataFrame with Duplicate Rows Dropped:")
# print(df_duplicates_dropped)

# # 14. Create a pivot table from a DataFrame with mean values for each group
# pivot_index = input("Enter name for pivot table index: ")
# pivot_columns = input("Enter name for pivot table columns: ")
# pivot_values = input("Enter name for pivot table values: ")
# df_pivot = pd.DataFrame(eval(input("Enter data for DataFrame as a list of dictionaries: ")))
# pivot_table = df_pivot.pivot_table(values=pivot_values, index=pivot_index, columns=pivot_columns, aggfunc='mean')
# print("\n14. Pivot Table with Mean Values:")
# print(pivot_table)

# # 15. Load a CSV file into a DataFrame and handle missing values by filling them with the mean of the column
# csv_file = input("Enter path to CSV file: ")
# df_csv = pd.read_csv(csv_file)
# df_csv_filled = df_csv.fillna(df_csv.mean())
# print("\n15. DataFrame with Missing Values Filled:")
# print(df_csv_filled)

# # 16. Convert a DataFrame into a CSV file and save it to disk
# csv_output_path = input("Enter path for CSV output file: ")
# df_to_csv = pd.DataFrame(eval(input("Enter data for DataFrame as a list of dictionaries: ")))
# df_to_csv.to_csv(csv_output_path, index=False)
# print("\n16. DataFrame Saved to CSV File.")

# # 17. Rename columns of a DataFrame based on a mapping dictionary
# df_rename = pd.DataFrame(eval(input("Enter data for DataFrame as a list of dictionaries: ")))
# column_mapping = eval(input("Enter column mapping as a dictionary (old_name: new_name): "))
# df_renamed = df_rename.rename(columns=column_mapping)
# print("\n17. DataFrame with Renamed Columns:")
# print(df_renamed)

# # 18. Create a new column in a DataFrame by applying a function to existing columns and group-wise operations
# new_column_name = input("Enter name for new column: ")
# function_str = input("Enter function to apply to existing columns (e.g., 'lambda x: x*2'): ")
# apply_function = eval(f"lambda x: {function_str}")
# df_apply_function = pd.DataFrame(eval(input("Enter data for DataFrame as a list of dictionaries: ")))
# df_apply_function[new_column_name] = df_apply_function.apply(lambda row: apply_function(row), axis=1)
# print("\n18. DataFrame with New Column:")
# print(df_apply_function)

# # 19. Calculate the correlation matrix of a DataFrame and visualize it using a heatmap
# import seaborn as sns
# df_corr = pd.DataFrame(eval(input("Enter data for DataFrame as a list of dictionaries: ")))
# correlation_matrix = df_corr.corr()
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# print("\n19. Correlation Matrix:")
# print(correlation_matrix)

# # 20. Load an HTML table into a DataFrame and extract specific rows and columns
# html_file = input("Enter path to HTML file: ")
# dfs_html = pd.read_html(html_file)
# df_html = dfs_html[0]  # Assuming first table is of interest
# rows_to_extract = eval(input("Enter row indices to extract as a list: "))
# columns_to_extract = eval(input("Enter column names to extract as a list: "))
# df_extracted = df_html.iloc[rows_to_extract, columns_to_extract]
# print("\n20. Extracted DataFrame from HTML:")
# print(df_extracted)

















