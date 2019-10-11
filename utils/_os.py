# -*- coding: utf-8 -*-
"""
基于os模块。
  - def `searchFile`
"""

import os


def searchFile(path, suffix=None, depth=-1, log=print):
    """
    在`path`目录下递归检索符合`suffix`后缀名的文件，返回这些文件的绝对地址列表。
      - `path`: 一个系统目录。
      - `suffix`: 文件的后缀名，区分大小写。可以是一个字符串，或字符串的元组。默认不区分后缀名。
      - `depth`: 表示最多检索到第几层子目录。默认检索无数层。
      - `log`: 记录日志的函数名。
    """
    # 检查输入的参数是否有效
    if not os.path.isdir(path):
        raise ValueError("'path' must be an existing directory.")

    # 将需要循环执行的语句放在内层函数中
    def __searchFile(path, suffix, depth):
        try:
            dir_list = os.listdir(path)

        # 可能会遇到没有访问权限的文件夹，这里把异常处理掉，以免打断程序运行
        except PermissionError as e:
            log("PermissionError: {}".format(e))
            return -1  # 退出函数，不检索该目录

        # 开始检索
        file_list = []
        for name in dir_list:
            # 把目录名和文件名合成一个子路径
            sub_path = os.path.join(path, name)

            # 如果子路径是一个文件夹且depth!=0，就递归调用本函数进入该文件夹检索，即深度优先搜索
            if depth != 0 and os.path.isdir(sub_path) == True:
                sub_list = __searchFile(sub_path, suffix, depth-1)
                if sub_list != -1:
                    file_list.extend(sub_list)  # 在file_list末尾增加一个列表

            # 如果子路径是一个文件，就判断后缀名是否正确，如果没输入suffix就不考虑后缀名
            elif suffix == None or sub_path.endswith(suffix):
                file_list.append(sub_path)  # 在file_list末尾增加一个字符串

        return file_list

    return __searchFile(path, suffix, depth)


if __name__ == "__main__":
    _list = searchFile("D:\\", ".py")
