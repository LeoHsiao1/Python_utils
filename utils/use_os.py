import os


def searchFile(path, suffix=None, depth=-1, logger=print):
    """
    在目录path下检索所有符合要求的文件，把它们的绝对地址保存成一个
    list返回（用户自行筛选文件名）。如果检索结果为空，则返回值为 [ ] 。
     path    : str，一个在系统中存在的目录名。
     suffix  : str，文件的后缀名，不区分大小写。默认不考虑后缀名，即
     检索所有类型的文件。
     depth   : int，最多检索depth层子目录。depth为负数时检索无限层。
     logger  : callable，记录异常信息的函数名。
    """
    # 检查输入的参数是否有效
    if not os.path.isdir(path):
        raise ValueError("'path' must be an existing directory.")

    # 将需要循环执行的语句放在内层函数中
    def __searchFile(path, suffix, depth):
        # 获取目录path下的文件列表
        try:
            dir_list = os.listdir(path)
        except PermissionError as e:
            # 可能会遇到没有访问权限的文件夹，这里把异常处理掉，以免打断程序运行
            logger("PermissionError: {}".format(e))
            return -1  # 退出函数，不检索该目录

        # 开始检索
        file_list = []
        for name in dir_list:
            sub_path = os.path.join(path, name)  # 把目录名和文件名合成一个子路径

            # 如果子路径是一个文件夹且depth!=0，就递归调用本函数进入该文件夹检索，即“深度优先搜索”
            if depth != 0 and os.path.isdir(sub_path) == True:
                sub_list = __searchFile(sub_path, suffix, depth-1)
                if sub_list != -1:
                    file_list.extend(sub_list)  # 在file_list末尾增加一个列表

            # 如果子路径是一个文件，就判断后缀名是否正确，如果没输入suffix就不考虑后缀名
            elif suffix == None or suffix.lower() == sub_path[sub_path.rfind('.'):].lower():
                file_list.append(sub_path)  # 在file_list末尾增加一个字符串

        return file_list

    return __searchFile(path, suffix, depth)
