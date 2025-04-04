import textwrap

import textwrap


class CSVView:
    @staticmethod
    def display_chart(chart_data, chart_type, title):
        if chart_data is None or chart_data.empty:
            print("⚠️ Cannot generate chart: No valid data available.")
            return

        labels = chart_data.index.tolist()
        values = chart_data.values.tolist()
        plt.close('all')
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = sns.color_palette("colorblind", len(labels))

        # Function to wrap long text labels
        def wrap_labels(labels, width=15):
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
                wrapped_labels = wrap_labels(labels, width=12
                                             )  # Adjust width for readability
                wedges, texts, autotexts = ax.pie(values, labels=wrapped_labels, autopct='%1.1f%%',
                                                  startangle=90, colors=colors,
                                                  textprops={'fontsize': 10, 'color': 'black'})

                # Adjust font weight for better visibility
                for text in texts + autotexts:
                    text.set_fontweight('bold')

                plt.axis("equal")  # Ensures the pie chart remains circular

                # Adjust layout to create more space
                plt.subplots_adjust(top=0.8)  # Moves the title higher
                ax.set_title(title, fontsize=16, fontweight='bold', color='black', pad=30)  # Adds extra padding

            plt.show()
        except Exception as e:
            print(f"⚠️ Error displaying chart: {e}")

