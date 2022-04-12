import os
import sys
from io import BytesIO
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile

from toinvite_core import settings
from toinvite_core.settings import BASE_DIR


class ImageCompressorMixin(object):

    def compress(self, field, delete_source=False, max_width=1200, max_height=1200):
        image = getattr(self, field)
        img = Image.open(image)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # compress image only if size is less than 1200 px on one side
        if image and (image.width > max_width or image.height > max_height):
            width = image.width if image.width < max_width else max_width
            height = image.height if image.height < max_height else max_height
            img.thumbnail((width, height), Image.ANTIALIAS)
            self._add_watermark(img)

        else:
            self._add_watermark(img, small=True)

        output = BytesIO()
        img.save(output, format='JPEG', quality=70, optimize=True,
                 progressive=True)
        output.seek(0)

        new_image = InMemoryUploadedFile(
            output, 'ImageField',
            f"{image.name.split('.')[0]}.jpg",
            'image/jpeg', sys.getsizeof(output), None
        )

        if delete_source:
            image.delete(False)
        setattr(self, field, new_image)

    def compress_without_watermark(self, field, delete_source=False, max_width=1200, max_height=1200):
        image = getattr(self, field)
        img = Image.open(image)
        if img.mode != 'RGB':
            img = img.convert('RGB')

        # compress image only if size is less than 1200 px on one side
        if image and (image.width > max_width or image.height > max_height):
            width = image.width if image.width < max_width else max_width
            height = image.height if image.height < max_height else max_height
            img.thumbnail((width, height), Image.ANTIALIAS)

        output = BytesIO()
        img.save(output, format='JPEG', quality=70, optimize=True,
                 progressive=True)
        output.seek(0)

        new_image = InMemoryUploadedFile(
            output, 'ImageField',
            f"{image.name.split('.')[0]}.jpg",
            'image/jpeg', sys.getsizeof(output), None
        )

        if delete_source:
            image.delete(False)
        setattr(self, field, new_image)

    def _add_watermark(self, img, small=False):
        watermark = Image.open(settings.WATERMARK_IMG)

        iw, ih = img.size
        offset_x, offset_y = 60, 40

        if small:
            # resize watermark and it's offsets accordingly if img is small
            x, y = watermark.size
            ratio = iw / 1000
            offset_x, offset_y = round(60 * ratio), round(40 * ratio)
            watermark.thumbnail((x * ratio, y * ratio), Image.ANTIALIAS)

        ww, wh = watermark.size
        location = (iw - ww - offset_x, ih - wh - offset_y, iw - offset_x, ih - offset_y)
        img.paste(watermark, location, watermark)
