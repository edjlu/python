def say_hi():
    print('Hi, this is mymodule speaking')

__version__ = '0.1'

import my_module

my_module.say_hi()
print('Version', my_module.__version__)

dir()