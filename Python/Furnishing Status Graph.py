import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate average price by category and plot a bar graph
def calculate_average_and_plot(file_path, category_column, value_column):
    try:
        # Load the CSV file
        df = pd.read_csv(file_path)

        # Strip whitespace from column names
        df.columns = df.columns.str.strip()

        # Check if the specified columns exist
        if category_column in df.columns and value_column in df.columns:
            # Convert value column to numeric
            df[value_column] = pd.to_numeric(df[value_column], errors='coerce')

            # Drop rows with missing values in either column
            df = df.dropna(subset=[category_column, value_column])
            
            # Group by the category column and calculate the average of the value column
            average_values = df.groupby(category_column)[value_column].mean().reset_index()
            average_values[value_column] = average_values[value_column].round().astype(int)
            print(f"Average of '{value_column}' categorized by '{category_column}':")
            print(average_values)

            # Plotting the bar graph
            plt.figure(figsize=(10, 6))
            plt.bar(average_values[category_column], average_values[value_column], color='skyblue', edgecolor='black')
            plt.title(f'Average Price vs Furnishing Status')
            plt.xlabel("Furnishing Status")
            plt.ylabel("Average Price by Millions")
            plt.xticks(rotation=45)  # Rotate x-ticks for better readability
            max_price = average_values[value_column].max() + 1000000  # Set a little higher than the max value for better visualization
            plt.yticks(range(0, int(max_price), 1000000), [f'{i//1000000}M' for i in range(0, int(max_price), 1000000)])
            plt.grid(axis='y', linestyle='--', alpha=0.7)
            plt.tight_layout()
            plt.show()
        else:
            print(f"One or both columns do not exist: '{category_column}', '{value_column}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
file_path = 'Housing.csv'  
value_column = 'price'  
category_column = 'furnishingstatus'  # Change category to furnishing status

# Define the columns in the DataFrame
df_columns = ['price    ', 'area  ', 'bedrooms ', 'bathrooms ', 'stories ',
              'mainroad ', 'guestroom ', 'basement ', 'hotwaterheating ',
              'airconditioning ', 'parking ', 'prefarea ', 'furnishingstatus']
# Assign cleaned column names to the DataFrame
df = pd.read_csv(file_path)
df.columns = df_columns

# Call the function to calculate averages and plot
calculate_average_and_plot(file_path, category_column, value_column)
