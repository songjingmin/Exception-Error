# 使用文件
poem = '''\
Programming is fun
When the work is done
if you wanna make the work also fun:
		use Python!
'''
class file():
	pass
f = file('poem.txt', 'w')
f.write(poem)
f.close()


f = file('poem.txt')
while True:
	line = f.readline()
	if len(line) == 0:
		break
	print (line),
f.close()