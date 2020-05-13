#!/usr/bin/env python 
#coding:utf-8


def f(filename):
    Xlist=[]
    fd = open(filename,"r")
    for line in fd.readlines():
        Xlist.append(line.strip())
        print "%s is %s " % (filename,len(Xlist))
        return Xlist
    fd.close()


if __name__ == "__main__":
    A='A.txt'
    B='B.txt'    
    
    Alist=f(A)
    Blist=f(B)
    
    
    #Alist and Blist 相同行
    ret_list1 = list((set(Alist).union(set(Blist)))^(set(Alist)^set(Blist)))
    print "A-B same %s" % len(ret_list1)
    
    
    #Alist and Blist 合并去重
    ret_list2 = list(set(Alist).union(set(Blist)))  
    print "A-B all %s" % len(ret_list2)
    
    
    #Blist 去重
    NewBlist= list(set(Blist))
    print "Blist" % len(NewBlist)