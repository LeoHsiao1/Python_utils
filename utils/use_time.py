import time
import threading

print(__file__)
print(__name__)

class _Clock:
    """
    自定义的时钟类，用于获取几种不同格式的当前时间。
     decimal：设置time_float的精度，控制其保留几位小数。
     time_diff：设置该时钟与UTC+0时区的时差。如果不设置，会自动采用
     本地时区。
    """

    def __init__(self, name=None, decimal=3, time_diff=None):
        self.name = name
        self.decimal = decimal
        self.time_diff = time_diff
        self.time_format = "%Y/%m/%d %H:%M:%S"  # 时间字符串的格式

    @property
    def time_float(self):
        """ UTC+0时区的时间戳，精度由self.decimal决定 """
        return round(time.time(), self.decimal)

    @property
    def time_int(self):
        """ UTC+0时区的时间戳，精度为秒 """
        return int(time.time())

    @property
    def time_tuple(self):
        """ 本地时区的时间元组 """
        if self.time_diff == None:
            return time.localtime(self.time_int)
        else:
            return time.gmtime(self.time_int+self.time_diff)

    @property
    def time_str(self):
        """ 本地时间的格式化字符串 """
        return time.strftime(self.time_format, self.time_tuple)


class Timer(_Clock):

    """
    自定义的计时器，像秒表一样，可以随时查看当前计时、暂停计时、继续计时。
     · 创建一个计时器之后，它就会开始计时，但并不需要创建一个线程。
     · 可直接调用_Clock类的几个方法来获取当前时间。
    """

    def __init__(self, *args, **kwargs):
        _Clock.__init__(self, *args, **kwargs)
        self.record = []  # 记录每次使用的 (开始时刻,暂停时刻,计时时长)
        self.status = "initial"
        self.go()

    @property
    def count(self):
        """ 当前计时值 """
        count = 0
        for line in self.record:
            if line[2] == None:
                count += self.time_float - line[0]
            else:
                count += line[2]
        return round(count, self.decimal)

    def go(self):
        """ 开始计时 """
        if self.status != "timing":
            self.record.append((self.time_float, None, None))
            self.status = "timing"

    def pause(self):
        """ 暂停计时 """
        # 如果该计时器在计时中，就暂停它，并计算这一段的计时时长
        if self.status == "timing":
            last_line = self.record[-1]
            self.record.remove(last_line)
            current_time = self.time_float
            self.record.append(
                (last_line[0], current_time, round(current_time - last_line[0], self.decimal)))
            self.status = "paused"


class Schedule(threading.Thread):
    """
    自定义的定时任务表，添加第一个定时任务后就创建一个线程，开始循环检查
    是否执行任务表中的任务。
     · 调用stop()来终止该线程。
    """

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self._askToStop = False
        self._schedule = []  # 保存定时任务表
        self.status = "initial"

    def _get_time(self):
        """ 获取当前时间 """
        return time.time()

    def addTask(self, countDown, func, *args, **kwargs):
        """ 
        在任务表中增加一项定时任务：在倒计时countDown结束之后调用
        函数func，并传入参数*args和**kwargs。
         · 定时任务只会被执行一次，执行后就会被从任务表中删除。
         · 定时任务只会在倒计时结束之后被执行，但无法保证无延迟。
        """
        if self.status == "initial":  # 第一次添加定时任务时创建一个新线程
            self.status = "running"
            self.start()

        task = []
        if isinstance(countDown, (int, float)) and countDown > 0:
            task.append(self._get_time()+countDown)  # 准备在指定时刻执行该任务
        else:
            raise ValueError("'countDown' must be a positive int or float.")
        if callable(func):
            task.append(func)
        else:
            raise ValueError("'func' must be callable.")
        task.append(args)  # 保存元组参数
        task.append(kwargs)  # 保存字典参数

        self._schedule.append(task)
        self._schedule.sort(key=lambda task: task[0])  # 将任务表按时间戳的大小排序

    def _doTask(self):
        """ 检查任务表中各项任务的时间，判断是否要执行它。 """
        current_time = self._get_time()
        i = 0
        while i < len(self._schedule):  # 遍历任务表
            task = self._schedule[i]
            if task[0] <= current_time:
                # 如果该任务的时间不晚于当前时间，就创建一个线程去执行该任务，避免阻塞定时器线程
                t1 = CreatThread(task[1], *task[2], **task[3])
                t1.start()
                i += 1
            else:
                break  # 如果该任务的时间戳大于当前时间，就提前结束遍历

        del self._schedule[:i]  # 删除过时的任务

    def run(self):
        """ 线程循环运行的内容 """
        while not self._askToStop:
            self._doTask()

        # 结束时进行清理
        self.status == "stopped"
        return 0

    def stop(self):
        self._askToStop = True


class CreatThread(threading.Thread):
    """ 一个简单的创建线程的类 """

    def __init__(self, func, *args, **kwargs):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, **self.kwargs)


""" sample """
if __name__ == "__main__":

    t1 = Timer("t1")
    s1 = Schedule(name="s1")

    def test(*args):
        print(*args)
        print(t1.count, t1.time_float, t1.time_str)
        if t1.count >= 10:
            s1.stop()
        s1.addTask(1.0, test, *args)

    s1.addTask(1.0, test, "test...")
