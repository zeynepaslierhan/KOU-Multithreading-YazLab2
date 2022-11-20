import similarity as sm

import pandas as pd

def sm_onData(column, threshold):
    data = pd.read_csv("C:/Users/zerha/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/littleData.csv")

    CsvLen= (len(data))
    print("CSV Satır sayısı="+str(CsvLen-1)+"\n")

    # Son satıra kadar okuma işlemi yapar
    with open("C:/Users/zerha/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/littleData.csv") as file:
        content = file.readlines()
        for i in range(1,CsvLen+1):
            print("------------------------------------------------------------")
            rows = content[i:]
            ListRow1=rows[0].split(",")
            print(ListRow1[column])
            print("---------------")
            for j in range(i+1,CsvLen+1):
                rows = content[j:]
                ListRow2=rows[0].split(",")
                threshold2=sm.similarity(ListRow1[column],ListRow2[column])
                if threshold2 >= threshold:
                    print(ListRow2[column])
                    print(threshold2)