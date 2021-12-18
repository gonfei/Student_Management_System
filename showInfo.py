# encoding:utf-8
# @作者: 2019014715孔光辉
# @类型: 课程设计
from basicOperation import show, info


# 返回成绩
def scoreSort(*ll):
    for score in ll:
        return score.get("score")


# 返回年龄
def ageSort(*ll):
    for age in ll:
        return age.get("age")


# 按成绩降序显示
def score_descend():
    print("按成绩降序(高-低)显示:")
    res = sorted(info, key=scoreSort, reverse=True)
    show(student_info=res)


# 按成绩升序显示
def score_ascend():
    print("按成绩升序(低-高)显示:")
    res = sorted(info, key=scoreSort)
    show(student_info=res)


# 按年龄升序显示
def age_ascend():
    print("按年龄升序(低-高)显示:")
    res = sorted(info, key=ageSort)
    show(student_info=res)


# 按年龄降序显示
def age_descend():
    print("按年龄降序(高-低)显示:")
    res = sorted(info, key=ageSort, reverse=True)
    show(student_info=res)
