from PIL import Image
import os

size = 128, 128
files = os.listdir(r'H:\cs1034-team-project\practical-3\specification-2\img')

for f in files:
    fn, fext = os.path.splitext(f)
    im = Image.open(os.path.join(r'H:\cs1034-team-project\practical-3\specification-2\img', f))

    if fext != '.jpg':
        im = im.convert('RGB')

    im.thumbnail(size)
    file_path = os.path.join(r'H:\cs1034-team-project\practical-3\specification-2\thumbnail', fn)
    im.save(file_path + ".thumbnail", "JPEG")
