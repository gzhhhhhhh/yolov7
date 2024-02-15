import os
import shutil

def rename_images(folder_path):
    # 获取文件夹中所有文件的列表
    files = os.listdir(folder_path)

    # 仅筛选图像文件（您可以根据需要自定义扩展名）
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # 为每个图像文件重新命名
    for i, file in enumerate(image_files, start=1):
        # 构建新文件名
        new_name = f"{i}.{file.split('.')[-1].lower()}"

        # 构建完整的路径
        old_path = os.path.join(folder_path, file)
        new_path = os.path.join(folder_path, new_name)

        # 重命名文件
        shutil.move(old_path, new_path)
        print(f'已重命名：{old_path} -> {new_path}')

# 将 'your_folder_path' 替换为包含图像的文件夹的实际路径
folder_path = 'D:\yolov7\datasets\\textimages'
rename_images(folder_path)
