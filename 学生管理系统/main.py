# encoding:utf-8
import fileOperation, showInfo, basicOperation
func_dic = {
    '1': basicOperation.addStu,
    '2': basicOperation.showStu,
    '3': basicOperation.updateStu,
    '4': basicOperation.delStu,
    '5': showInfo.score_ascend,
    '6': showInfo.score_descend,
    '7': showInfo.age_ascend,
    '8': showInfo.age_descend,
    '9': fileOperation.saveInfo,
    '10': fileOperation.readFile,
    '11': fileOperation.clearFile,
}

print('=======欢迎来到学生管理系统======')
print("1)\t添加学生信息。")
print("2)\t显示所有学生信息。")
print("3)\t修改学生信息。")
print("4)\t删除学生信息。")
print("5)\t按学生成绩高-低显示学生信息。")
print("6)\t按学生成绩低-高显示学生信息。")
print("7)\t按学生年龄高-低显示学生信息。")
print("8)\t按学生年龄低-高显示学生信息。")
print("9)\t保存学生信息到文件(student.txt)。")
print("10)\t保存学生信息到文件(student.txt)。")
print("11)\t清空学生信息文件(student.txt)。")
print("\t退出: 按任意键退出。。。")

while 1:
    value = input('请输入您要使用管理系统的功能(序号):')
    try:
        func_dic[value]()
    except Exception:
        print('管理系统己退出。')
        break
