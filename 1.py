import hashlib

h = hashlib.sha256()    # 生成一个hash器
h.update("Hello".encode())      # 输入要hash的内容（必须转换成bytes类型）
h.update("World".encode())
h.digest()              # 获取hash结果（也是bytes类型）

# 简化成一步
hashlib.sha256(b"Hello World").digest()

# 通过对原始口令加一个复杂字符串来实现，俗成“加盐
# 加盐、加用户名