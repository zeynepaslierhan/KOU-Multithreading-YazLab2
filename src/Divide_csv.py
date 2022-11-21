def divide_csvFile(part):
    filename=0
    csvfile = open("C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/littleData.csv", 'r').readlines()
    length=len(csvfile)
    lines_divided_number=int(length/part)
    for i in range(length):
        if i % lines_divided_number == 0:
            if i == 0: #Sütun bilgilerinin bölünmüş dosyalarda yazılmaması için
                open('C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/divided_CsvFile/'+ str(filename) + '.csv', 'w+').writelines(csvfile[i+1:i+lines_divided_number])
            else:
                open('C:/Users/hkf_4/Documents/GitHub/KOU-Multithreading-YazLab2/src/divided_CsvFile/'+ str(filename) + '.csv', 'w+').writelines(csvfile[i:i+lines_divided_number])
            filename += 1
    return filename
