# encoding:utf-8
# @作者: 2019014715孔光辉
# @类型: 课程设计
from basicOperation import info

# 文件保存路径
path = '.\\student.txt'


# 保存学生信息
def saveInfo():
    # 追加写入
    with open(path, 'a', encoding='utf-8') as f:
        for dic in info:
            f.write(f'姓名:{dic["name"]:<4}\t学号:{dic["number"]:<10}\t年龄:{dic["age"]:<3}\t成绩:{dic["score"]}\n')
            # 已经添加到文件的学生信息从列表删除
        info.clear()

    print("学生信息保存成功!!")


# 读取文件内容
def readFile():
    import re

    print("===文件内容显示===")
    with open(path, 'r', encoding='utf-8') as f:
        f = f.readlines()
        if not f:
            print("文件数据为空!!!")
            return
        for rl in f:
            print(rl.strip())  # 打印内容
            # 把读取信息加入列表中
            dic = {'name': re.search(r'姓名:(.*?)\t', rl).group(1).strip(),
                   'number': re.search(r'学号:(\d+)', rl).group(1),
                   'age': re.search(r'年龄:(\d+)', rl).group(1),
                   'score': re.search(r'成绩:(\d+)', rl).group(1)}
            info.append(dic)
    clearFile()  # 清空文件内容


# 清空文件内容
def clearFile():
    with open(path, 'w', encoding='utf-8') as f:
        f.truncate()
    print("student.txt文件己清空!!!")

'''
姓名:张三  	学号:2019014809	年龄:19	成绩:98
姓名:李四  	学号:2019014811	年龄:20	成绩:66
姓名:孔光辉 	学号:2019014715	年龄:22	成绩:99
'''