s = input('Enter something -->')
# 终端上运行出现错误为 ：Enter somethingTraceback (most recent call last):
  # File "try_except.py", line 1, in <module>
  #  s = input('Enter something')
# EOFError

# 处理异常

import sys
try:
	s = input('Enter something -->')  
except EOFError:
	print('\nWhy did you do an EOF on me?')
	sys.exit()
except:
	print('\nSome error/exception occurred.')
print('Done')