import os

def Remove_file(file_path,file_type):
   
    num = 0
    count = 1
    total = 0

    for line in enumerate(open(file_path,'r')):
        total += 1
    print (total)

    for num in range(843000, total):
        path = '../../DATA/%s/%s/%s.jpg' % (size, file_type, num)
        if path not in name:
            if os.path.exists(path):
                os.remove(path) 
                count += 1
        if count % 1000 == 0:
            print("%s files has been removed, current file: %s" % (count, num))  
        if num % 10000 == 0:
            print("%s labels has been searched " % num)  
    print("%s files have been removed " % count)

net = 'Pnet'
size = '12'

item = 'imglists/PNet/train_%s_landmark.txt' % net   
dataset_dir = os.path.join('../../DATA', item)
pos_labelpath = '../../DATA/%s/pos_%s.txt' % (size, size)
neg_labelpath = '../../DATA/%s/neg_%s.txt' % (size, size)
part_labelpath = '../../DATA/%s/part_%s.txt' % (size, size)

name = list()

with open(dataset_dir, 'r') as imagelist:
    for line in imagelist.readlines():
        info = line.strip().split(' ')
        name.append(info[0])

name = name[999999:1250005]
# Remove_file(pos_labelpath, 'positive')
# Remove_file(neg_labelpath, 'negative')
Remove_file(part_labelpath, 'part')