import pandas as pd
import matplotlib.pyplot as plt
import os
# Model: Handles data loading and processing
class CSVModel:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")

        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def filter_records(self, column, value):
        """Filter records based on user input."""
        if column not in self.df.columns:
            print(f"❌ Invalid column: {column}")
            return pd.DataFrame()

        filtered_data = self.df[self.df[column].astype(str).str.contains(value, case=False, na=False)]
        return filtered_data if not filtered_data.empty else pd.DataFrame([["No matching records found"]],
                                                                          columns=[column])

    def sort_records(self, columns, ascending):
        """Sort records based on multiple columns."""
        invalid_columns = [col for col in columns if col not in self.df.columns]
        if invalid_columns:
            print(f"❌ Invalid column(s): {', '.join(invalid_columns)}")
            return self.df

        return self.df.sort_values(by=columns, ascending=ascending)

    def get_columns(self):
        """Returns a list of available columns in the dataset."""
        return self.df.columns.tolist()

    def group_data(self, category_column, value_column):
        """Group data for visualization purposes."""
        if category_column not in self.df.columns or value_column not in self.df.columns:
            print(f"❌ Invalid column(s) selected: {category_column}, {value_column}")
            return None

        try:
            grouped_data = self.df.groupby(category_column)[value_column].sum()
            return grouped_data if not grouped_data.empty else None
        except Exception as e:
            print(f"❌ Error while grouping data: {e}")
            return None


# View: Handles displaying output
class CSVView:
    @staticmethod
    def display_dataframe(df):
        """Displays DataFrame in a readable format."""
        if df.empty:
            print("\n⚠️ No results found.")
        else:
            print(df.to_string(index=False))

    @staticmethod
    def display_chart(chart_data, chart_type, title):
        """Displays the selected chart."""
        if chart_data is None or chart_data.empty:
            print("⚠️ Cannot generate chart: No valid data available.")
            return

        plt.figure(figsize=(10, 6))
        try:
            if chart_type == "barh":
                chart_data.plot(kind="barh", color="skyblue")
            elif chart_type == "bar":
                chart_data.plot(kind="bar", color="coral")
            elif chart_type == "pie":
                chart_data.plot(kind="pie", autopct='%1.1f%%', startangle=90, colormap='viridis')

            plt.title(title)
            plt.show()
        except Exception as e:
            print(f"⚠️ Error displaying chart: {e}")


# Controller: Manages user interaction
class CSVController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def run(self):
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
        """Handles filtering logic"""
        print("\n🔍 Available Columns:", ", ".join(self.model.get_columns()))
        column = input("Enter column name to filter by: ").strip()
        value = input(f"Enter value to search in '{column}': ").strip()
        filtered_df = self.model.filter_records(column, value)
        self.view.display_dataframe(filtered_df)

    def sort_records(self):
        """Handles sorting logic"""
        print("\n📑 Available Columns:", ", ".join(self.model.get_columns()))
        columns = input("Enter columns to sort by (comma-separated): ").strip().split(',')
        columns = [col.strip() for col in columns]
        ascending = input("Sort in ascending order? (yes/no): ").strip().lower() == "yes"
        sorted_df = self.model.sort_records(columns, ascending)
        self.view.display_dataframe(sorted_df)

    def generate_chart(self):
        """Handles visualization logic"""
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




# Main Program Execution
if __name__ == "__main__":


    # file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test01.csv"
    file_path = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"
    # file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test_03.csv"
    try:
        model = CSVModel(file_path)
        view = CSVView()
        controller = CSVController(model, view)
        controller.run()
    except FileNotFoundError as e:
        print(e)
