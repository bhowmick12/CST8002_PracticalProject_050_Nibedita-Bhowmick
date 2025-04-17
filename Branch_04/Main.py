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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import textwrap

class CSVModel:
    """
    Model class that handles loading, filtering, sorting, and grouping CSV data.
    """

    def __init__(self, file_path):
        """
        Initialize the model with the provided CSV file path.

        Parameters:
        file_path (str): Path to the CSV file.

        Raises:
        FileNotFoundError: If the file does not exist at the given path.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def filter_records(self, column, value):
        """
        Filter records in the dataframe by matching a value in a specific column.

        Parameters:
        column (str): The column to filter by.
        value (str): The value to search for.

        Returns:
        DataFrame: Filtered records or a message if no match found.
        """
        if column not in self.df.columns:
            print(f"❌ Invalid column: {column}")
            return pd.DataFrame()
        filtered_data = self.df[self.df[column].astype(str).str.contains(value, case=False, na=False)]
        return filtered_data if not filtered_data.empty else pd.DataFrame([["No matching records found"]], columns=[column])

    def sort_records(self, columns, ascending):
        """
        Sort the dataframe based on specified columns.

        Parameters:
        columns (list): List of column names to sort by.
        ascending (bool): Whether to sort in ascending order.

        Returns:
        DataFrame: Sorted dataframe.
        """
        invalid_columns = [col for col in columns if col not in self.df.columns]
        if invalid_columns:
            print(f"❌ Invalid column(s): {', '.join(invalid_columns)}")
            return self.df
        return self.df.sort_values(by=columns, ascending=ascending)

    def get_columns(self):
        """
        Get a list of all column names in the dataframe.

        Returns:
        list: Column names.
        """
        return self.df.columns.tolist()

    def group_data(self, category_column, value_column):
        """
        Group data by a category column and sum the values in a value column.

        Parameters:
        category_column (str): Column to group by.
        value_column (str): Column containing numeric values.

        Returns:
        Series or None: Grouped data or None if error or empty result.
        """
        if category_column not in self.df.columns or value_column not in self.df.columns:
            print(f"❌ Invalid column(s) selected: {category_column}, {value_column}")
            return None
        try:
            grouped_data = self.df.groupby(category_column)[value_column].sum()
            return grouped_data if not grouped_data.empty else None
        except Exception as e:
            print(f"❌ Error while grouping data: {e}")
            return None


class CSVView:
    """
    View class responsible for rendering visualizations like bar and pie charts.
    """

    @staticmethod
    def display_chart(chart_data, chart_type, title):
        """
        Display a chart based on the given data and chart type.

        Parameters:
        chart_data (Series): Grouped data with category labels and values.
        chart_type (str): Type of chart to generate (barh, bar, pie).
        title (str): Title of the chart.
        """
        if chart_data is None or chart_data.empty:
            print("⚠️ Cannot generate chart: No valid data available.")
            return

        labels = chart_data.index.tolist()
        values = chart_data.values.tolist()
        plt.close('all')
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = sns.color_palette("colorblind", len(labels))

        def wrap_labels(labels, width=15):
            """
            Wrap long text labels to fit within chart space.

            Parameters:
            labels (list): List of label strings.
            width (int): Max characters per line.

            Returns:
            list: Wrapped labels.
            """
            return ['\n'.join(textwrap.wrap(label, width)) if isinstance(label, str) else label for label in labels]

        try:
            if chart_type == "barh":
                wrapped_labels = wrap_labels(labels)
                plt.barh(wrapped_labels, values, color=colors)
                plt.xlabel("Count", fontsize=14, fontweight='bold', color='black')
                plt.ylabel("Categories", fontsize=14, fontweight='bold', color='black')
            elif chart_type == "bar":
                wrapped_labels = wrap_labels(labels)
                plt.bar(wrapped_labels, values, color=colors)
                plt.xlabel("Categories", fontsize=14, fontweight='bold', color='black')
                plt.ylabel("Count", fontsize=14, fontweight='bold', color='black')
            elif chart_type == "pie":
                wrapped_labels = wrap_labels(labels, width=12)
                wedges, texts, autotexts = ax.pie(
                    values, labels=wrapped_labels, autopct='%1.1f%%',
                    startangle=90, colors=colors,
                    textprops={'fontsize': 10, 'color': 'black'}
                )
                for text in texts + autotexts:
                    text.set_fontweight('bold')
                plt.axis("equal")
                plt.subplots_adjust(top=0.8)
                ax.set_title(title, fontsize=16, fontweight='bold', color='black', pad=30)

            plt.show()
        except Exception as e:
            print(f"⚠️ Error displaying chart: {e}")


class CSVController:
    """
    Controller class that connects the model and view, and handles user interaction.
    """

    def __init__(self, model, view):
        """
        Initialize the controller with model and view instances.

        Parameters:
        model (CSVModel): The data model.
        view (CSVView): The visualization view.
        """
        self.model = model
        self.view = view

    def run(self):
        """
        Run the main interaction loop for the program.
        """
        while True:
            print("\n📊 CSV Data Processing - Select an Option:")
            print("1. Filter Records")
            print("2. Sort Records")
            print("3. Generate Charts")
            print("4. Exit")
            choice = input("Enter your choice: ").strip()
            if choice == "1":
                self.filter_records()
            elif choice == "2":
                self.sort_records()
            elif choice == "3":
                self.generate_chart()
            elif choice == "4":
                print("✅ Exiting program. Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please try again.")

    def filter_records(self):
        """
        Prompt user for filtering parameters and display filtered data.
        """
        print("\n🔍 Available Columns:", ", ".join(self.model.get_columns()))
        column = input("Enter column name to filter by: ").strip()
        value = input(f"Enter value to search in '{column}': ").strip()
        filtered_df = self.model.filter_records(column, value)
        print(filtered_df)

    def sort_records(self):
        """
        Prompt user for sorting columns and display sorted data.
        """
        print("\n📑 Available Columns:", ", ".join(self.model.get_columns()))
        columns = input("Enter columns to sort by (comma-separated): ").strip().split(',')
        columns = [col.strip() for col in columns]
        ascending = input("Sort in ascending order? (yes/no): ").strip().lower() == "yes"
        sorted_df = self.model.sort_records(columns, ascending)
        print(sorted_df)

    def generate_chart(self):
        """
        Prompt user to select chart parameters and generate a chart.
        """
        print("\n📈 Available Columns:", ", ".join(self.model.get_columns()))
        category_column = input("Enter column for categories: ").strip()
        value_column = input("Enter column for values: ").strip()
        print("\nChoose Chart Type:")
        print("1. Horizontal Bar Chart")
        print("2. Vertical Bar Chart")
        print("3. Pie Chart")
        chart_choice = input("Enter your choice: ").strip()
        chart_data = self.model.group_data(category_column, value_column)
        chart_types = {"1": "barh", "2": "bar", "3": "pie"}
        if chart_choice not in chart_types:
            print("❌ Invalid choice. Defaulting to Vertical Bar Chart.")
            chart_choice = "2"
        self.view.display_chart(chart_data, chart_types[chart_choice], f"{category_column} vs {value_column}")


if __name__ == "__main__":
    # Modify file path as needed
    file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test_03.csv"
    # file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test01.csv"
    # file_path = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"

    try:
        model = CSVModel(file_path)
        view = CSVView()
        controller = CSVController(model, view)
        controller.run()
    except FileNotFoundError as e:
        print(e)
