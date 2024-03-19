import os

def list_files(directory):
    """
    递归列出指定目录及其子目录下的所有文件名,并获取所有文本,生成all.txt
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
    with open("all.txt", 'w') as file:
        file.write(text)
    return file_list,text