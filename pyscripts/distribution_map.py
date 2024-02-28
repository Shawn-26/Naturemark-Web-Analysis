import pandas as pd
import folium
import matplotlib.colors as mcolors
from selenium import webdriver
import time
import os
from PIL import Image, ImageDraw, ImageFont

def create_colormap(unique_values):
    colors = list(mcolors.TABLEAU_COLORS.values())  # Using Tableau's color scheme
    color_count = len(colors)
    colormap = {value: colors[i % color_count] for i, value in enumerate(unique_values)}
    return colormap

def plot_points_with_legend(map_obj, data, colormap, column_name):
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row['lat'], row['long']],
            radius=5,
            color=colormap[row[column_name]],
            fill=True,
            fill_color=colormap[row[column_name]],
            fill_opacity=0.7
        ).add_to(map_obj)

    legend_html = '''<div style="position: fixed; bottom: 50px; left: 50px; width: 240px; 
                    height: auto; background-color: white; border:2px solid grey; z-index:9999; 
                    padding: 5px;"><h4 style="margin-top: 0;">{}</h4>'''.format(column_name)
    for name, color in colormap.items():
        legend_html += '<i style="background: {}; width: 25px; height: 18px; margin-left: 20px; \
                        display: inline-block; vertical-align: middle;"></i> {}<br>'.format(color, name)
    legend_html += '</div>'
    map_obj.get_root().html.add_child(folium.Element(legend_html))

# # Load the dataset
# file_path = './pyscripts/gps_test_gabgal.csv'  # Replace with your dataset file path
# data = pd.read_csv(file_path)

# # Create a color map
# unique_scientific_names = data['scientific_name'].unique()
# scientific_name_colormap = create_colormap(unique_scientific_names)

# # Create the map centered around the average coordinates with a higher zoom level
# map_center = [data['lat'].mean(), data['long'].mean()]
# map_with_points = folium.Map(location=map_center, zoom_start=120)  # Increased zoom level

# # Plot points with a legend
# plot_points_with_legend(map_with_points, data, scientific_name_colormap, "scientific_name")

# # Save the map as HTML
# html_path = './pyscripts/diversity.html'
# map_with_points.save(html_path)

# # Set up Selenium WebDriver for Chromium
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run Chromium in headless mode (without a UI)
# options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
# options.add_argument('--window-size=2180x2180')  # Specify window size

# driver = webdriver.Chrome(options=options)

# # Load the HTML file
# full_html_path = 'file://' + os.path.abspath(html_path)
# driver.get(full_html_path)

# # Give it time to render and take a screenshot
# time.sleep(5)  # Adjust time as needed
# png_path = './pyscripts/diversity_map.png'
# driver.save_screenshot(png_path)

# # Close the browser
# driver.quit()

# Add copyright text to the image
# image = Image.open(png_path)
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype("arial.ttf", 45)  # Adjust font and size as needed
# draw.text((image.width - 650, image.height - 80), "©️ NatureMark Systems 2024", fill=(0, 0, 0), font=font)
# image.save(png_path)

def main(file_path):
    data = pd.read_csv(file_path)

    # Create a color map
    unique_scientific_names = data['scientific_name'].unique()
    scientific_name_colormap = create_colormap(unique_scientific_names)

    # Create the map centered around the average coordinates with a higher zoom level
    map_center = [data['lat'].mean(), data['long'].mean()]
    map_with_points = folium.Map(location=map_center, zoom_start=120)  # Increased zoom level

    # Plot points with a legend
    plot_points_with_legend(map_with_points, data, scientific_name_colormap, "scientific_name")

    # Save the map as HTML
    html_path = './pyscripts/diversity.html'
    map_with_points.save(html_path)

    # Set up Selenium WebDriver for Chromium
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chromium in headless mode (without a UI)
    options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    options.add_argument('--window-size=2180x2180')  # Specify window size

    driver = webdriver.Chrome(options=options)

    # Load the HTML file
    full_html_path = 'file://' + os.path.abspath(html_path)
    driver.get(full_html_path)

    # Give it time to render and take a screenshot
    time.sleep(5)  # Adjust time as needed
    png_path = './pyscripts/diversity_map.png'
    driver.save_screenshot(png_path)

    # Close the browser
    driver.quit()

    # Add copyright text to the image
    image = Image.open(png_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", 45)  # Adjust font and size as needed
    draw.text((image.width - 650, image.height - 80), "©️ NatureMark Systems 2024", fill=(0, 0, 0), font=font)
    image.save(png_path)
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python distribution_map.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])
