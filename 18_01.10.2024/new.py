# from PIL import Image

# # Open the main image
# image = Image.open('apple.jpg')
# w, h = image.size
# # Open the thumbnail image
# thumbnail = Image.open('thumbnail.jpg')

# # Resize the thumbnail to a smaller size if needed
# thumbnail.thumbnail((100, 100))  # Adjust the size as needed

# if image.mode == 'RGBA':
#     image = image.convert('RGB')

# # Calculate the position to paste the thumbnail (right bottom corner)
# x = image.width - thumbnail.width
# y = image.height - thumbnail.height

# # Paste the thumbnail onto the main image
# image.paste(thumbnail, (x, y), thumbnail if thumbnail.mode == 'RGBA' else None)

# # Save the resulting image
# image.save('output_image_with_thumbnail.jpg')

# # Optionally, display the final image
# image.show()