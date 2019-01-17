import os
import time


# 保存检索的输入信息（本来是用全局变量，现在改成类变量，便于扩展）
class Inputs:
    dict1 = dict()
    # 设置检索的关键词file_key和str_key
    # dict1["file_key"] = "str_key"
    dict1[""] = ""  # 要判断receive的数量，低于5就提取

    # 设置检索目录
    path = ''

    #设置要检索的文件的后缀名
    suffix=''


# 获取path目录下，所有.log文件的绝对地址，保存在file_list列表中返回
def searchFile(path, suffix):
    if os.path.isdir(path) == 0:
        raise TypeError('The first argument of searchFile() is not a directory.')
    if isinstance(suffix, str) == 0:
        raise TypeError('The second argument of searchFile() is not a str.')

    try:
        dir_list = os.listdir(path)  # 获得path目录下的所有文件和文件夹列表
    except:
        # 可能会撞到没有访问权限的文件夹，这里把异常处理掉，以免打断程序运行
        print("访问目录 %s 失败。" % (path))
        return -1

    file_list = []
    for name in dir_list:
        sub_path = os.path.join(path, name)  # 把目录名和文件名合成一个子路径
        if os.path.isdir(sub_path) == True:  # 如果该子路径是一个文件夹，就递归调用本函数检索子文件夹，即“深度优先搜索”
            sub_list = searchFile(sub_path,suffix)
            if sub_list != -1:
                file_list.extend(sub_list)  # 在file_list末尾增加一个列表
        elif sub_path[sub_path.rfind('.'):].lower() == suffix:
            file_list.append(sub_path)  # 在file_list末尾增加一个字符串

    return file_list


# 获取指定文件中，包含str_key的每行数据，保存在result列表中返回
def searchString(file_path, str_key):
    result = []
    with open(file_path, 'r') as raw_file:
        for line in raw_file:
            if str_key in line:
                result.append(line)
    return result


def inputPath(tip_str):
    while 1:
        try:
            path = input(tip_str)
            if os.path.isdir(path) == False:
                print("输入的目录不存在！")
            else:
                return path
        except:
            print("输入的目录不存在！")


def main():
    # 提示用户输入
    print("该脚本用于检索指定目录下所有文件的内容，合并成一个文件。")
    Inputs.path = inputPath("请输入要检索的目录：")
    Inputs.suffix=input("请输入要检索的文件的后缀名：")

    # 设置保存检索结果的文件路径
    time_str = time.strftime(
        '-%Y%m%d-%H%M%S', time.localtime())  # 加上时间戳，用于区分生成的多个结果文件
    result_file_name = "merge_result" + time_str + Inputs.suffix
    result_file_path = os.path.join(Inputs.path, result_file_name)

    file_list = searchFile(Inputs.path,Inputs.suffix)

    # 开始检索
    with open(result_file_path,'w') as f:
        for file_key, str_key in Inputs.dict1.items():
            for path in file_list:
                if file_key in os.path.basename(path):
                    try:
                        result = searchString(path, str_key)
                        f.writelines(result)
                    except:
                        print("检索文件 {} 时出错".format(path))
                        # raise  #不抛出异常，使程序在检索出错时也能保存数据

            print("完成。")

    print("\n检索完成！\n数据保存为文件 {} ".format(result_file_path))

    return 0


try:
    main()
except:
    print("运行出错！")
    raise
finally:
    os.system("pause")  # 无论是否发生异常，都保留DOS窗口的显示