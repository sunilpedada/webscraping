import sys
import urllib.request
import csv
import pandas
from matplotlib import pyplot as plt
import cx_Oracle
from tkinter import *
if __name__=="__main__":
    stock_list=[]
    outputfile_list=[]
    with open("stock_list.txt",'r') as listofstock:
        for eachline in listofstock.readlines():
            if len(eachline)!=1:
                stock_list.append(eachline[0:len(eachline)-1])
    print(stock_list)
    #print(len(stock_list))
    urllib.request.urlopen("http://api.kibot.com/?action=login&user=guest&password=guest")
    #conn=cx_Oracle.connect("system","123456","localhost:1521/orcl")
    #cur=conn.cursor()
    for stock_numbers in stock_list:
        filname=str(stock_numbers)+"His.csv"
        #print(filname)
        resp=urllib.request.urlopen("http://api.kibot.com/?action=history&symbol="+stock_numbers+"&interval=daily&period="+sys.argv[1])
        html=resp.read()
        data=html.decode('utf-8')
        lst=data.split()
        #print(lst)
        x=open(filname,'w')
        ex=csv.writer(x)
        ex.writerow(["symbal","date","open","high","low","close","volume"])
        for p in lst:
            line=stock_numbers+","+p
            lst=line.split(",")
            #print(lst)
            sy=lst[0]
            dt=lst[1]
            op=float(lst[2])
            hi=float(lst[3])
            lo=float(lst[4])
            cl=float(lst[5])
            vi=int(lst[6])
            row=[(sy,dt,op,hi,lo,cl,vi)]
            #print(row)
            #cur.executemany("insert into stock_list(SY,DT,OP,HI,LO,CL,VI) values(:1,:2,:3,:4,:5,:6,:7)",row)
            ex.writerow(lst)
        x.close()
    #cur.close()
    master=Tk()
    variable1=StringVar(master)
    variable1.set(stock_list[0])
    w=OptionMenu(master,variable1,*stock_list)
    w.pack()
    variable2=StringVar(master)
    variable2.set(stock_list[0])
    w=OptionMenu(master,variable2,*stock_list)
    w.pack()
    def compare():
        v1=variable1.get()
        v2=variable2.get()
        print(v1)
        print(v2)
        f1=v1+"His.csv"
        f2=v2+"His.csv"
        print(f1)
        print(f2)
        r1=pandas.read_csv(f1)
        r2=pandas.read_csv(f2)
        print(r1)
        print(r2)
        lst1=list(r1["close"])
        lst2=list(r2["close"])
        x=range(1,len(lst1)+1)
        plt.plot(x,lst1,label=v1)
        plt.plot(x,lst2,label=v2)
        plt.xlabel('days')
        plt.ylabel("closeprice")
        plt.legend()
        plt.show()
    button=Button(master,text="compare",command=compare)
    button.pack()
    mainloop()
    #conn.close()