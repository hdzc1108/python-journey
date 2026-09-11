#猜数字游戏
import random
print ('猜数字大小游戏')
the_answer = random.randint(1,100)
while True:
    user_answer = float(input('请输入你认为的数字'))
    if the_answer < user_answer:
        print("猜大了，重新猜")
    if the_answer > user_answer:
        print("猜小了，重新猜")
    if the_answer == user_answer:
        break
print('猜对了')