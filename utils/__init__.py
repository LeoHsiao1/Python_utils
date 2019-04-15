"""
一个自定义的包，包含一些可通用的模块。
  - 可以将该包拷贝到其它项目中使用，也可以作为git的submodule被其它项目引用。
  - 保持 https://github.com/LeoHsiao1/test_Python.git 处的utils包为最新版本。
"""


__all__ = ["use_io", "use_os", "use_time", "use_form", "use_log", "use_plot"]


for i in __all__:
    from . import i
