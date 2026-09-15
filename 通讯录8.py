#中国大陆电话通讯录
import csv
import os
import shutil
CONTACT_FILE = '通讯录.txt'

import sys
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    #print('running in a PyInstaller bundle')
    CONTACT_FILE = os.path.join(os.path.dirname(sys.executable), '通讯录.txt')
else:
    #print('running in a normal Python process')
    CONTACT_FILE = '通讯录.txt'

def clean_contact(contact):
    choice = input('是否一键清除所有联系人（y/n）：').strip().lower()
    if choice == 'y':
        contact.clear()
        upload_contact(contact)
        print('已清空通讯录')
    elif choice == 'n':
        print('已取消清空')
    else:
        print ('输入无效')
    print('正在回到修改程序')

def download_contact(contact):
    if not contact:
        print ('没有联系人可以导出')
    else:
        print ('直接列举 a | 导出成excel b | 退出 任意键')
        choice = input('请输入：').strip()
        if choice == 'a':
            for name, phone in contact.items():
                print(f'{name} | {phone}')
        elif choice == 'b':
            try:
                path = os.path.join(os.path.dirname(CONTACT_FILE),'通讯录导出.csv')
                shutil.copy(CONTACT_FILE, path)
                print(f'✅ 数据已成功导出到{path}')
                print('导出的excel需要用户自己手动拉宽 B 列才能看见完整电话号码')
            except PermissionError :
                print('❌ 文件被占用，请先关闭打开的通讯录后重试')
            except Exception as e:
                print(f'❌ 导出失败，错误信息：{e}')
        else:
            pass
        print('正在回到修改程序')

def redraw_contact(contact):
    while True:
        print()
        print ('导出数据 1 | 添加 2 | 修改 3 | 删除 4 | 清空 5 | 退出 任意键')
        choice = input('请输入：').strip()
        if choice == '1':
            download_contact(contact)
        elif choice == '2':
            add_new_contact(contact)
        elif choice == '3':
            update_contact(contact)
        elif choice == '4':
            delete_contact(contact)
        elif choice == '5':
            clean_contact(contact)
        else:
            print('正在回到主程序')
            return

def read_contact():
    if not os.path.exists(CONTACT_FILE):
        example ={'示范':'13322229999'}
        upload_contact(example,show_msg=False)
        print('无文件，已生成示范内容')
        return example
    try:
        with open(CONTACT_FILE, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            contact = {}
            for line in lines:
                if not line.strip():
                    continue
                if ',' not in line:
                    continue
                name,phone = line.strip().split(',',1)
                contact[name] = phone
            if not contact:
                example = {'示范': '13322229999'}
                upload_contact(example,show_msg=False)
                print('无文件，已生成示范内容')
                return example
    except Exception as e:
        print(f"读取失败：{e}")
        bak = CONTACT_FILE + '.bak'
        shutil.copy(CONTACT_FILE, bak)
        print(f'通讯录文件损坏，已备份为 {bak}，将重新初始化。')
        return {'示范': '13322229999'}
    return contact

def upload_contact(contact,show_msg=True):
    try:
        with open(CONTACT_FILE, 'w', newline='',encoding = 'utf-8-sig') as f:
            writer = csv.writer(f)
            for name, phone in contact.items():
                writer.writerow([name, phone])
            if show_msg:
                print(f'数据已保存至{CONTACT_FILE}里')
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
        choice = input('确认是否删除（y/n）：').strip().lower()
        if choice == 'y':
            del contact[new_name]
            print(f'联系人{new_name}已删除')
            upload_contact(contact)
        elif choice == 'n':
            print('已取消删除')
        else:
            print('输入无效')
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