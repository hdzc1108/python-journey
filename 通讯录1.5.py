#通讯录

contact = {
    'Jay' : '122345',
    'Chen' : '45678',
    'May' : '1556'
}
while True:
    user_input = input('请输入你要查询的联系人,按“A”结束，如果需要新增联系人，请按B')
    user_clean_input = user_input.strip().title()
    if user_clean_input == 'A':
        break
    elif user_clean_input in contact:
        print (f'该联系人电话号码是{contact[user_clean_input]}')
    elif user_clean_input == 'B':
        new_name = input("请输入新联系人姓名").strip().title()
        new_phone = input('请输入新联系人电话')
        contact[new_name] = new_phone
        print('添加成功')
    else:
        new_input = input ('未查到联系人,请问是否添加新联系人').strip()
        if new_input =='是':
            new_name = input("请输入新联系人姓名").strip().title()
            new_phone = input ('请输入新联系人电话')
            contact[new_name] = new_phone
            print ('添加成功')
        elif new_input =='否':
            continue
        else:
            print ('输入错误，请输入是或否')
print('谢谢使用')