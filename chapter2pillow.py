from PIL import Image
from PIL import ImageFilter

# Memuat gambar
image = Image.open('bunga.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('chapter2pillow_result.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('chapter2pillow_result.jpg')

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('chapter2pillow_result.jpg')

# Menyimpan gambar hasil sebagai PNG tanpa perlu mengonversi mode warna
filtered_image.save('filteredChapter2_result.png')
# Jika gambar dalam mode RGBA, ubah menjadi RGB
if filtered_image.mode == 'RGBA':
    filtered_image = filtered_image.convert('RGB')

# Menyimpan gambar
image.save('Chapter2result.jpg')