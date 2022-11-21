# MongoDb işlemleri için gerekli kütüphaneler eklendi
import pymongo
import csv

def lastData():
    # Cluster için bağlantı sağlandı.
    myclient = pymongo.MongoClient("mongodb://zeynep:1234@ac-hfldnho-shard-00-00.z9rxq6v.mongodb.net:27017,ac-hfldnho-shard-00-01.z9rxq6v.mongodb.net:27017,ac-hfldnho-shard-00-02.z9rxq6v.mongodb.net:27017/?ssl=true&replicaSet=atlas-jk8908-shard-0&retryWrites=true&w=majority") 

    # Kullanacağımız veritabanı için erişim sağladık.
    mydb = myclient["Mutlithreading"]

    # Bilgisayar Veritabanındaki koleksiyonuna erişim sağladık
    mycollection= mydb["Similarity"]

    data=mycollection.find()
    mongo_docs = list(data)
    fileName="C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/LastData.csv"
    fields = ["Complaint ID 1","Complaint ID 2","threshold"]
    with open(fileName, 'w') as csvfile: 
        
        # creating a csv writer object 
        csvwriter = csv.writer(csvfile)
        # writing the fields 
        csvwriter.writerow(fields)
        for row in mongo_docs:
            item=[str(row["Complaint ID 1"]),str(row["Complaint ID 2"]),str(row["threshold"])]
            csvwriter.writerow(item)
            item.clear()