
import pandas as pd
import folium
from folium.plugins import HeatMap
from branca.colormap import LinearColormap
from selenium import webdriver
import time
import os
import sys
from PIL import Image, ImageDraw, ImageFont

def add_matching_gradient_legend_to_map(folium_map, title, vmin, vmax):
    colors = ['#B8860B', '#ADFF2F', '#008000', '#006400']  # dark golden to green
    colormap = LinearColormap(colors, vmin=vmin, vmax=vmax)
    colormap.caption = title
    folium_map.add_child(colormap)

# # Load the dataset
# file_path = './pyscripts/gps_test_gabgal.csv'  # Update this with the path to your dataset
# data = pd.read_csv(file_path)

# # Prepare data for the heatmap
# heat_data = [[row['lat'], row['long'], row['carbon_seq']] for index, row in data.iterrows()]

# # Determine the min and max values for carbon_seq
# min_carbon_seq = data['carbon_seq'].min()
# max_carbon_seq = data['carbon_seq'].max()

# # Create the map centered around the average coordinates with increased zoom level
# map_center = [data['lat'].mean(), data['long'].mean()]
# heatmap_map = folium.Map(location=map_center, zoom_start=120)

# # Add HeatMap to the map
# HeatMap(heat_data, min_opacity=0.5, max_val=max_carbon_seq, radius=15, blur=10, gradient={0: '#B8860B', 0.5: '#ADFF2F', 1: '#006400'}).add_to(heatmap_map)

# # Add the matching gradient legend to the map
# add_matching_gradient_legend_to_map(heatmap_map, 'Carbon Sequence Concentration', min_carbon_seq, max_carbon_seq)

# # Save the map as HTML
# html_path = './pyscripts/carbon_seq_gabgal.html'
# heatmap_map.save(html_path)

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
# png_path = './pyscripts/carbon_seq_gabgal.png'
# driver.save_screenshot(png_path)

# # Close the browser
# driver.quit()

# # Add copyright text to the image
# image = Image.open(png_path)
# draw = ImageDraw.Draw(image)
# font = ImageFont.truetype("arial.ttf", 45)  # Adjust font and size as needed
# draw.text((image.width - 650, image.height - 80), "©️ NatureMark Systems 2024", fill=(0, 0, 0), font=font)
# image.save(png_path)

def main(file_path):
    data = pd.read_csv(file_path)

    # Prepare data for the heatmap
    heat_data = [[row['lat'], row['long'], row['carbon_seq']] for index, row in data.iterrows()]

    # Determine the min and max values for carbon_seq
    min_carbon_seq = data['carbon_seq'].min()
    max_carbon_seq = data['carbon_seq'].max()

    # Create the map centered around the average coordinates with increased zoom level
    map_center = [data['lat'].mean(), data['long'].mean()]
    heatmap_map = folium.Map(location=map_center, zoom_start=120)

    # Add HeatMap to the map
    HeatMap(heat_data, min_opacity=0.5, max_val=max_carbon_seq, radius=15, blur=10, gradient={0: '#B8860B', 0.5: '#ADFF2F', 1: '#006400'}).add_to(heatmap_map)

    # Add the matching gradient legend to the map
    add_matching_gradient_legend_to_map(heatmap_map, 'Carbon Sequence Concentration', min_carbon_seq, max_carbon_seq)

    # Save the map as HTML
    html_path = './pyscripts/carbon_seq_gabgal.html'
    heatmap_map.save(html_path)

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
    png_path = './pyscripts/carbon_seq_gabgal.png'
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
        print("Usage: python heatmap_carbonseq.py <file_path>")
        sys.exit(1)
    main(sys.argv[1])