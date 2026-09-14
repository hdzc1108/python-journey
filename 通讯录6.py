#中国大陆电话通讯录
import pandas as pd
import json
import os
import shutil
CONTACT_FILE = 'contacts.json'

def clean_contact(contact):
    choice = input('是否一键清除所有联系人（请按是或否）：').strip()
    if choice == '是':
        contact.clear()
        upload_contact(contact)
        print('已清空通讯录')
    else:
        print('已取消清空')
    print('正在回到修改程序')

def download_contact(contact):
    if not contact:
        print ('没有联系人可以导出')
    else:
        print ('直接列举 a | 导出成excel b | 退出 任意键')
        choice = input('请输入：').strip()
        if choice == 'a':
            print(contact)
        elif choice == 'b':
            try:
                # 1. 把字典转换成 pandas 能看懂的表格格式（列表里面套字典）
                # 原来的 contact 是 {'jay': '133...'}，我们要变成 [{'姓名': 'jay', '电话': '133...'}, ...]
                data_list = [{'姓名': name, '电话': phone} for name, phone in contact.items()]
                # 2. 把列表转换成表格对象（DataFrame）
                df = pd.DataFrame(data_list)
                # 3. 导出到 Excel 文件
                # index=False 的意思是不加行号，让表格更干净
                df.to_excel('通讯录导出.xlsx', index=False)
                print('✅ 数据已成功导出到 通讯录导出.xlsx')
            except Exception as e:
                print(f'❌ 导出失败，错误信息：{e}')
        else:
            pass
        print('正在回到修改程序')

def redraw_contact(contact):
    while True:
        print()
        print ('导出数据 a | 添加 b | 修改 c | 删除 d | 清空 e | 退出 任意键')
        choice = input('请输入：').strip()
        if choice == 'a':
            download_contact(contact)
        elif choice == 'b':
            add_new_contact(contact)
        elif choice == 'c':
            update_contact(contact)
        elif choice == 'd':
            delete_contact(contact)
        elif choice == 'e':
            clean_contact(contact)
        else:
            print('正在回到主程序')
            return

def read_contact():
    """读取通讯录。文件不存在/损坏/为空时安全兜底。"""
    if not os.path.exists(CONTACT_FILE):
        return {'示范': '13322229999'}
    try:
        with open(CONTACT_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        if isinstance(data, dict):
            return data
        # 文件内容不是 dict，视为损坏
        raise ValueError('root is not a dict')
    except (json.JSONDecodeError, ValueError):
        # 备份损坏文件，避免覆盖丢失
        bak = CONTACT_FILE + '.bak'
        shutil.copy(CONTACT_FILE, bak)
        print(f'通讯录文件损坏，已备份为 {bak}，将重新初始化。')
        return {'示范': '13322229999'}

def upload_contact(contact):
    try:
        with open(CONTACT_FILE, 'w', encoding = 'utf-8') as f:
            json.dump(contact, f, ensure_ascii=False, indent=4)
            print('数据已保存至"contacts.json"里')
    except OSError:
        print ('保存失败，请检查文件代码')

def valid_phone(new_phone):
    return (len(new_phone) == 11
            and new_phone.isdigit()
            and new_phone[0] == '1'
            and new_phone[1] in '3456789')

def delete_contact(contact):
    new_name = input("请输入原联系人姓名：").strip()
    if new_name == '':
        print('姓名不能为空,请重新输入')
    elif new_name not in contact:
        print('未查到联系人')
    else:
        choice = input('确认是否删除（回答是或否）：').strip()
        if choice == '是':
            del contact[new_name]
            print(f'联系人{new_name}已删除')
            upload_contact(contact)
        else:
            print('已取消删除')
    print('正在回到修改程序')

def add_new_contact(contact):
    new_name = input("请输入新联系人姓名：").strip()
    if new_name == '':
        print('姓名不能为空')
    elif new_name in contact:
        print('此联系人已存在')
    else:
        new_phone = input('请输入新联系人电话：').strip()
        if valid_phone(new_phone):
            contact[new_name] = new_phone
            print(f'联系人{new_name}添加成功')
            upload_contact(contact)
        else:
            print('电话号码格式有误，必须11位纯数字，有效号段开头')
    print('正在回到修改程序')

def update_contact(contact):
    new_name = input("请输入原联系人姓名：").strip()
    if new_name == '':
        print('姓名不能为空')
    elif new_name not in contact:
        print('未查到联系人')
    else:
        new_phone = input('请输入原联系人新的电话：').strip()
        if valid_phone(new_phone):
            contact[new_name] = new_phone
            print(f'联系人{new_name}修改成功')
            upload_contact(contact)
        else:
            print('电话号码格式有误，必须11位纯数字，有效号段开头')
    print('正在回到修改程序')

def main():
    print ('中国大陆通讯录小程序')
    contact = read_contact()
    while True:
        print()
        print('操作：直接查询姓名 | 退出 * | 修改 +')
        user_input = input('请输入：')
        user_clean_input = user_input.strip()
        if user_clean_input == '*':
            break
        elif user_clean_input == '+':
            redraw_contact(contact)
        elif user_clean_input in contact:
            print(f'该联系人电话号码是{contact[user_clean_input]}')
        else:
            print('未查到联系人')
    print('谢谢使用')

if __name__ == '__main__':
    main()