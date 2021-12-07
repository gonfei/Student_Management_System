# encoding:utf-8


info = []


# 添加学生信息
def addStu():
    dic = {}  # 存放学生信息
    # name = input("请输入学生姓名:")
    dic['name'] = '孔光辉'
    # number = input("请输入学生学号:")
    dic['number'] = '2019014715'
    # age = input("请输入学生年龄:")
    dic['age'] = '18'
    # score = input("请输入学生成绩:")
    dic['score'] = '99'

    # 判断是否已经添加该学生信息
    for i in info:
        if dic['number'] in i['number']:
            print('学生信息已经存在。')
            return

    # 增加学生
    info.append(dic)


# 删除学生信息
def delStu():
    name = input('请输入要删除学生的姓名:')
    number = input('请输入要删除学生的学号:')
    for dic in info:
        if dic['number'] == number and dic['name'] == name:
            info.remove(dic)


# 显示学生信息
def showStu():
    if not info:
        return print("管理系统学生信息为空!!!")
    for dic in info:
        print('姓名:{:<3}\t学号:{:<10}\t年龄:{:<2}\t成绩:{}'.format(dic['name'], dic['number'], dic['age'], dic['score']))


# 修改学生信息
def updateStu():
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
    temp = {
        '1': 'name',
        '2': 'number',
        '3': 'age',
        '4': 'score',
    }
    print('1. 修改姓名\n2. 修改学号\n3. 修改年龄\n4. 修改成绩\n5. 任意键退出修改')

    while 1:
        flag = False
        val = input('请输入需要修改的信息(序号):')

        if val not in ['1', '2', '3', '4']:
            print('退出修改!')
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
