#成绩统计

def get_scores():
    score_list = []
    while True:
        user_input = input ('请输入成绩（输入a结束）')
        if user_input == 'a':
            break
        try:
            x = float(user_input)
            score_list.append(x)
        except ValueError:
            print('请输入有效的数字！')
    return score_list

def average (score_list):
    all = sum(score_list)
    average = all / len(score_list)
    return average

def biggest (score_list):
    top = max(score_list)
    return top

def main():
    score_list = get_scores()
    ave = average (score_list)
    top = biggest (score_list)
    print('最高分：',top)
    print('平均分：',ave)

main()