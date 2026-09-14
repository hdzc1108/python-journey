#中国大陆电话通讯录

import json
CONTACT_FILE = 'contacts.json'

def read_contact():
    try:
        with open(CONTACT_FILE, 'r', encoding = 'utf-8') as f:
            return json.loads(f.read())
    except FileNotFoundError:
        return {'示范':'13322229999'}

def upload_contact(contact):
    try:
        with open(CONTACT_FILE, 'w', encoding = 'utf-8') as f:
            json.dump(contact, f, ensure_ascii=False, indent=4)
            print('数据已保存至“contacts.json"里')
    except OSError:
        print ('保存失败，请检查文件代码')


def valid_phone(new_phone):
    valid_prefix = ('13','15','17','18','19')
    if len(new_phone)!=11:
        return False
    elif not new_phone.isdigit():
        return False
    elif not new_phone.startswith(valid_prefix):
        return False
    else:
        return True

def add_new_contact(contact):
    while True:
        new_name = input("请输入新联系人姓名").strip().lower()
        if new_name == '':
            print('姓名不能为空,请重新输入')
            continue
        elif new_name in contact:
            print('此联系人已存在，如果需要更改联系人，请按c')
            return
        else:
            while True:
                new_phone = input('请输入新联系人电话').strip()
                result = valid_phone(new_phone)
                if result == True:
                    contact[new_name] = new_phone
                    print('添加成功')
                    upload_contact(contact)
                    break
                else:
                    print('电话号码格式有误，必须11位纯数字，有效号段开头。请重新输入。')
        break

def update_contact(contact):
    while True:
        new_name = input("请输入原联系人姓名").strip().lower()
        if new_name == '':
            print('姓名不能为空,请重新输入')
            continue
        elif new_name not in contact:
            print('未查到联系人,如果需要新增联系人，请按b,如果需要更改联系人，请按c')
            return
        else:
            while True:
                new_phone = input('请输入原联系人新的电话').strip()
                result = valid_phone(new_phone)
                if result == True:
                    contact[new_name] = new_phone
                    print('修改成功')
                    upload_contact(contact)
                    break
                else:
                    print('电话号码格式有误，必须11位纯数字，有效号段开头。请重新输入。')
        break

def main():
    contact = read_contact()
    while True:
        user_input = input('请输入你要查询的联系人,按“a”结束，如果需要新增联系人，请按b，如果需要更改联系人，请按c')
        user_clean_input = user_input.strip().lower()
        if user_clean_input == 'a':
            break
        elif user_clean_input in contact:
            print(f'该联系人电话号码是{contact[user_clean_input]}')
        elif user_clean_input == 'b':
            add_new_contact(contact)
        elif user_clean_input == 'c':
            update_contact(contact)
        else:
            print('未查到联系人,如果需要新增联系人，请按b,如果需要更改联系人，请按c')
    print('谢谢使用')

if __name__ == '__main__':
    main()