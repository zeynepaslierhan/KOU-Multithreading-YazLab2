# MongoDb işlemleri için gerekli kütüphaneler eklendi
import pymongo
import pandas as pd
import similarity as sm

# Cluster için bağlantı sağlandı.
myclient = pymongo.MongoClient("mongodb://zeynep:1234@ac-hfldnho-shard-00-00.z9rxq6v.mongodb.net:27017,ac-hfldnho-shard-00-01.z9rxq6v.mongodb.net:27017,ac-hfldnho-shard-00-02.z9rxq6v.mongodb.net:27017/?ssl=true&replicaSet=atlas-jk8908-shard-0&retryWrites=true&w=majority") 

# Kullanacağımız veritabanı için erişim sağladık.
mydb = myclient["Mutlithreading"]

# Bilgisayar Veritabanındaki koleksiyonuna erişim sağladık
mycollection= mydb["Similarity"]

def threshold_func(file1,file2,column,threshold):

    fileName1='C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/divided_CsvFile/'+str(file1)+".csv"
    print(fileName1)
    fileName2='C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/divided_CsvFile/'+str(file2)+".csv"
    print(fileName2)


    # Veri aktarmadan önce koleksiyon içeriğini tamamen siliyoruz.
    mycollection.delete_many({})

    data = pd.read_csv(fileName1)
    len_file1= (len(data))
    print("1.csv Satır sayısı="+str(len_file1)+"\n")

    data = pd.read_csv(str(file2)+".csv")
    len_file2= (len(data))
    print("2.csv Satır sayısı="+str(len_file2)+"\n")

    with open(fileName1) as file1:
        content1 = file1.readlines()

        for i in range(len_file1):
            print("________________________________________________")
            rows = content1[i:]
            ListRow1=rows[0].split(",")
            print(ListRow1[column])
            print("---")

            with open(fileName2) as file2: 
                content2 = file2.readlines() 
                for j in range(len_file2):
                    if fileName1 == fileName2: # Tek bir csv dosyasınında kendi için karşılaştırılması için
                        j=j+1+i
                        print(j)
                        if j > len_file2:
                            break
                    rows = content2[j:]
                    ListRow2=rows[0].split(",")
                    threshold2=sm.similarity(ListRow1[column],ListRow2[column])
                    
                    #veriyi tutan dict
                    item = {}
                    if threshold2 >= threshold:
                        print(ListRow2[column])

                        item["Product 1"] = ListRow1[1]
                        item["Issue 1"] = ListRow1[2]
                        item["Company 1"]=ListRow1[3]
                        item["State 1"]=ListRow1[4]
                        item["ZIP code 1"]=ListRow1[5]
                        item["Complaint ID 1"]=ListRow1[6]

                        item["Product 2"] = ListRow2[1]
                        item["Issue 2"] = ListRow2[2]
                        item["Company 2"]=ListRow2[3]
                        item["State 2"]=ListRow2[4]
                        item["ZIP code 2"]=ListRow2[5]
                        item["Complaint ID 2"]=ListRow2[6]

                        item["threshold"] = threshold2

                        mycollection.insert_one(item)
                        item.clear()
                        
                        print(threshold2)
                        print("-")

