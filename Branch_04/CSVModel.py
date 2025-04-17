# Model: Handles data loading and processing
class CSVModel:
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")
        self.file_path = file_path
        self.df = pd.read_csv(file_path)

    def filter_records(self, column, value):
        if column not in self.df.columns:
            print(f"❌ Invalid column: {column}")
            return pd.DataFrame()
        filtered_data = self.df[self.df[column].astype(str).str.contains(value, case=False, na=False)]
        return filtered_data if not filtered_data.empty else pd.DataFrame([["No matching records found"]], columns=[column])

    def sort_records(self, columns, ascending):
        invalid_columns = [col for col in columns if col not in self.df.columns]
        if invalid_columns:
            print(f"❌ Invalid column(s): {', '.join(invalid_columns)}")
            return self.df
        return self.df.sort_values(by=columns, ascending=ascending)

    def get_columns(self):
        return self.df.columns.tolist()

    def group_data(self, category_column, value_column):
        if category_column not in self.df.columns or value_column not in self.df.columns:
            print(f"❌ Invalid column(s) selected: {category_column}, {value_column}")
            return None
        try:
            grouped_data = self.df.groupby(category_column)[value_column].sum()
            return grouped_data if not grouped_data.empty else None
        except Exception as e:
            print(f"❌ Error while grouping data: {e}")
            return None
