# Сравнение списков
import collections

l1 = ['asd', 20, 30, 40, 50]
l2 = [30, 20, 'asd', 50, 40]

if collections.Counter(l1) == collections.Counter(l2):
	print ("Lists l1 and l2 same")
else:
	print ("Lists l1 and l2 not same")
