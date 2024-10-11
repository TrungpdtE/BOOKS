from PIL import Image

# Mo file anh
image = Image.open('image.jpg')
# Chuyen anh sang che do RGB
image = image.convert('RGB')

# Tai du lieu pixel
pixels = image.load()

# Lay kich thuoc cua anh
width, height = image.size

# Duyet qua tung pixel
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        # Neu gia tri RGB cua pixel nho hon hoac bang 30, doi thanh mau trang
        if r <= 30 and g <= 30 and b <= 30:
            pixels[x, y] = (255, 255, 255)
        # Neu gia tri RGB cua pixel lon hon 30, doi thanh mau den
        else:
            pixels[x, y] = (0, 0, 0)

# Luu anh da sua doi
image.save('image_modified.png')