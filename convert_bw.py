# convert_bw.py

# Import Image module from PIL
from PIL import Image

# Load the color image
img = Image.open('C:\\Users\\lenovo\\Music\\pic.jfif')

# Convert the image to black and white (grayscale)
bw = img.convert("L")

# Show the black and white image
bw.show()
