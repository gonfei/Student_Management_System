# encoding:utf-8
# @作者: 2019014715孔光辉
# @类型: 课程设计

info = []


# 显示选项信息
def menu():
    print('=======欢迎来到学生管理系统======')
    print("0)\t显示功能菜单。")
    print("1)\t添加学生信息。")
    print("2)\t显示所有学生信息。")
    print("3)\t修改学生信息。")
    print("4)\t删除学生信息。")
    print("5)\t按学生成绩高-低显示学生信息。")
    print("6)\t按学生成绩低-高显示学生信息。")
    print("7)\t按学生年龄高-低显示学生信息。")
    print("8)\t按学生年龄低-高显示学生信息。")
    print("9)\t保存学生信息到文件(student.txt)。")
    print("10)\t从文件中读取数据(student.txt)。")
    print("11)\t清空学生信息文件(student.txt)。")
    print("12)\t退出: 按任意键退出。。。")


# 添加学生信息
def addStu():
    print('===欢迎使用添加学生信息功能===')
    # 存放学生信息
    try:
        dic = {'name': input("请输入学生姓名:"),
               'number': input("请输入学生学号:"),
               'age': int(input("请输入学生年龄:")),
               'score': int(input("请输入学生成绩:"))}
    except Exception as e:
        print("输入信息有误。")
        return

    # 判断信息是否合乎常理
    if dic['age'] > 100 or dic['age'] < 0:
        print("输入年龄信息有误，请重新输入!!!")
        addStu()
    if dic['score'] < 0 or dic['score'] > 100:
        print("输入成绩信息有误，请重新输入!!!")
        addStu()

    # 判断是否已经添加该学生信息
    for i in info:
        if dic['number'] in i['number']:
            print('学生信息已经存在。')
            return

    # 增加学生
    info.append(dic)
    print("学生信息添加成功!!!")


# 删除学生信息
def delStu():
    print('===欢迎使用删除学生信息功能===')
    name = input('请输入要删除学生的姓名:')
    number = input('请输入要删除学生的学号:')
    for dic in info:
        if dic['number'] == number and dic['name'] == name:
            info.remove(dic)
            print("删除成功!!")
            break


# 显示学生信息
def printStu(student_info):
    print('===所有学生信息如下===')
    for dic in student_info:
        print(f'姓名:{dic["name"]:<4}\t学号:{dic["number"]:<10}\t年龄:{dic["age"]:<2}\t成绩:{dic["score"]}')


def showStu():
    if not info:
        return print("管理系统学生信息为空!!!")
    printStu(info)


def show(student_info):
    if not student_info:
        return print("管理系统学生信息为空!!!")
    printStu(student_info)


# 修改学生信息
def updateStu():
    print('===欢迎使用修改学生信息功能===')
    if not info:
        return print("管理系统学生信息为空!!!")

    number = input('请输入要修改信息学生学号:')
    flag = True
    # 判断学生是否存在
    for dic in info:
        if dic['number'] == number:
            flag = False
    if flag:
        print('该学生不存在!!!')
        return
    temp = {'1': 'name', '2': 'number', '3': 'age', '4': 'score'}
    print('请按照提示选择修改内容:')
    print('1. 修改姓名\n2. 修改学号\n3. 修改年龄\n4. 修改成绩\n5. 任意键退出修改')

    while 1:
        flag = False
        val = input('请输入需要修改的信息(序号):')

        if val not in ['1', '2', '3', '4']:
            print('退出修改!')
            menu()
            break
        text = input('修改内容为:')

        # 判断学号是否冲突
        if val == '2':
            for dic in info:
                # 判断是否信息冲突
                if dic[temp[val]] == text:
                    print('学号冲突,请重新修改!!!')
                    flag = True
                    break
        if flag:
            continue

        # 修改学生信息
        for dic in info:
            if dic['number'] == number:
                dic[temp[val]] = text
                print('修改成功!!!')
                break
'''
姓名:孔光辉 	学号:2019014715	年龄:22	成绩:99
姓名:李四  	学号:2019014811	年龄:20	成绩:66
姓名:张三  	学号:2019014809	年龄:19	成绩:98
'''