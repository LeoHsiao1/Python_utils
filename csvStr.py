def list_to_csvStr(raw_list):
    if isinstance(raw_list, list) == 0:
        raise TypeError('The argument of list_to_csvStr() is not a list.')

    line_list = []

    # 将list中各项元素转换成字符串类型
    for i in raw_list:
        line_list.append(str(i))

    # 保证末尾有一个换行符
    csvStr = ','.join(line_list)
    if csvStr[-2:] == '\n':
        return csvStr
    else:
        return csvStr+'\n'


def csvStr_to_list(csvStr):
    if isinstance(csvStr, str) == 0:
        raise TypeError('The argument of csvStr_to_list() is not a str.')

    line_str = csvStr.replace('\n', '')  # 删除每行末尾的换行符 \n
    line_list = line_str.split(',')  # 将每行的各项分开

    # 如果某项是字符串类型的数字，就把它转换成数字
    i = 0
    for x in line_list:
        try:
            if isinstance(int(x), int):
                line_list[i] = int(x)
        except:
            pass
        i += 1

    return line_list


# sample:

# with open(path, 'a') as f:  # 创建.csv文件，模式为add
#     for line in data_list:
#         f.writelines(list_to_csvStr(line))  # 保存检索结果
