# encoding:utf-8
# @作者: 2019014715孔光辉
# @类型: 课程设计

import basicOperation as bo
import showInfo as show
import fileOperation as fo

# 系统功能字典
func_dic = {
    '0': bo.menu,
    '1': bo.addStu,
    '2': bo.showStu,
    '3': bo.updateStu,
    '4': bo.delStu,
    '5': show.score_descend,
    '6': show.score_ascend,
    '7': show.age_descend,
    '8': show.age_ascend,
    '9': fo.saveInfo,
    '10': fo.readFile,
    '11': fo.clearFile,
}
bo.menu()  # 显示菜单
while 1:
    value = input('请输入您要使用管理系统的功能(序号):')
    try:
        func_dic[value]()
    except Exception as e:
        print(f'{e}\n管理系统己退出。')
        break
