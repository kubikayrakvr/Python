import pandas as pd
import matplotlib.pyplot as plt

def plot_histograms(file_path, value_column, category_column):
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        if category_column in df.columns and value_column in df.columns:
            df[value_column] = pd.to_numeric(df[value_column], errors='coerce')
            df.dropna(subset=[category_column, value_column], inplace=True)

            unique_categories = df[category_column].unique()

            plt.figure(figsize=(12, 8))
            for category in unique_categories:
                subset = df[df[category_column] == category]
                plt.hist(subset[value_column], bins=20, alpha=0.5, label=str(category), edgecolor='black')

            plt.title(f'Distribution of {value_column.capitalize()} by {category_column.capitalize()}')
            plt.xlabel("Price by Millions")
            max_price = df[value_column].max() + 1000000
            plt.xticks(range(0, int(max_price), 1000000), [f'{i//1000000} M' for i in range(0, int(max_price), 1000000)])
            plt.ylabel('Frequency')
            plt.legend(title=category_column.capitalize())
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        else:
            print(f"Sütun ya da sütunlar mevcut değil: '{category_column}', '{value_column}'.")
    except Exception as e:
        print(f"Hata: {e}")
file_path = 'Housing.csv'
value_column = 'price'
category_columns = ['area', 'bedrooms', 'stories']

for category_column in category_columns:
    plot_histograms(file_path, value_column, category_column)
