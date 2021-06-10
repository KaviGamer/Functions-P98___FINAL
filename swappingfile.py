def swapFileData():
    ar = open('sample1.txt','r')
    br = open('sample2.txt','r')
    data_a = ar.read()
    data_b = br.read()
    aw = open('sample1.txt','w')
    aw.write(data_b)
    aw.close()
    bw = open('sample2.txt','w')
    bw.write(data_a)
    bw.close()

swapFileData();

print("Process Complete!")