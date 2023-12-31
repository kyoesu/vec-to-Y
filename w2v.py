# -*- coding: utf-8 -*-
"""w2v.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1we1I9fxWfbXr9e1jwVWaP-ySNmW9Hy0T

# `открытие доков`
"""

texts = []
file_paths = ['Berezin-Gruppa_Trevilja.txt', 'Burmistrov_D._Anomaliya.txt', 'Divov_S.W.A.L.K.E.R._Pohititeli_artefaktov.290495.txt', 'guttaperchevyy-malchik.txt','kavkazskiy-plennik.txt','Klin.txt',
              'Melnik_Sektor_obstrela.244283.txt','Pervushin_Lvinoe_Serdtse.270984.txt','Proshkin__Ovchinnikov-Palachi_Smertniki-2_.txt','russian.txt','svetlana-1.txt','Tumanovskij-Dva_mutanta.txt',
              'Vardunas_I._S_W_A_L_K_E_R_Bayiki_Iz_B.txt','voina-i-mir-tom-5-liev-tolstoi.txt','Vyistavnoy_Buka_2_Tvar.392067.txt',
              '47598319.txt','60366138.txt','avidreaders.ru__skazka-o-mertvoy-carevne-i-o1.txt','avidreaders.ru__zapiski-iz-mertvogo-doma.txt','bednaya-liza.txt','bednye-lyudi.txt','belye-nochi.txt',
             'besy.txt','Velikii_inkvizitor.txt','dubrovskiy.txt','evgeniy-onegin.txt','idiot.txt','igrok1.txt','kapitanskaya-dochka.txt', "Lomonosov-Mihail.-Ody.-Stihotvoreniya.txt", "marfa-posadnica.txt",
              "mednyy-vsadnik.txt", "mixail-lomonosov-sluchilis-vmeste-dva-astronoma-v-piru.txt",  "oda_na_den.txt", "pesn-o-veschem-olege.txt", "prestuplenie-i-nakazanie_1418.txt", "skaz_o_carevne_i_7_bog.txt",
              "treadovski_vasili.txt" ]
d=["taras-bulba.txt","skazka-o-care-saltane.txt","povesti-belkina.txt","poltava.txt","podrostok.txt","natalya-boyarskaya-doch.txt","Mayakovskiy Vladimir. Sborniki stihotvoreniy - BooksCafe.Net.txt","Lomonosov Mihail. Ody. Stihotvoreniya.txt"]
for file_path in file_paths:
    file_path = "/content/drive/MyDrive/books/" + file_path
    with open(file_path, encoding='utf-8') as f:
        print(file_path)
        text = f.read()
        texts.append(text)

"""# `преобразование текста`"""

import nltk
nltk.download('punkt')



import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

#stop_words = set(stopwords.words('russian'))
stop_words=[]
processed_texts = []

for text in texts:
    # Удаление символов пунктуации и приведение к нижнему регистру
    text = re.sub(r'[^\w\s]', '', text.lower())

    # Токенизация текста
    tokens = word_tokenize(text)

    # Удаление стоп-слов
    filtered_tokens = [token for token in tokens if token not in stop_words]

    # Добавление предобработанных текстов в список
    processed_texts.append(filtered_tokens)

print(processed_texts[0:1])

"""# `создание модели w2v`"""

from gensim.models import Word2Vec

model_w2v = Word2Vec(processed_texts, vector_size=1000, window=10, min_count=2, epochs=15)

vector = model_w2v.wv['программа']
#print(vector)

with open("/content/drive/MyDrive/books/russian.txt", encoding='utf-8') as f:
    text = f.read()

word_set=text.split("\n")


missing_words = []
for word in word_set:
    if word not in model_w2v.wv.key_to_index:
        missing_words.append(word)

print("Отсутствующие слова: ", missing_words[:50])

print(len(missing_words))
print(len(word_set))

"""
|<font size="4"> **i**</font> | <font size="4">**word_set** | <font size="4">**missing_words** | <font size="4">**good_res**</font> |
|:-:|:--------:|:-------------:|:------:|
|<font size="4"> 1 |<font size="4">  1532629 |<font size="4">   1412705     |<font size="4"> 119924 |
| <font size="4">2 |<font size="4">  1532629 |<font size="4">  1372969|<font size="4">  159 660|
|<font size="4"> 3 |<font size="4">  1532629 |<font size="4">  |<font size="4">  |




"""

!git init