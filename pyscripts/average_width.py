# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your data
# file_path = './pyscripts/gps_test_gabgal.csv'
# data = pd.read_csv(file_path)

# # Calculating the average width for each Scientific_name
# average_heights = data.groupby('scientific_name')['width'].mean()

# # Create a bar graph for average widths
# plt.figure(figsize=(55, 40))  # Adjust the figure size as needed
# plt.bar(average_heights.index, average_heights, color='green')

# # Set font sizes
# title_font_size = 30  # Adjust the font size for the title
# axis_label_font_size = 34  # Adjust the font size for the axis labels
# axis_ticks_font_size = 26  # Adjust the font size for the axis ticks

# # Add labels and title with specified font sizes
# plt.xlabel('Scientific name', fontsize=axis_label_font_size)
# plt.ylabel('Average Width', fontsize=axis_label_font_size)
# plt.title('Average Tree Width', fontsize=title_font_size)

# # Rotate the X-axis labels for better readability and adjust font size
# plt.xticks(rotation=90, fontsize=axis_ticks_font_size)
# plt.yticks(fontsize=axis_ticks_font_size)  # Set the font size for Y-axis ticks

# # Adjust the subplot parameters to give some padding
# plt.subplots_adjust(bottom=0.3)
# # Adding Copyright Rights
# fig = plt.gcf()
# plt.text(0.95, 0.05, '©️ Nature Mark Systems 2024', 
#         fontsize=45, color='black',
#         ha='right', va='bottom', alpha=0.5,
#         transform=fig.transFigure)

# # Save the figure as a PNG file
# plt.savefig('./pyscripts/Tree_width.png')

# # Display the plot
# plt.show()

import sys
import pandas as pd
import matplotlib.pyplot as plt

def main(file_path):
    data = pd.read_csv(file_path)

    # Calculating the average width for each Scientific_name
    average_heights = data.groupby('scientific_name')['width'].mean()

    # Create a bar graph for average widths
    plt.figure(figsize=(55, 40))  # Adjust the figure size as needed
    plt.bar(average_heights.index, average_heights, color='green')

    # Set font sizes
    title_font_size = 30  # Adjust the font size for the title
    axis_label_font_size = 34  # Adjust the font size for the axis labels
    axis_ticks_font_size = 26  # Adjust the font size for the axis ticks

    # Add labels and title with specified font sizes
    plt.xlabel('Scientific name', fontsize=axis_label_font_size)
    plt.ylabel('Average Width', fontsize=axis_label_font_size)
    plt.title('Average Tree Width', fontsize=title_font_size)

    # Rotate the X-axis labels for better readability and adjust font size
    plt.xticks(rotation=90, fontsize=axis_ticks_font_size)
    plt.yticks(fontsize=axis_ticks_font_size)  # Set the font size for Y-axis ticks

    # Adjust the subplot parameters to give some padding
    plt.subplots_adjust(bottom=0.3)
    # Adding Copyright Rights
    fig = plt.gcf()
    plt.text(0.95, 0.05, '©️ NatureMark Systems 2024', 
            fontsize=45, color='black',
            ha='right', va='bottom', alpha=0.5,
            transform=fig.transFigure)

    # Save the figure as a PNG file
    plt.savefig('./pyscripts/Tree_width.png')
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python average_width.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])
