from PIL import Image, ImageDraw, ImageFont
import pandas as pd
from datetime import datetime
import os

A4_SIZE = (2480, 3508)  # A4 size in pixels at 300 DPI

def add_text_to_a4_image(image_path, location, start_date, end_date, duration, output_path):
    # Open the original image
    original_img = Image.open(image_path)

    # Resize original image to fit within A4 size, maintaining aspect ratio
    original_img.thumbnail((A4_SIZE[0], A4_SIZE[1] - 600), Image.Resampling.LANCZOS)  # Leave space for text

    # Create an A4 size image with white background
    img = Image.new('RGB', A4_SIZE, 'white')
    img_w, img_h = img.size

    # Calculate position to paste the original image (centered)
    paste_x = (img_w - original_img.width) // 2
    paste_y = (img_h - original_img.height - 600) // 2  # Leave space at the bottom for text
    img.paste(original_img, (paste_x, paste_y))

    # Set font
    font_size = 60
    font_path = "C:\\Windows\\Fonts\\arial.ttf"
    if not os.path.exists(font_path):
        font_path = "arial.ttf"  # Fallback to a default font
    font = ImageFont.truetype(font_path, size=font_size)

    # Prepare and draw text
    draw = ImageDraw.Draw(img)
    text_top = f"   Location: {location}                                Start-Date: {start_date}"
    text_bottom = f"   Duration: {duration}                                      End-Date: {end_date}"
    text_y = img_h - 550  # Position for text

    draw.text((50, text_y), text_top, font=font, fill="black")
    draw.text((50, text_y + font_size + 10), text_bottom, font=font, fill="black")

    # Save the new image
    img.save(output_path)

def calculate_dates_and_location(csv_file):
    # Read CSV file
    data = pd.read_csv(csv_file)

    # Get location (assuming it's the same for all rows)
    location = data['Location'].iloc[0]

    # Convert 'date' column to datetime
    start_date = datetime.strptime(data['Date'].min(), '%d-%m-%y')
    end_date = datetime.strptime(data['Date'].max(), '%d-%m-%y')

    # Calculate duration
    duration = end_date - start_date
    return location, start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'), f"{duration.days} days"

# File paths and names
csv_file = './gps_test9.csv'  # Replace with your CSV file path
image_file = 'Front.png'  # Replace with your PNG image path
output_image_file = 'output_image_a4_size.png'

# Calculate dates and location from CSV
location, start_date, end_date, duration_days = calculate_dates_and_location(csv_file)

# Add text to the A4-sized image and save as new PNG
add_text_to_a4_image(image_file, location, start_date, end_date, duration_days, output_image_file)

print(f"A4 size image with text saved as {output_image_file}")
