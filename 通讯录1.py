#通讯录

contact = {
    'Jay' : '122345',
    'Chen' : '45678',
    'May' : '1556'
}
while True:
    user_input = input('请输入你要查询的联系人,按“a”结束')
    if user_input == 'a':
        break
    elif user_input in contact:
        print (f'该联系人电话号码是{contact[user_input]}')
    else:
        print ('未查到联系人')
print('谢谢使用')