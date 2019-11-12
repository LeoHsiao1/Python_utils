"""
setup.py file for SWIG
"""

from distutils.core import setup, Extension


module = Extension('_api',
                   sources=['api.c', 'api_wrap.c'],
                   )

setup(name='api',
      ext_modules=[module],
      py_modules=["api"],
      )
