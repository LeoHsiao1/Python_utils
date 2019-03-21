"""
实现一些与终端交互、读写文件、记录日志的功能。
  class `Inputs`
  def `print_text`
  def `read_csv`
  def `write_csv`
  def `repeat`
  def `creat_logger`
"""

import os
import time


class Inputs:
    """
    提供一些从终端获取用户输入的静态方法。
      - 可在外部创建该类的变量，暂存一些输入的数据。
    """

    @staticmethod
    def input_int(tip_str='', repeat=True):
        while repeat:
            try:
                return int(input(tip_str))
            except:
                print("输入的不是整数！")

    @staticmethod
    def input_positive_int(tip_str='', repeat=True):
        while repeat:
            num = Inputs.input_int(tip_str, repeat)
            if num > 0:
                return num
            else:
                print("输入的不是正整数！")

    @staticmethod
    def input_real_num(tip_str='', repeat=True):
        while repeat:
            try:
                return float(input(tip_str))
            except:
                print("输入的不是整数或浮点数！")

    @staticmethod
    def input_path(tip_str='', repeat=True):
        while repeat:
            path = input(tip_str)
            if os.path.isdir(path):
                return path
            else:
                print("输入的不是有效目录！")


def print_text(text, delay=0):
    """ 在DOS窗口中显示文本text，显示每个字符的间隔时长为delay """
    import sys
    for line in text:
        for word in line:
            print(word, end='')  # 逐个字显示
            time.sleep(delay)
            # 每打印一个字符就刷新一次stdout，
            # 否则缓存区累积了一行才会刷新stdout
            sys.stdout.flush()


def read_csv(file, *args, **kwargs):
    """
    从一个csv文件中读取数据，并将每行数据转换成list格式。
      - 基于csv模块。
      - 该函数的参数列表与open()相同。
    """
    import csv
    result = []
    with open(file, *args, **kwargs) as f:
        csv_reader = csv.reader(f)   # 在一个文件流f上创建csv阅读器
        try:
            for line in csv_reader:  # 迭代csv_reader的内容
                result.append(line)
        except csv.Error as e:       # 捕捉读取csv文件时的异常
            raise OSError("A reading error in file {}, line {}:\n{}"
                          .format(file, csv_reader.line_num, e))
    return result


def write_csv(data, file, mode='w', newline='', **kwargs):
    """ 
    将数据转换成csv格式，再保存到指定文件中。
      - 基于csv模块。
    """
    import csv
    with open(file, mode, newline=newline, **kwargs) as f:
        csv_writer = csv.writer(f)  # 在文件流f上创建一个csv写入器
        csv_writer.writerows(data)  # 写入多行


def repeat(repeat=0, logger=print):
    """
    一个装饰器。当函数因为异常而中断运行时，最多重复执行repeat次。
      `repeat`为负数时重复执行无限次，直到函数正常结束。
      `logger`是记录异常信息的函数名。
    """
    import traceback

    def __decorator(func):
        def __wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # logger(traceback.format_exc())
                logger(str(e))
                nonlocal repeat
                if repeat != 0:
                    repeat -= 1
                    __wrapper(*args, **kwargs)
                else:
                    raise
        return __wrapper
    return __decorator

# # sample：
# @repeat(repeat=3)
# def fun1(x=None):
#     print(x  - 1)


def creat_logger(name, level="INFO"):
    """ 使用logging模块创建日志器，进行设置时需要手动修改该函数的代码。 """
    import logging

    # 设置日志的文件名
    filename = name + time.strftime("_%Y%m%d", time.localtime()) + ".log"

    # 创建一个日志处理器
    handler = logging.FileHandler(filename)
    handler.setLevel("DEBUG")
    formatter = logging.Formatter(
        fmt="{asctime}  - {levelname:5}  - {threadName:20} --> {message}", style='{')
    handler.setFormatter(formatter)            # 设置该handler的格式器

    # 创建一个将日志输出到终端的日志处理器
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel("INFO")

    # 创建一个日志器
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)                 # 为该日志器添加一个处理器
    logger.addHandler(console_handler)

    return logger
