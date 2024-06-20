'''
ip:
7262 seconds
op:
2hr:1min:2sec
'''
seconds=7262
minutes=0
hrs=0
sec=0
hrs=seconds//3600
seconds=seconds-3600*hrs
minutes=seconds//60
seconds=seconds-minutes*60
sec=seconds
print(hrs,"hr:",minutes,"min:",sec,"sec")