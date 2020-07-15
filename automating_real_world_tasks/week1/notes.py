# from PIL import Image
# im = Image.open("bride.jpg")
# im.rotate(45).show()

# handbook -> https://pillow.readthedocs.io/en/stable/handbook/index.html

# 
print("Resizing image: ")
from PIL import Image
im = Image.open("IMG_5475.jpeg")
new_im = im.resize((640,480))
new_im.save("example_resize.jpg")
new_im.show()

# from PIL import Image
# im = Image("example.jpg")
# new_im = im.rotate(90)
# new_im.save("example_rotated.jpg")

# from PIL import Image
# im = Image("example.jpg")
# im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")