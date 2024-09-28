import pandas as pd
import matplotlib.pyplot as plt

def plot_correlation_matrix(file_path):
    try:
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        for column in df.columns:
            if df[column].dtype == object:
                df[column] = pd.to_numeric(df[column].str.strip(), errors='coerce')
        df = df.dropna(axis=1, how='all')

        correlation_matrix = df.corr()

        print("Correlation Matrix:\n", correlation_matrix)

        plt.figure(figsize=(12, 8))
        cax = plt.matshow(correlation_matrix, cmap='coolwarm', fignum=1)
        plt.colorbar(cax)

        plt.xticks(range(len(correlation_matrix.columns)), correlation_matrix.columns, rotation=45)
        plt.yticks(range(len(correlation_matrix.columns)), correlation_matrix.columns)

        plt.title('Correlation Matrix', pad=20)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

file_path = 'Housing.csv'  
plot_correlation_matrix(file_path)
