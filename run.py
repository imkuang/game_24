from utils import *
import sys


def main():
    print("********** 24点小游戏 By 夕日 **********")
    print("使用说明：")
    print("1. 输入 answer 查看当前题目的答案")
    print("2. 输入 stop 终止游戏")
    print("3. 直接输入算式即可回答题目，若判断无解请输入 nope")
    print("4. 除上述描述情况之外的任何输入都是不合法的")
    answers = load_answer()
    cmd_list = ["stop", "answer", "nope"]
    while True:
        cards = gen_cards()
        print("***************************************")
        print("题目：", cards)
        cards.sort()
        standard_answer = answers[tuple(cards)]
        user_input = input(": ")
        if user_input == cmd_list[0]:
            sys.exit(0)
        elif user_input == cmd_list[1]:
            print("标准答案：", standard_answer.replace("nope", "无解"))
        elif user_input == cmd_list[2]:
            if standard_answer == "nope":
                print("回答正确！答案： 无解")
            else:
                print("回答错误！正确答案：", standard_answer)
        else:
            if is_legal(user_input, tuple(cards)):
                try:
                    if abs(eval(user_input) - 24) < 1e-10:
                        print("回答正确！答案：", user_input)
                    else:
                        print("回答错误！答案：", standard_answer)
                except ArithmeticError:
                    print("无效的算式！标准答案：", standard_answer.replace("nope", "无解"))
            else:
                print("不合法的输入！标准答案：", standard_answer.replace("nope", "无解"))


if __name__ == "__main__":
    main()
