#猜数字游戏
import random
def random_num():
    print('猜数字大小游戏')
    the_answer = random.randint(1, 100)
    count = 0
    while True:
        count += 1
        try:
            user_answer = int(input('请输入你认为的数字'))
        except ValueError:
            print('请输入有效数字')
            continue
        if the_answer < user_answer:
            print("猜大了，重新猜")
        elif the_answer > user_answer:
            print("猜小了，重新猜")
        else:
            break
    print('猜对了')
    print('一共猜了' + str(count) + '次')
    print(f'一共猜了{count}次')

random_num()