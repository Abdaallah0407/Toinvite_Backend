import PIL
from PIL import Image

ADMIN = 1
CLIENT_USER = 2

USER_TYPE = [
    (ADMIN, 'Админ'),
    (CLIENT_USER, 'Пользователь'),
]


def image_compress(image, width_size, height_size):
    img = Image.open(image)
    width, height = img.size
    if width > width_size:
        ratio = float(width / width_size)
        width = int(width / ratio)
        height = int(height / ratio)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        img.save(image.path, quality=100, optimize=True)
    if height > height_size:
        ratio = float(height / height_size)
        height = int(height / ratio)
        width = int(width / ratio)
        img = img.resize((width, height), PIL.Image.ANTIALIAS)
        img.save(image.path, quality=100, optimize=True)
