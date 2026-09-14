
import json
import os
import shutil

CONTACT_FILE = 'contacts.json'


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


def save_contact(contact):
    """保存通讯录到 JSON。"""
    try:
        with open(CONTACT_FILE, 'w', encoding='utf-8') as f:
            json.dump(contact, f, ensure_ascii=False, indent=4)
        print('数据已保存至 “contacts.json” 里。')
    except OSError:
        print('保存失败，请检查文件权限。')


def valid_phone(new_phone):
    """
    中国大陆手机号：11 位纯数字，且以 1 开头、第二位为 3-9。
    覆盖 13x/14x/15x/16x/17x/18x/19x 全部现行号段。
    """
    return (len(new_phone) == 11
            and new_phone.isdigit()
            and new_phone[0] == '1'
            and new_phone[1] in '3456789')


def add_new_contact(contact):
    new_name = input('请输入新联系人姓名：').strip()
    if new_name == '':
        print('姓名不能为空。')
        return
    if new_name in contact:
        print('此联系人已存在，如需修改请按 “c”。')
        return

    new_phone = input('请输入新联系人电话：').strip()
    if not valid_phone(new_phone):
        print('电话号码格式有误：必须是 11 位纯数字，且为中国大陆手机号段。')
        return
    contact[new_name] = new_phone
    print('添加成功。')
    save_contact(contact)


def update_contact(contact):
    new_name = input('请输入要修改的联系人姓名：').strip()
    if new_name == '':
        print('姓名不能为空。')
        return
    if new_name not in contact:
        print('未查到该联系人，如需新增请按 “b”。')
        return

    new_phone = input('请输入新的电话号码：').strip()
    if not valid_phone(new_phone):
        print('电话号码格式有误：必须是 11 位纯数字，且为中国大陆手机号段。')
        return
    contact[new_name] = new_phone
    print('修改成功。')
    save_contact(contact)


def delete_contact(contact):
    name = input('请输入要删除的联系人姓名：').strip()
    if name in contact:
        del contact[name]
        print('删除成功。')
        save_contact(contact)
    else:
        print('未查到该联系人。')


def list_contacts(contact):
    if not contact:
        print('通讯录为空。')
        return
    print('—— 当前通讯录 ——')
    for i, (name, phone) in enumerate(contact.items(), 1):
        print(f'{i}. {name}: {phone}')


def main():
    contact = read_contact()
    menu = ('操作：直接输入姓名查询 | a 退出 | b 新增 | c 修改 | '
            'd 删除 | l 列出全部')
    while True:
        print('\n' + menu)
        user_input = input('请输入：').strip()
        key = user_input.lower()

        if key == '':
            continue
        elif key == 'a':
            break
        elif key == 'b':
            add_new_contact(contact)
        elif key == 'c':
            update_contact(contact)
        elif key == 'd':
            delete_contact(contact)
        elif key == 'l':
            list_contacts(contact)
        elif user_input in contact:
            print(f'{user_input} 的电话号码是 {contact[user_input]}')
        else:
            print('未查到联系人。如需新增请按 “b”。')


if __name__ == '__main__':
    main()
