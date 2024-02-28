import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# Load your data
file_path = './pyscripts/gps_test_gabgal.csv'  # Replace with the path to your CSV file
data = pd.read_csv(file_path)

# Calculate the most and least abundant scientific names and their counts
value_counts = data['scientific_name'].value_counts()
most_abundant = value_counts.idxmax()
least_abundant = value_counts.idxmin()
most_abundant_count = value_counts.max()
least_abundant_count = value_counts.min()

# Calculate the highest and lowest height for each scientific name
highest_height = data.groupby('scientific_name')['height'].max()
lowest_height = data.groupby('scientific_name')['height'].min()

# Calculate the highest and lowest width for each scientific name
highest_width = data.groupby('scientific_name')['width'].max()
lowest_width = data.groupby('scientific_name')['width'].min()

# Extracting the scientific names for the highest and lowest widths
highest_width_name = highest_width.idxmax()
lowest_width_name = lowest_width.idxmin()

# Calculate the highest and lowest carbon sequestration for each scientific name
highest_carbon_seq = data.groupby('scientific_name')['carbon_seq'].max()
lowest_carbon_seq = data.groupby('scientific_name')['carbon_seq'].min()

# Calculate the overall highest and lowest total carbon sequestration for each scientific name
total_carbon_seq = data.groupby('scientific_name')['carbon_seq'].sum()
highest_total_carbon_seq_name = total_carbon_seq.idxmax()
lowest_total_carbon_seq_name = total_carbon_seq.idxmin()

# Creating a summary table
summary_table = pd.DataFrame({
    "Statistic": ["Most Abundant", "Count (Most Abundant)", "Least Abundant", "Count (Least Abundant)", 
                  "Highest Height (Scientific Name)", "Height (Highest)", "Lowest Height (Scientific Name)", "Height (Lowest)",
                  "Highest Width (Scientific Name)", "Width (Highest)", "Lowest Width (Scientific Name)", "Width (Lowest)",
                  "Highest Carbon Seq (Scientific Name)", "Carbon Seq (Highest)", "Lowest Carbon Seq (Scientific Name)", "Carbon Seq (Lowest)",
                  "Highest Total Carbon Seq (Scientific Name)", "Total Carbon Seq (Highest)", "Lowest Total Carbon Seq (Scientific Name)", "Total Carbon Seq (Lowest)"],
    "Value": [most_abundant, most_abundant_count, least_abundant, least_abundant_count,
              highest_height.idxmax(), highest_height.max(), lowest_height.idxmin(), lowest_height.min(),
              highest_width_name, highest_width.max(), lowest_width_name, lowest_width.min(),
              highest_carbon_seq.idxmax(), highest_carbon_seq.max(), lowest_carbon_seq.idxmin(), lowest_carbon_seq.min(),
              highest_total_carbon_seq_name, total_carbon_seq.max(), lowest_total_carbon_seq_name, total_carbon_seq.min()]
})

# Exporting the summary table as a PNG file
fig, ax = plt.subplots(figsize=(6, 10))  # Adjust the figure size
ax.axis('off')

# Create and format the table
tbl = table(ax, summary_table, loc='center', cellLoc='center', rowLoc='center')
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.scale(1.2, 1.2)  # Adjust the scale
tbl.auto_set_column_width(col=list(range(len(summary_table.columns))))  # Adjust the column width

# Enhancing the visibility of the table borders by adjusting cell properties
for key, cell in tbl.get_celld().items():
    cell.set_linewidth(1.2)
    cell.set_edgecolor('black')

# Adjust layout
plt.tight_layout()

fig = plt.gcf()
plt.text(0.95, 0.05, '©️ NatureMark Systems 2024', 
        fontsize=25, color='black',
        ha='right', va='bottom', alpha=0.5,
        transform=fig.transFigure)


# Save the figure
plt.savefig('./pyscripts/summary_table.png', bbox_inches='tight', dpi=300)
#plt.show()

