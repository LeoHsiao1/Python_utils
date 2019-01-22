import tkinter
from tkinter import messagebox


tk_main = tkinter.Tk()

tk_main.attributes("-topmost", True,     # 使该窗口置顶
                   #"-fullscreen", True,  # 使该窗口为全屏
                   #"-disabled", True,    # 使该窗口无法操作（用户对它的点击、输入统统无效）
                   #"-toolwindow", True,  # 使该窗口为toolwindow
                   #"-alpha", 0.9,        # 设置该窗口的透明度，0代表完全透明，1代表完全不透明
                   )


img = tkinter.PhotoImage(file=r"C:\Users\Will\Desktop\scene.png", width=200, height=100)


tk_main.mainloop()

