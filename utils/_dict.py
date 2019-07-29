# -*- coding: utf-8 -*-
"""
关于字典。
  - def `sort_dict`
  - def `flat_key`
  - def `flat_dict`
"""

def sort_dict(_dict):
    """ 基于sorted()对字典排序，返回一个新字典。 """
    result = {}
    for k in sorted(_dict):
        result[k] = _dict[k]
    return result


def flat_key(layer):
    """ 将多层key合并为一个key，例如：flat_key(["1","2",3,4]) -> "1[2][3][4]" """
    if len(layer) == 1:
        return layer[0]
    else:
        _list = ["[{}]".format(k) for k in layer[1:]]
        return layer[0] + "".join(_list)


def flat_dict(_dict):
    """ 展开嵌套字典，返回一个单层字典。 """
    if not isinstance(_dict, dict):
        raise TypeError("argument must be a dict, not {}".format(type(_dict)))
    def __flat_dict(pre_layer, value):
        result = {}
        for k, v in value.items():
            layer = pre_layer[:]
            layer.append(k)
            if isinstance(v, dict):
                result.update(__flat_dict(layer,v))
            else:
                result[flat_key(layer)] = v
        return result
    return __flat_dict([], _dict)


# sample
if __name__ == "__main__":
    payload = {"status": 200,
                "body": {"id": 1,
                        "msg": "hello"}
                }
    _dict = flat_dict(payload)
    print(_dict.items())