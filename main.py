import os
from PIL import Image

input_folder_path = r"C:\Users\Lakindu Perera\Desktop\Poto"
output_folder_path = r"C:\Users\Lakindu Perera\Desktop\Poto\New folder"

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

for filename in os.listdir(input_folder_path):
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        with Image.open(os.path.join(input_folder_path, filename)) as img:
            width, height = img.size
            half_width = width // 2
            left_img = img.crop((0, 0, half_width, height))
            right_img = img.crop((half_width, 0, width, height))
            left_img.save(os.path.join(output_folder_path, f"left_{filename}"))
            right_img.save(os.path.join(output_folder_path, f"right_{filename}"))
