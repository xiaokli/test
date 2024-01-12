from PIL import Image

im = Image.open("/workspaces/test/resources/20211112_125229.jpg.thumb.jpg")
print(im.format, im.size, im.mode)
print("original =", im.mode, im.size)

im.draft("L", (100, 100))
print("draft =", im.mode, im.size)