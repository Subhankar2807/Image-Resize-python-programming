from PIL import Image
filename=input()
image_path = "./ Enter the photo path"

width = int(input("Enter the Width:"))
height = int(input("Enter the height:"))

image = Image.open(image_path)


new_size =(width, height)

resized_image = image.resize(new_size)

resized_image.save("Resize_image.JPG")

resized_image.show()

