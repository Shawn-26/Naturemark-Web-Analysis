# import pandas as pd
# import matplotlib.pyplot as plt

# # Load your data
# file_path = './scripts/gps_test_gabgal.csv'
# data = pd.read_csv(file_path)

# # Calculating the average height for each scientific_name
# average_heights = data.groupby('scientific_name')['height'].mean()

# # Create a bar graph for average heights
# plt.figure(figsize=(55, 40))  # Adjust the figure size as needed
# plt.bar(average_heights.index, average_heights, color='maroon')

# # Set font sizes
# title_font_size = 30  # Adjust the font size for the title
# axis_label_font_size = 24  # Adjust the font size for the axis labels
# axis_ticks_font_size = 36  # Adjust the font size for the axis ticks

# # Add labels and title with specified font sizes
# plt.xlabel('Scientific name', fontsize=axis_label_font_size)
# plt.ylabel('Average Height', fontsize=axis_label_font_size)
# plt.title('Average Tree Height', fontsize=title_font_size)

# # Adjust the X-axis labels for better readability and font size
# plt.xticks(rotation=90, fontsize=axis_ticks_font_size)  # Set font size here
# plt.yticks(fontsize=axis_ticks_font_size)  # Set the font size for Y-axis ticks as well

# # Adjust the subplot parameters to give some padding
# plt.subplots_adjust(bottom=0.3)

# # Save the figure as a PNG file
# plt.savefig('./scripts/Tree_height.png')

# # Display the plot
# # plt.show()
import sys
import pandas as pd
import matplotlib.pyplot as plt

def main(file_path):
    # Load your data
    data = pd.read_csv(file_path)

    # Calculating the average height for each scientific_name
    average_heights = data.groupby('scientific_name')['height'].mean()

    # Create a bar graph for average heights
    plt.figure(figsize=(55, 40))  # Adjust the figure size as needed
    plt.bar(average_heights.index, average_heights, color='maroon')

    # Set font sizes
    title_font_size = 30  # Adjust the font size for the title
    axis_label_font_size = 24  # Adjust the font size for the axis labels
    axis_ticks_font_size = 36  # Adjust the font size for the axis ticks

    # Add labels and title with specified font sizes
    plt.xlabel('Scientific name', fontsize=axis_label_font_size)
    plt.ylabel('Average Height', fontsize=axis_label_font_size)
    plt.title('Average Tree Height', fontsize=title_font_size)

    # Adjust the X-axis labels for better readability and font size
    plt.xticks(rotation=90, fontsize=axis_ticks_font_size)  # Set font size here
    plt.yticks(fontsize=axis_ticks_font_size)  # Set the font size for Y-axis ticks as well

    # Adjust the subplot parameters to give some padding
    plt.subplots_adjust(bottom=0.3)
    
    # Adding Copyright Rights
    fig = plt.gcf()
    plt.text(0.95, 0.05, '©️ NatureMark Systems 2024', 
         fontsize=45, color='black',
         ha='right', va='bottom', alpha=0.5,
         transform=fig.transFigure)

    # Save the figure as a PNG file
    plt.savefig('./pyscripts/Tree_height.png')

    # Display the plot
    # plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python average_height.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])
