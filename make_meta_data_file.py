import os
import sys

folder1=input("Please enter the name of folder: ")
libsiz=input("Please enter the size of library: ")
fileoutput=open("meta-data2.txt","w")
fileoutput.write("SampleID"+"\t"+"Name"+'\t'+'Category'+'\t'+'ReadLength'+'\n')

d1=[]  #####whole length
for root,dirs,files in os.walk(folder1):
    for file in files:
        d1.append(str(file).replace(".fa","").replace(".gz","").replace("_1.fq","").replace("_2.fq",""))
d2=list(set(d1))

for i in d2:
    num= d2.index(i)+1
    fileoutput.write(str(num)+ '\t'+str(i)+'\t'+'influent'+'\t'+libsiz+'\n')


fileoutput.close()
    

