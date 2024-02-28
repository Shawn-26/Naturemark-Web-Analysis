import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import sys

# Function to adjust color brightness and saturation
def adjust_color_brightness_saturation(rgba_color, brightness_factor=0.8, saturation_factor=0.6):
    # Extract RGB components
    rgb_color = rgba_color[:3]

    # Convert RGB to HSV
    hsv_color = mcolors.rgb_to_hsv(rgb_color)

    # Adjust brightness (V channel)
    hsv_color[2] = np.clip(hsv_color[2] * brightness_factor, 0, 1)

    # Adjust saturation (S channel)
    hsv_color[1] = np.clip(hsv_color[1] * saturation_factor, 0, 1)

    # Convert back to RGB and recombine with alpha
    adjusted_rgb = mcolors.hsv_to_rgb(hsv_color)
    return (adjusted_rgb[0], adjusted_rgb[1], adjusted_rgb[2], rgba_color[3])

# # Load your data
# data = pd.read_csv('./pyscripts/gps_test_gabgal.csv')

# # Count the occurrences of each scientific name
# name_counts = data['scientific_name'].value_counts()

# # Combine tab20, tab20b, and tab20c
# tab20_combined = plt.cm.get_cmap('tab20', 20)
# tab20b_combined = plt.cm.get_cmap('tab20b', 20)
# tab20c_combined = plt.cm.get_cmap('tab20c', 20)

# # Creating a new combined color list
# combined_colors = list(tab20_combined.colors) + list(tab20b_combined.colors) + list(tab20c_combined.colors)

# # Adjust color brightness and saturation
# combined_colors = [adjust_color_brightness_saturation(color) for color in combined_colors]

# # Truncate or repeat the color list to match the number of categories
# num_categories = len(name_counts)
# if num_categories > len(combined_colors):
#     combined_colors = combined_colors * (num_categories // len(combined_colors) + 1)
# combined_colors = combined_colors[:num_categories]

# # Create the pie chart without internal percentage labels
# plt.figure(figsize=(30, 22))
# patches, texts = plt.pie(name_counts, colors=combined_colors, startangle=140)
# plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

# title_font_size = 34  # Adjust this value for the title font size
# plt.title('Distribution of Trees by Scientific Name', fontsize=title_font_size)

# # Calculate percentage and update legend labels
# percentages = [f'{p / sum(name_counts) * 100:.1f}%' for p in name_counts]
# legend_labels = [f'{name} - {percent}' for name, percent in zip(name_counts.index, percentages)]

# legend_font_size = 28  # Adjust this value for the legend items font size
# legend_title_font_size = 30  # Adjust this value for the legend title font size
# legend = plt.legend(patches, legend_labels, title="Scientific Names", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=legend_font_size)
# plt.setp(legend.get_title(), fontsize=legend_title_font_size)  # Set the font size of the legend title

# # Adjust the subplot parameters to give some padding
# plt.subplots_adjust(right=0.6)

# fig = plt.gcf()
# plt.text(0.95, 0.05, '©️ NatureMark Systems 2024', 
#         fontsize=45, color='black',
#         ha='right', va='bottom', alpha=0.5,
#         transform=fig.transFigure)

# # Save the figure as a PNG file
# plt.savefig('./pyscripts/Distribution.png')

# Display the plot
#plt.show()

def main(file_path):
    # Load your data
    data = pd.read_csv(file_path)

    # Count the occurrences of each scientific name
    name_counts = data['scientific_name'].value_counts()

    # Combine tab20, tab20b, and tab20c
    tab20_combined = plt.cm.get_cmap('tab20', 20)
    tab20b_combined = plt.cm.get_cmap('tab20b', 20)
    tab20c_combined = plt.cm.get_cmap('tab20c', 20)

    # Creating a new combined color list
    combined_colors = list(tab20_combined.colors) + list(tab20b_combined.colors) + list(tab20c_combined.colors)

    # Adjust color brightness and saturation
    combined_colors = [adjust_color_brightness_saturation(color) for color in combined_colors]

    # Truncate or repeat the color list to match the number of categories
    num_categories = len(name_counts)
    if num_categories > len(combined_colors):
        combined_colors = combined_colors * (num_categories // len(combined_colors) + 1)
    combined_colors = combined_colors[:num_categories]

    # Create the pie chart without internal percentage labels
    plt.figure(figsize=(30, 22))
    patches, texts = plt.pie(name_counts, colors=combined_colors, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.

    title_font_size = 34  # Adjust this value for the title font size
    plt.title('Distribution of Trees by Scientific Name', fontsize=title_font_size)

    # Calculate percentage and update legend labels
    percentages = [f'{p / sum(name_counts) * 100:.1f}%' for p in name_counts]
    legend_labels = [f'{name} - {percent}' for name, percent in zip(name_counts.index, percentages)]

    legend_font_size = 28  # Adjust this value for the legend items font size
    legend_title_font_size = 30  # Adjust this value for the legend title font size
    legend = plt.legend(patches, legend_labels, title="Scientific Names", loc="center left", bbox_to_anchor=(1, 0.5), fontsize=legend_font_size)
    plt.setp(legend.get_title(), fontsize=legend_title_font_size)  # Set the font size of the legend title

    # Adjust the subplot parameters to give some padding
    plt.subplots_adjust(right=0.6)

    fig = plt.gcf()
    plt.text(0.95, 0.05, '©️ NatureMark Systems 2024', 
            fontsize=45, color='black',
            ha='right', va='bottom', alpha=0.5,
            transform=fig.transFigure)

    # Save the figure as a PNG file
    plt.savefig('./pyscripts/Distribution.png')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pie_diversity.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])
