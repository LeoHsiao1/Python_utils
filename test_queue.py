import queue

q = queue.Queue(10)
# Create a queue object with a given maximum size.
# If maxsize is <= 0, the queue size is infinite.

q.put("hello")  # Put an item into the queue，block if necessary until a free slot is available.
q.put("world", block=False) # 如果队列没有空位就不阻塞，直接抛出异常
q.put("!", timeout=1)  # 最多阻塞1秒，达到timeout时抛出异常
# def put(item, block=True, timeout=None)

q.get()  # 从队列中提取一项数据
# def get(block=True, timeout=None)

q.qsize()   # 返回队列的大小（可能在调用该函数时，队列的大小就发生了变化）


