import os
import shutil

# 定义源目录路径
source_dir = r"D:\PythonExercise\case_20"

# 检查目录是否存在
if not os.path.exists(source_dir):
    print(f"❌ 错误：目录 '{source_dir}' 不存在！")
else:
    # 遍历目录下的所有文件
    for filename in os.listdir(source_dir):
        # 只处理 .py 文件
        if filename.endswith(".py"):
            source_file = os.path.join(source_dir, filename)

            # 新文件名：原名 + "_exercise"
            new_filename = filename.replace(".py", "_exercise.py")
            target_file = os.path.join(source_dir, new_filename)

            try:
                # 读取原文件内容
                with open(source_file, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                # 只保留前5行（如果文件少于5行，就全保留）
                content_to_write = lines[:5]

                # 写入新文件
                with open(target_file, 'w', encoding='utf-8') as f:
                    f.writelines(content_to_write)

                print(f"✅ 已生成: {filename} → {new_filename} (仅保留前5行)")

            except Exception as e:
                print(f"❌ 处理失败: {filename}, 错误: {e}")