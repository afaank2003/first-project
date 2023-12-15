import pandas as pd
# In this code, I will use an archeological dataset to determine which province of the Roman Empire has the most known inscriptions.

# Loading the dataset
file_path = "C:/Users/afaan/Downloads/merged_edh_data.csv"
edh_data = pd.read_csv(file_path)

# Counting the number of inscriptions per province
inscription_counts = edh_data['provinz_x'].value_counts()

# Displaying the top provinces with the most inscriptions
print(inscription_counts.head())

# List of top provinces
top_provinces = ['GeS', 'Dal', 'Rom', 'HiC', 'Afr']

# Creating the subset
subset_data = edh_data[edh_data['provinz_x'].isin(top_provinces)]

# Saving the subset to a new CSV file
subset_file_path = "C:/Users/afaan/Downloads/edh_data_top_provinces.csv"
subset_data.to_csv(subset_file_path, index=False)