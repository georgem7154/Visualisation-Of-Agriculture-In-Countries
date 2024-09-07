import pandas as pd

# Load the dataset
def clean_data():
    file_path = 'climate.csv'
    data = pd.read_csv(file_path).sort_values(by=['Year'])
    data.drop_duplicates(inplace=True)
    data.info()  # I see no null values, # the data looks clean to me
    return data

