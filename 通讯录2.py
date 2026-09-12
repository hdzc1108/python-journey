#通讯录
contact = {
    'Jay' : '122345',
    'Chen' : '45678',
    'May' : '1556'
}

def add_new_contact():
    while True:
        new_name = input("请输入新联系人姓名").strip().title()
        new_phone = input('请输入新联系人电话').strip()
        if new_name == '' or new_phone == '':
            print ('姓名和电话不能为空！')
        else:
            contact[new_name] = new_phone
            print('添加成功')
            break

while True:
    user_input = input('请输入你要查询的联系人,按“A”结束，如果需要新增联系人，请按B')
    user_clean_input = user_input.strip().title()
    if user_clean_input == 'A':
        break
    elif user_clean_input in contact:
        print (f'该联系人电话号码是{contact[user_clean_input]}')
    elif user_clean_input == 'B':
        add_new_contact()
    else:
        print ('未查到联系人,如果需要新增联系人，请按B')

print('谢谢使用')