import pandas as pd

#File path to the notepad file#
file_path = r'E:\amazon\sales ID creation\rawdata.txt'
data = pd.read_csv(file_path, delimiter='\t')

print("Original Data:")
print(data.head())
print(data.columns)

# Removing rows where 'fulfillment-channel' is 'Amazon'
filtered_data = data[data['fulfillment-channel'] != 'Amazon']
print("\nFiltered Data (no Amazon in 'fulfillment-channel'):")
print(filtered_data.head())

# Removing rows where 'order-status' is 'CANCELLED'
cleaned_data = filtered_data[filtered_data['order-status'] != 'Cancelled']
print("\nCleaned Data (no Cancelled in 'order-status'):")
print(cleaned_data.head())

# Output file path to save the cleaned data
output_file_path = r'E:\amazon\sales ID creation\cleaned_rawdata.xlsx'
cleaned_data.to_excel(output_file_path, index=False)
