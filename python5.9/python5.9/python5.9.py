
a = []

with open('D:\\python作业\\text-file-process\\log_files\\201811113005.log', mode='r',encoding='UTF-8') as f:
    for l in f:
       ll=l.split('：')[2]
       lll=ll.split(',')[0]
       a.append(lll)
print(a.count('201811113005'))
