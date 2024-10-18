from PIL import Image, ImageFilter

filename_dog = "dog.jpg"

with Image.open(filename_dog) as dog:
    dog.load()
print(dog.size)


dog = dog.crop((300, 0, 1280, 854))
# dog.show()

dog_gray = dog.convert("L")
# dog_gray.show()
# threshold = 80
# dog_threshold = dog_gray.point(
#     lambda x: 0 if x > threshold else 255
# )
# dog_threshold.show()

red, green, blue = dog.split()
# red.show()
# green.show()
# blue.show()
threshold = 50
dog_threshold = red.point(lambda x: 0 if x > threshold else 255)
dog_threshold = dog_threshold.convert("1")
# dog_threshold.show()

def erode(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MinFilter(1))
    return image


def dilate(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MaxFilter(1))
    return image

step_1 = erode(18, dog_threshold)
# step_1.show()

step_2 = dilate(8, step_1)
# step_2.show()

dog_mask = erode(45, step_2)
# dog_mask.show()

dog_mask = dog_mask.convert("L")
dog_mask = dog_mask.filter(ImageFilter.BoxBlur(20))
# dog_mask.show()

blank = dog.point(lambda _: 0)
dog_segmented = Image.composite(dog, blank, dog_mask)
# dog_segmented.show()

filename_agac = "agac.jpg"
with Image.open(filename_agac) as agac:
    agac.load()
print(agac.size)
agac.paste(
    dog.resize((dog.width // 5, dog.height // 5)),
    (400, 200),
    dog_mask.resize((dog_mask.width // 5, dog_mask.height // 5)),
)

agac.show()