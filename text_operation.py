import os

def list_files(directory, write_path):
    """获取指定目录下的所有文本文件，并写入汇总于单个文本

    Args:
        directory (str): 目标文本顶层目录路径
        write_path (str): 写入文本路径

    Returns:
        str: file_list
        str: text
    """
    file_list = []
    text = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    # return file_list
    for file_name in file_list:
        text += ("\n" + file_name + ":")
        with open(file_name, 'r') as file:
            text += file.read()
        text += "\n ''' \n"
    with open(write_path, 'w') as file:
        file.write(text)
    return file_list,text