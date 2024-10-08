from PIL import Image, ImageFilter, ImageEnhance, ImageOps

# Open the image
image = Image.open('naturmort.jpg')

# # Define the crop area (left, upper, right, lower)
# crop_area = (0, 0, 200, 200)

# # Crop the image
# cropped_image = image.crop(crop_area)

# if cropped_image.mode == 'RGBA':
#     cropped_image = cropped_image.convert('RGB')

# # Save the cropped image
# cropped_image.save('result.jpg')

# Optionally, display the cropped image
# cropped_image.show()
# image.show()

try:  
    original = Image.open("naturmort.jpg")  
except FileNotFoundError:  
    print("Файл не найден")
print("Размер изображения:")  
print(original.format, original.size, original.mode)
blurred = original.filter(ImageFilter.CONTOUR)
# открываем оригинал и размытое изображение
# blurred.show()
# size = (100, 100)
# original.thumbnail(size)
# original.show()

box = (100, 100, 400, 400)
region = original.crop(box)
def roll(im, delta):
    """Roll an image sideways."""
    xsize, ysize = im.size

    delta = delta % xsize
    if delta == 0:
        return im

    part1 = im.crop((0, 0, delta, ysize))
    part2 = im.crop((delta, 0, xsize, ysize))
    im.paste(part1, (xsize - delta, 0, xsize, ysize))
    im.paste(part2, (0, 0, xsize - delta, ysize))

    return im
# roll(original, 100)

# region = region.transpose(Image.Transpose.ROTATE_180)
# original.paste(region, box)

# r, g, b = original.split()
# original = Image.merge("RGB", ( g, b, r))
# print(r, g, b)
# rot = original.rotate(45)
# out = original.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
# out = original.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
# multiply each pixel by 1.2
out = original.point(lambda i: i * 100)
# out.save('ot.jpg')
# out = original.transpose(Image.Transpose.ROTATE_90)
# out = original.transpose(Image.Transpose.ROTATE_180)
# out = original.transpose(Image.Transpose.ROTATE_270)
# out.show()

# from PIL import Image, ImageOps
size = (100, 150)
with Image.open("naturmort.jpg") as im:
    # ImageOps.contain(im, size).save("imageops_contain.webp")
    # ImageOps.cover(im, size).save("imageops_cover.webp")
    # ImageOps.fit(im, size).save("imageops_fit.webp")
    # ImageOps.pad(im, size, color="#f00").save("imageops_pad.webp")

    # thumbnail() can also be used,
    # but will modify the image object in place
    im.thumbnail(size)
    # im.save("image_thumbnail.webp")
    
    # split the image into individual bands
source = original.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
im = Image.merge(im.mode, source)

enh = ImageEnhance.Contrast(im)
enh.enhance(1.3).show("30% more contrast")
enh.show()