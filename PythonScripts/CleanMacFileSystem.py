import argparse
import os

import os

def delete_files_with_prefixes_recursively(directory, prefixes):
    # 遍历目录树
    for dirpath, dirnames, filenames in os.walk(directory):
        # 遍历当前目录中的所有文件
        for filename in filenames:
            # 检查文件名是否以Set中的某个前缀开头
            for prefix in prefixes:
                if filename.startswith(prefix):
                    # 构建文件的完整路径
                    file_path = os.path.join(dirpath, filename)
                    
                    # 尝试删除文件
                    try:
                        os.remove(file_path)
                        print(f"已删除文件: {file_path}")
                    except Exception as e:
                        print(f"无法删除文件 {file_path}: {e}")
                    # 既然已经找到匹配的前缀并删除了文件，就不需要再检查其他前缀了
                    break

prefix_set = { ".DS_Store", "._" };

def clean_mac_fileysystem(directory):
    delete_files_with_prefixes_recursively(directory, prefix_set);


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Clean mac filesystem.')
    parser.add_argument('--dir', required=True)
    args = parser.parse_args()

    clean_mac_fileysystem(args.dir)
