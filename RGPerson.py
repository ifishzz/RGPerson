# -*-coding:utf-8-*-
# Author: key
# Email: admin@gh0st.cn
# Blog: gh0st.cn
# Team: Mystery Security Team

import random
from districtcode import area_dict
from datetime import timedelta, date

# 生成手机号
def genMobile():
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "170", "172", "176", "178", "177", "180", "181", "182",
                   "183", "184","185", "186", "187", "188", "189"]
        return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

# 生成车牌号
def genCarNo():
    provinces = ['京', '津', '沪', '渝', '冀', '豫', '云', '辽', '黑', '湘', '皖', '鲁', '新', '苏', '浙', '赣', '鄂', '桂','甘', '晋', '蒙', '陕', '吉', '闽', '贵', '粤', '青', '藏', '川', '宁', '琼']
    province = random.sample(provinces, 1)
    letter = [chr(random.randint(65, 90))]
    code_list = []
    for i in range(10):
        code_list.append(str(i))
    for i in range(65, 91):
        if chr(i) == 'O':
            pass
        else:
            code_list.append(chr(i))
    num_1 = random.sample(code_list, 1)
    num_2 = random.sample(code_list, 1)
    num_3 = [str(random.randint(0, 9))]
    num_4 = [str(random.randint(0, 9))]
    num_5 = [str(random.randint(0, 9))]
    nums = num_1 + num_2 + num_3 + num_4 + num_5
    carNo = ''.join(province + letter + nums)
    return carNo

def first_name():
    first_name_list = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
                '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
                '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
                '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
                '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']
    n = random.randint(0, len(first_name_list) - 1)
    f_name = first_name_list[n]
    return f_name

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xf9)
    val = f'{head:x}{body:x}'
    st = bytes.fromhex(val).decode('gb2312')
    return st

def second_name():
    second_name_list = [GBK2312(), '']
    n = random.randint(0, 1)
    s_name = second_name_list[n]
    return s_name

def last_name():
    return GBK2312()

# 生成姓名
def genName():
    name = first_name() + second_name() + last_name()
    return name

# 生成身份证
def genIdCard(age,gender):
    area_code = ('%s' % random.choice(list(area_dict.keys())))
    id_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    check_code_list = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    if str(area_code) not in area_dict.keys():
        return None
    datestring = str(date(date.today().year - age, 1, 1) + timedelta(days=random.randint(0, 364))).replace("-", "")
    rd = random.randint(0, 999)
    if gender == 0:
        gender_num = rd if rd % 2 == 0 else rd + 1
    else:
        gender_num = rd if rd % 2 == 1 else rd - 1
    result = str(area_code) + datestring + str(gender_num).zfill(3)
    b = result + str(check_code_list[sum([a * b for a, b in zip(id_code_list, [int(a) for a in result])]) % 11])
    return b

if __name__ == '__main__':
    age = random.randint(16,60) #可调整生成的年龄范围（身份证），这边是16-60岁
    gender = random.randint(0,1)
    sex = u"男" if gender == 1 else u"女"
    print("姓名: {0}\n年龄: {1}\n性别: {2}\n身份证: {3}\n手机号: {4}\n车牌号: {5}".format(genName(), age, sex, genIdCard(age, gender), genMobile(),genCarNo()))