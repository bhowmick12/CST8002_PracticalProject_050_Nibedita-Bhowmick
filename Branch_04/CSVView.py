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
