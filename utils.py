import random
import os


def is_legal(exp_str, cards):
    """
    检查输入的表达式是否合法
    
    :param exp_str: 用户输入的表达式，字符串类型
    :param cards: 本次题目的牌组，是一个从小到大排好序的 tuple 型数组
    :return: bool 型数据，合法返回 True，不合法返回 False
    """
    op_list = ["+", "-", "*", "/", "(", ")"]  # 所有合法的操作符
    cards_used = []  # 存放表达式中所有用到的牌
    tmp = ""
    for ch in exp_str:
        if ch.isdigit():
            tmp += ch
        elif ch in op_list:
            if tmp != "":
                cards_used.append(int(tmp))
                tmp = ""
        else:
            return False
    if tmp != "":
        cards_used.append(int(tmp))
    cards_used.sort()
    if cards != tuple(cards_used):  # 表达式中用到的牌和题目给的牌组不同时
        return False
    return True


def gen_cards():
    """
    随机生成牌组（题目）

    :return: 一个 4 个数字的数组
    """
    cards = []
    for i in range(4):
        cards.append(random.randint(1, 13))
    return cards


def load_answer():
    """
    从文件中加载所有的标准答案

    :return: 一个字典，以从小到大排好序的 tuple 型数组（牌组）作为 key，以其标准答案作为 value
    """
    answer_dict = {}
    with open(
        os.path.join(os.path.dirname(__file__), "answer.txt"), "r", encoding="utf-8",
    ) as f:
        line = f.readline()
        while line:
            cards, answer = _process_line(line.replace("\n", ""))
            # 将卡片列表转成元组作为字典的key
            answer_dict[tuple(cards)] = answer
            line = f.readline()
    return answer_dict


def _process_line(line):
    """
    针对标准答案文件中的单行数据进行处理

    :param line: 从标准答案文件中读取的一行字符串
    :return: 一个牌组（4 数字的数组）cards，及其对应的标准答案 answer
    """
    line_split = line.split(" ")
    cards_str = line_split[:4]
    cards = list(map(int, cards_str))
    answer = line_split[-1]
    return cards, answer
