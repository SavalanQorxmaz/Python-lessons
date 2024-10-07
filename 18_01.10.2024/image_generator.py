from PIL import Image

# Open the image
image = Image.open('apple.jpg')

# Define the crop area (left, upper, right, lower)
crop_area = (0, 0, 200, 200)

# Crop the image
cropped_image = image.crop(crop_area)

if cropped_image.mode == 'RGBA':
    cropped_image = cropped_image.convert('RGB')

# Save the cropped image
cropped_image.save('result.jpg')

# Optionally, display the cropped image
cropped_image.show()