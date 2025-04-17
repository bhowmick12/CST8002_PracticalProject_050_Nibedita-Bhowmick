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
        print("\n🔍 Available Columns:", ", ".join(self.model.get_columns()))
        column = input("Enter column name to filter by: ").strip()
        value = input(f"Enter value to search in '{column}': ").strip()
        filtered_df = self.model.filter_records(column, value)
        print(filtered_df)

    def sort_records(self):
        print("\n📑 Available Columns:", ", ".join(self.model.get_columns()))
        columns = input("Enter columns to sort by (comma-separated): ").strip().split(',')
        columns = [col.strip() for col in columns]
        ascending = input("Sort in ascending order? (yes/no): ").strip().lower() == "yes"
        sorted_df = self.model.sort_records(columns, ascending)
        print(sorted_df)

    def generate_chart(self):
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
