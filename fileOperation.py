# encoding:utf-8
import basicOperation  # 导入基本操作模块

# 文件保存路径
path = '.\\student.txt'


# 保存学生信息
def saveInfo():
    with open(path, 'a', encoding='utf-8') as f:
        for dic in basicOperation.info:
            f.write('姓名:{}\t学号:{}\t年龄:{}\t成绩:{}\n'.format(dic['name'], dic['number'], dic['age'], dic['score']))


# 读取文件内容
def readFile():
    with open(path, 'r', encoding='utf-8') as f:
        for rl in f.readlines():
            print(rl)


# 清空文件内容
def clearFile():
    with open(path, 'w', encoding='utf-8') as f:
        f.truncate()

