# ------------------------------------------------------
# Filename: Main.py
# Author: Nibedita Bhowmick
# Due date: 2025-04-06
# Version: 2.3
# Description:
#     This script manages records for a childcare facility system.
#     It provides an interactive menu for loading, displaying, adding,
#     updating, deleting, sorting, and saving records.
# ------------------------------------------------------

import pandas as pd  # Importing pandas for data manipulation and analysis
import matplotlib.pyplot as plt  # Importing matplotlib for chart plotting
import os  # Importing os module for file path and file existence handling


# Model: Handles data loading and processing
class CSVModel:
    def __init__(self, file_path):
        # Check if the file exists at the given path, raise error if not
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")

        # Store the file path and load the CSV data into a pandas DataFrame
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def filter_records(self, column, value):
        """
        Filter records based on user input.
        Checks if the column exists and applies a case-insensitive filter.
        """
        if column not in self.df.columns:
            print(f"❌ Invalid column: {column}")
            return pd.DataFrame()  # Return an empty DataFrame for invalid column

        # Filter rows where the value in the given column matches the search value
        filtered_data = self.df[self.df[column].astype(str).str.contains(value, case=False, na=False)]
        return filtered_data if not filtered_data.empty else pd.DataFrame([["No matching records found"]],
                                                                          columns=[column])

    def sort_records(self, columns, ascending):
        """
        Sort records based on one or more columns in ascending or descending order.
        """
        # Check if all the provided columns are valid
        invalid_columns = [col for col in columns if col not in self.df.columns]
        if invalid_columns:
            print(f"❌ Invalid column(s): {', '.join(invalid_columns)}")
            return self.df  # Return the DataFrame as it is in case of invalid columns

        # Sort the DataFrame based on the provided columns
        return self.df.sort_values(by=columns, ascending=ascending)

    def get_columns(self):
        """Return a list of available columns in the dataset."""
        return self.df.columns.tolist()

    def group_data(self, category_column, value_column):
        """
        Group data for visualization purposes.
        Groups by a category and sums the values in the specified value column.
        """
        if category_column not in self.df.columns or value_column not in self.df.columns:
            print(f"❌ Invalid column(s) selected: {category_column}, {value_column}")
            return None

        try:
            # Group data by category and sum the corresponding values
            grouped_data = self.df.groupby(category_column)[value_column].sum()
            return grouped_data if not grouped_data.empty else None
        except Exception as e:
            print(f"❌ Error while grouping data: {e}")
            return None


# View: Handles displaying output to the user
class CSVView:
    @staticmethod
    def display_dataframe(df):
        """Display the DataFrame in a readable format."""
        if df.empty:
            print("\n⚠️ No results found.")
        else:
            print(df.to_string(index=False))  # Print the DataFrame without row indices

    @staticmethod
    def display_chart(chart_data, chart_type, title):
        """
        Display a chart based on the provided data and chart type.
        Supports barh, bar, and pie charts.
        """
        if chart_data is None or chart_data.empty:
            print("⚠️ Cannot generate chart: No valid data available.")
            return

        plt.figure(figsize=(10, 6))  # Set the figure size for the chart
        try:
            # Plot the chart based on the user's selection
            if chart_type == "barh":
                chart_data.plot(kind="barh", color="pink")  # Horizontal bar chart
            elif chart_type == "bar":
                chart_data.plot(kind="bar", color="coral")  # Vertical bar chart
            elif chart_type == "pie":
                chart_data.plot(kind="pie", autopct='%1.1f%%', startangle=90, colormap='viridis')  # Pie chart

            plt.title(title)  # Set the title of the chart
            plt.show()  # Display the chart
        except Exception as e:
            print(f"⚠️ Error displaying chart: {e}")  # Handle any errors during chart creation


# Controller: Manages user interaction and ties together the model and view
class CSVController:
    def __init__(self, model, view):
        # Initialize the model (data handler) and view (output display)
        self.model = model
        self.view = view

    def run(self):
        """Main loop for displaying menu and handling user choices."""
        while True:
            # Display the menu options to the user
            print("\n📊 CSV Data Processing - Select an Option:")
            print("1. Filter Records")
            print("2. Sort Records")
            print("3. Generate Charts")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()

            # Handle user input for different operations
            if choice == "1":
                self.filter_records()  # Call method to filter records
            elif choice == "2":
                self.sort_records()  # Call method to sort records
            elif choice == "3":
                self.generate_chart()  # Call method to generate charts
            elif choice == "4":
                print("✅ Exiting program. Goodbye!")
                break  # Exit the program
            else:
                print("❌ Invalid choice. Please try again.")

    def filter_records(self):
        """Handles filtering logic"""
        # Display available columns and prompt user for filtering criteria
        print("\n🔍 Available Columns:", ", ".join(self.model.get_columns()))
        column = input("Enter column name to filter by: ").strip()
        value = input(f"Enter value to search in '{column}': ").strip()
        filtered_df = self.model.filter_records(column, value)
        self.view.display_dataframe(filtered_df)

    def sort_records(self):
        """Handles sorting logic"""
        # Display available columns and prompt user for sorting criteria
        print("\n📑 Available Columns:", ", ".join(self.model.get_columns()))
        columns = input("Enter columns to sort by (comma-separated): ").strip().split(',')
        columns = [col.strip() for col in columns]  # Strip any extra spaces
        ascending = input("Sort in ascending order? (yes/no): ").strip().lower() == "yes"
        sorted_df = self.model.sort_records(columns, ascending)
        self.view.display_dataframe(sorted_df)

    def generate_chart(self):
        """Handles chart generation logic"""
        # Display available columns and prompt user for charting data
        print("\n📈 Available Columns:", ", ".join(self.model.get_columns()))
        category
