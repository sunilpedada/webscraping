import sys
import urllib.request
import csv
import pandas
from matplotlib import pyplot
import cx_Oracle
from tkinter import *
if __name__=="__main__":
    stock_list=[]
    outputfile_list=[]
    with open("stock_list.txt",'r') as listofstock:
        for eachline in listofstock.readlines():
            if len(eachline)!=1:
                stock_list.append(eachline[0:len(eachline)-1])
   # print(stock_list)
    print(len(stock_list))
    urllib.request.urlopen("http://api.kibot.com/?action=login&user=guest&password=guest")
    conn=cx_Oracle.connect("system","123456","localhost:1521/orcl")
    cur=conn.cursor()
    for stock_numbers in stock_list:
        filname=str(stock_numbers)+"His.csv"
        print(filname)
        resp=urllib.request.urlopen("http://api.kibot.com/?action=history&symbol="+stock_numbers+"&interval=daily&period="+sys.argv[1])
        html=resp.read()
        data=html.decode('utf-8')
        lst=data.split()
        #print(lst)
        x=open(filname,'w')
        ex=csv.writer(x)
        ex.writerow(["symbal","data","open","high","low","close","volume"])
        for p in lst:
            line=stock_numbers+","+p
            lst=line.split(",")
            print(lst)
            sy=lst[0]
            #print(sy)
            dt=lst[1]
            op=float(lst[2])
            hi=float(lst[3])
            lo=float(lst[4])
            cl=float(lst[5])
            vi=int(lst[6])
            rows=[(str(sy)+","+str(dt)+","+str(op)+","+str(hi)+","+str(lo)+","+str(cl)+","+str(vi))]
            cur.bindarraysize=10
            cur.executemany("insert into stock_list(SY,DT,OP,HI,LO,CL,VI) values(:1,:2,:3,:4,:5,:6,:7)",rows)
            conn.commit()
            ex.writerow(lst)
        x.close()
    cur.close()
    conn.commit()
