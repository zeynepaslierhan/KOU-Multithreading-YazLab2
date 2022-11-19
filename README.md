# KOU-Multithreading-YazLab2

## Giriş

Müşteri şikayet kayıtlarının tutulduğu bir veri seti içerisindeki benzer kayıtlar tespit edilmektedir. Tespit edilen kayıtlar masaüstü uygulamasında gösterilecektir. Multithreading kullanarak benzerlik arama süresi düşürülmektedir.

## Multithreading (Çok İş Parçacıklı Çalışma)

Multithreading (çok iş parçacıklı çalışma), bir merkezi işlem biriminin (CPU) (veya çok çekirdekli bir işlemcideki tek bir çekirdeğin) aynı anda işletim sistemi tarafından desteklenen birden çok yürütme iş parçacığı sağlama yeteneğidir.

Bu tür programlamada birden çok iş parçacığı aynı anda çalışır. Çok iş parçacıklı model, sorgulamalı olay döngüsü kullanmaz. CPU zamanı boşa harcanmaz. Boşta kalma süresi minimumdur. Daha verimli programlarla sonuçlanır. Herhangi bir nedenle bir iş parçacığı duraklatıldığında, diğer iş parçacıkları normal şekilde çalışır.

## Veri seti

Kullanılacak veri setine aşağıdaki linkten ulaşabilirsiniz:

* https://www.kaggle.com/datasets/selener/consumer-complaint-database

Bu veri seti; finansal ürünler ve hizmetler hakkında alınan gerçek dünya şikayetlerini içermektedir. Veri seti, müşterilerin Kredi Raporları, Öğrenci Kredileri, Para Transferi vb. gibi finans sektöründeki birden fazla ürün ve hizmet hakkında yaptığı şikayetlerin farklı bilgilerini içermektedir.

### Veri Setini Projede kullanabilmek için

Projede veri setini kullanabilmek için dosya uzantılarını değiştirin. Ya da:
1. src klasörü içerisine data_set klasörü ekleyin.
2. data_set klasörünü içerisine yüklenilen veri setinin ismini "originalData.csv" olarak ayarlayın.

## Kodlar

### Veri Seti Düzenleme

Veri Setinin nasıl düzenlendiğini incelemek için  [editDataset.ipynb Notebook'unu](https://github.com/zeynepaslierhan/KOU-Multithreading-YazLab2/blob/main/notebooks/editDataset.ipynb) inceleyebilirsiniz

### Benzerlik Hesaplanması

Benzerlik hesaplanmasının nasıl yapıldığını incelemek için  [similarity.ipynb Notebook'unu](https://github.com/zeynepaslierhan/KOU-Multithreading-YazLab2/blob/main/notebooks/similarity.ipynb) inceleyebilirsiniz.

### Multithreading 

Multithreading işlemlerinin nasıl yapıldığını incelemek için  [mutlithreading.ipynb Notebook'unu](https://github.com/zeynepaslierhan/KOU-Multithreading-YazLab2/blob/main/notebooks/mutlithreading.ipynb) inceleyebilirsiniz.


## Kaynakça

1. [What is Thread?](https://www.tutorialspoint.com/operating_system/os_multi_threading.htm)
2. [Multithreading Pyhton](https://www.geeksforgeeks.org/multithreading-python-set-1/)
3. [Tkinter, İbrahim EFE @WriteandLearn](https://www.youtube.com/playlist?list=PLSmHiN0iazy_qX_6Tmecj4tTOefqh2-m2)
4. [Codemy.com](https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV)
5. [TomSchimansky, Custom Tkinter](https://github.com/TomSchimansky/CustomTkinter)
6. [CSV dosyalarıyla işlemler](https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/)

