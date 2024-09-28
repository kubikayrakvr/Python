import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Housing.csv')

def calculate_average_by_category(file_path, category_column, value_column):
    try:
        df = pd.read_csv(csv)

        df.columns = df.columns.str.strip()

        if category_column in df.columns and value_column in df.columns:
            df[value_column] = pd.to_numeric(df[value_column], errors='coerce')

            df = df.dropna(subset=[category_column, value_column])

            average_values = df.groupby(category_column)[value_column].mean().reset_index()
            print(f"Average of '{value_column}' categorized by '{category_column}':")
            average_values[value_column] = average_values[value_column].round().astype(int)
          
            plt.figure(figsize=(10, 6))
            plt.scatter(df[category_column], df[value_column], alpha=0.5, color='blue', label='Individual Prices')
            plt.plot(average_values[category_column], average_values[value_column], color='red', linewidth=2, label='Average Price')
            plt.title(f'Price vs Number of {category_column.capitalize()}')
            plt.xlabel(category_column.capitalize())
            plt.ylabel("Price by Millions")
            plt.xticks(df[category_column].unique())
            plt.grid(True)
            plt.legend()
            plt.tight_layout()
            plt.show()
        else:
            print(f"One or both columns do not exist: '{category_column}', '{value_column}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

csv = 'Housing.csv'  
value_column = 'price'  
category_column = 'bedrooms'
df.columns = ['price    ', 'area  ', 'bedrooms ', 'bathrooms ', 'stories ',
       'mainroad ', 'guestroom ', 'basement ', 'hotwaterheating ',
       'airconditioning ', 'parking ', 'prefarea ', 'furnishingstatus']
calculate_average_by_category(csv, category_column, value_column)
