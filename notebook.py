import pandas as pd

# Load the CSV file to inspect its contents
file_path = 'C:/Users/ADMIN/Desktop/funddatascience/ecommerce_customer_data_large.csv'
data = pd.read_csv(file_path)

# Display basic information and first few rows of the dataset to assess its structure
data_info = data.info()
data_head = data.head()

data_info, data_head

# Step 1: Remove duplicate 'Age' column
data_cleaned = data.drop(columns=['Age'])

# Step 2: Convert 'Purchase Date' to datetime format
data_cleaned['Purchase Date'] = pd.to_datetime(data_cleaned['Purchase Date'], format='%Y-%m-%d %H:%M:%S')

# Step 3: Handle missing values in 'Returns' column
# Since 'Returns' indicates whether a purchase was returned (1.0) or not (0.0),
# we can assume missing values mean no return (0.0)
data_cleaned['Returns'].fillna(0.0, inplace=True)

# Step 4: Verify 'Total Purchase Amount' consistency
# Calculate if Total Purchase Amount matches Product Price * Quantity
data_cleaned['Calculated Total'] = data_cleaned['Product Price'] * data_cleaned['Quantity']
inconsistent_totals = data_cleaned[data_cleaned['Total Purchase Amount'] != data_cleaned['Calculated Total']]

# Remove the 'Calculated Total' column after the check
data_cleaned.drop(columns=['Calculated Total'], inplace=True)

# Output results
data_cleaned_info = data_cleaned.info()
inconsistent_totals_count = inconsistent_totals.shape[0]

data_cleaned_info, inconsistent_totals_count

# Save the cleaned data to a CSV file
data_cleaned.to_csv('C:/Users/ADMIN/Desktop/funddatascience/ecommerce_customer_data_large - preprocessed.csv', index=False)
