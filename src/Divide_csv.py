

def divide_csvFile(lines_divided_number,filename):
    csvfile = open("C:/Users/zerha/Documents/GitHub/KOU-Multithreading-YazLab2/src/data_set/littleData.csv", 'r').readlines()
    for i in range(len(csvfile)):
        if i % lines_divided_number == 0:
            if i == 0: #Sütun bilgilerinin bölünmüş dosyalarda yazılmaması için
                open('C:/Users/zerha/Documents/GitHub/KOU-Multithreading-YazLab2/src/divided_CsvFile/'+ str(filename) + '.csv', 'w+').writelines(csvfile[i+1:i+lines_divided_number])
            else:
                open('C:/Users/zerha/Documents/GitHub/KOU-Multithreading-YazLab2/src/divided_CsvFile/'+ str(filename) + '.csv', 'w+').writelines(csvfile[i:i+lines_divided_number])
            filename += 1
    return filename