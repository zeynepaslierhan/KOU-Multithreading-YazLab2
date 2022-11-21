import Threshold_comparison_csv as th_csv
import Divide_csv as dv_csv
import threading
import time

def searching_with_mutlithreading(column,threshold,thread):
    
    if thread == 1:
        dv_csv.divide_csvFile(1)
        t = threading.Thread(target = th_csv.threshold_func,args =(0,0,column,threshold))
        t.start()
        t.join()
    
    else:
        if thread % 2 == 0:
            thread= thread + 1

        dv_csv.divide_csvFile(thread-2)
        threads=[]
        j=0

        for i in range(thread-2):
            t = threading.Thread(target = th_csv.threshold_func,args =(j,j,column,threshold))
            threads.append(t)
            t.start()
            j=j+1
        
        for i in range(thread-3):
            t = threading.Thread(target = th_csv.threshold_func, name='thread{}'.format(j),args =(i,i+1,column,threshold))
            threads.append(t)
            t.start()
    
        for i in thread:
            i.join()
