# @File  : countLine.py
# @Author: Zeng Yixuan
# @Date  :  2019/11/29
def countLine(filepath):
    count = 0
    with open(filepath, 'r') as file:
        for line in file.readlines():
            if(line.strip()):
                count += 1
    return count

def writeUser(filepath,name,id):
    """
    文件的写入   a+:指针最后文本的追加
    :param filepath:
    :param name:
    :param id:
    :return:
    """
    with open(filepath,'a+') as file:
        file.write(name + "*" + id+"\n")
