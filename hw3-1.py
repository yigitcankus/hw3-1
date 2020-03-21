import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics
import math

"""
numpy kütüphanesini kullanarak üreteceğiniz 3 farklı veri aracılığı ile merkezi eğilim ve dağılım ölçümlerini 
hem yukarıda verilen matematiksel formülle hem de python'da hazır bulunan (built-in) kodlar aracılığıyla analiz edin!!!
"""

"""
ortalama,medyan,mod,varyans, standart sapma,standart hata
"""
####ortalama
veri1= np.array([1,2,3,4,5,8,8,11,12,13,14,15])

veri1_sum = veri1.sum()
veri1_len=len(veri1)
veri1_mean=veri1_sum/veri1_len
print(veri1_mean)

veri1_mean_np= np.mean(veri1)
print(veri1_mean_np)

##################

####medyan

veri1_medyan = 0
if len(veri1)%2==0:
    veri1_medyan= (veri1[(veri1_len-1)//2]+veri1[veri1_len//2]) / 2
else:
    veri1_medyan=veri1[veri1_len//2]
print(veri1_medyan)

veri1_medyan_np = np.median(veri1)
print(veri1_mean_np)

################

####mod

veri1_mod=statistics.mode(veri1)
print(veri1_mod)

##paketsiz nasıl yapılır, yapamadım

#################

### varyans
var_total = 0
for i in veri1:
    var_total = var_total + ((i-veri1_mean_np)**2 / (veri1_len-1))
print(var_total)

print(statistics.variance(veri1))

np_var=np.var((veri1), ddof=1)

print(np_var)

#################

###standart sapma

std_total = 0
for i in veri1:
    std_total = std_total + ((i - veri1_mean_np) ** 2 / (veri1_len - 1))

std= math.sqrt(std_total)
print(std)
std_math = math.sqrt(np_var)
print(std_math)

np_std = np.std(veri1, ddof=1)
print(np.std) ######## neden olmuyor anlamadım

##########

####standart hata

std_error = std / math.sqrt(veri1_len)
print(std_error)




