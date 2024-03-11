# ProPresenterBibles


Репозиторий с исправленными русскими переводами библии для `ProPresenter 7`

- Исправлены все опечатки в Синодальном переводе (RST) для macOS и Windows
- Добавлен [Новый русский перевод (NRT)](https://www.bible.com/ru/bible/143/GEN.1.%D0%9D%D0%A0%D0%9F) для macOS и Windows. Перевод взят из [VisioBible](https://www.visiobible.org.ua/?page=main)
- Добавлен [Новый русский перевод (IBS)](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html) для macOS и Windows
- Добавлен [Библия под ред. М.П. Кулакова и М.М. Кулакова (BTI)](https://www.bible.com/ru/bible/313/GEN.1.BTI) для macOS и Windows. Перевод взят из [Институт перевода Библии в Заокском](https://www.ph4.org/b4_1.php)


## Различие [NRT](https://www.bible.com/ru/bible/143/GEN.1.%D0%9D%D0%A0%D0%9F) и [IBS](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html) переводов
   Если вы не знаете какой перевод вам нужен, то вам нужен [NRT](https://www.bible.com/ru/bible/143/GEN.1.%D0%9D%D0%A0%D0%9F). Именно этот перевод используется в [YouVersion](https://www.bible.com/).


## Описание версий

#### 0.5

- Добавлен [Библия под ред. М.П. Кулакова и М.М. Кулакова (BTI)](https://www.bible.com/ru/bible/313/GEN.1.BTI) для macOS и Windows. Перевод взят из [Институт перевода Библии в Заокском](https://www.ph4.org/b4_1.php)


#### 0.4

- Добавлен [Новый русский перевод (NRT)](https://www.bible.com/ru/bible/143/GEN.1.%D0%9D%D0%A0%D0%9F) Для macOS и Windows. Перевод взят из [VisioBible](https://www.visiobible.org.ua/?page=main)


#### 0.3

- Для Синодального перевода (RST) за основу взят перевод из [VisioBible](https://www.visiobible.org.ua/?page=main) 

#### 0.2

- Какие-то фиксы


## Скачать необходимые файлы

1. Выбрать последний релиз:

![image](https://user-images.githubusercontent.com/15382949/123510831-0d829700-d697-11eb-95c7-16e981aea303.png)

2. Скачать архив `artifat.zip`:

![image](https://user-images.githubusercontent.com/15382949/123510839-1e330d00-d697-11eb-86c8-65d8700eb8be.png)

---

### Установка Windows

#### Синодальный перевод (RST)
1. Запустить `ProPresenter`
2. Установить Синодальный русский перевод

![image](https://user-images.githubusercontent.com/15382949/123508598-d5288c00-d689-11eb-9d18-f911955cec48.png)

3. Закрыть `ProPresenter`
4. Перейти в каталог `C:\ProgramData\RenewedVision\ProPresenter\Bibles`
5. Открыть файл `BibleData.proPref` в текстовом редакторе (блокноте)
6. В файле найти название каталога, который отвечает за Синодальный перевод и перейти в него (на скриншоте - это `eeac8c52-b8a1-4efa-b526-4c5de7490f2a`, соответственно полный путь к каталогу в который надо перейти выглядит так: `C:\ProgramData\RenewedVision\ProPresenter\Bibles\eeac8c52-b8a1-4efa-b526-4c5de7490f2a`) 

![image](https://user-images.githubusercontent.com/15382949/123508776-ee7e0800-d68a-11eb-87cb-c9bbfdd9d759.png)

7. Заменить файл `bible.db3` на `res\Windows\Russian Synodal Translation (SYN)\bible.db3` из скачанного архива
8. Открыть `ProPresenter` и убедиться, что исправления подтянулись (Псалтирь 54:1)

---

#### Новый русский перевод [NRT](https://www.bible.com/ru/bible/143/GEN.1.%D0%9D%D0%A0%D0%9F) или [IBS](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html)

**Одновременно оба перевода установить нельзя**

1. Запустить `ProPresenter`
2. Установить библию `A Conservative Version` из стандартной библиотеки `ProPresenter`

![image](https://user-images.githubusercontent.com/15382949/123509033-af50b680-d68c-11eb-95ff-361e4ed0ae16.png)

3. Закрыть `ProPresenter`
4. Перейти в каталог `C:\ProgramData\RenewedVision\ProPresenter\Bibles`
5. Открыть файл `BibleData.proPref` в текстовом редакторе (блокноте)
6. В файле найти название каталога, который отвечает за `A Conservative Version` и перейти в него (на скриншоте - это `77f2a51a-5539-42e0-8e22-4cf74847d339`, соответственно полный путь к каталогу в который надо перейти выглядит так: `C:\ProgramData\RenewedVision\ProPresenter\Bibles\77f2a51a-5539-42e0-8e22-4cf74847d339`) 

![image](https://user-images.githubusercontent.com/15382949/123509100-0bb3d600-d68d-11eb-995f-e48ab68a68c7.png)

7. Заменить файлы `bible.db3` и `rvmetadata.xml` на файлы из скачанного архива: 
- Для NRT перевода: `res\Windows\New Russian Translation (NRT)`
- Для IBS перевода: `res\Windows\International Bible Society (IBS)`
8. Открыть `ProPresenter` и убедиться, что появился новый перевод `New Russian Translation` 

![image](https://user-images.githubusercontent.com/15382949/123509520-6e0dd600-d68f-11eb-913a-295feee101f0.png)

---

#### Библия под ред. М.П. Кулакова и М.М. Кулакова (BTI) [Пример](https://www.bible.com/ru/bible/313/GEN.1.BTI)

1. Запустить `ProPresenter`
2. Установить библию `Geneva Bible (1599) (Geneva)` из стандартной библиотеки `ProPresenter`

![image](https://github.com/SlowBroshka/ProPresenterBibles/assets/15382949/3e41089a-3b5e-4b23-a56f-54f38c8e1ff8)

3. Закрыть `ProPresenter`
4. Перейти в каталог `C:\ProgramData\RenewedVision\ProPresenter\Bibles`
5. Открыть файл `BibleData.proPref` в текстовом редакторе (блокноте)
6. В файле найти название каталога, который отвечает за `Geneva Bible (1599) (Geneva)` и перейти в него (на скриншоте - это `9b221d86-9910-4a89-b8fb-9b345f713693`, соответственно полный путь к каталогу в который надо перейти выглядит так: `C:\ProgramData\RenewedVision\ProPresenter\Bibles\9b221d86-9910-4a89-b8fb-9b345f713693`) 

![image](https://github.com/SlowBroshka/ProPresenterBibles/assets/15382949/13840982-914d-4485-b8a2-ea57a0224f7a)
![image](https://github.com/SlowBroshka/ProPresenterBibles/assets/15382949/7b9e706d-47f8-4fd0-84d2-f46c6e6b3637)


7. Заменить файлы `bible.db3` и `rvmetadata.xml` на файлы из скачанного архива `res\Windows\Bible Translation Institute at Zaoksky (BTI)`
8. Открыть `ProPresenter` и убедиться, что появился новый перевод `(BTI) Bible Translation Institute at Zaoksky` 

---

### Установка macOS

#### Синодальный перевод

1. Файл `res\MacOS\Russian Synodal Translation (SYN)\ntc-rst-ru.rvbible` скопировать в каталог `/Library/Application Support/RenewedVision/RVBibles/v2/`
2. Запустить `ProPresenter`
3. Убедиться, что появился новый перевод `(NTC) Russian Synodal Translation`
   ![Снимок экрана 2021-06-14 в 18 18 28](https://user-images.githubusercontent.com/15382949/123508496-4ae02800-d689-11eb-9b6c-b3fbed078172.png)


#### Новый русский перевод [NRT](https://www.bible.com/ru/bible/143/GEN.1.%D0%9D%D0%A0%D0%9F) или [IBS](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html)

**Одновременно оба перевода установить нельзя**

##### Для [NRT](https://www.bible.com/ru/bible/143/GEN.1.%D0%9D%D0%A0%D0%9F) перевода:

1. Файл `res\MacOS\New Russian Translation (NRT)\ntc-nrt-ru.rvbible` скопировать в каталог `/Library/Application Support/RenewedVision/RVBibles/v2/`
2. Запустить `ProPresenter`

##### Для [IBS](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html) перевода:
1. Файл `res\MacOS\International Bible Society (IBS)\ntc-ibs-ru.rvbible` скопировать в каталог `/Library/Application Support/RenewedVision/RVBibles/v2/`
2. Запустить `ProPresenter`


#### Библия под ред. М.П. Кулакова и М.М. Кулакова (BTI) [Пример](https://www.bible.com/ru/bible/313/GEN.1.BTI)

##### Для [IBS](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html) перевода:
1. Файл `res\MacOS\Bible Translation Institute at Zaoksky (BTI)\ntc-bti-ru.rvbible` скопировать в каталог `/Library/Application Support/RenewedVision/RVBibles/v2/`
2. Запустить `ProPresenter`


---

## Примеры исправлений

#### Удалены лишние символы
- Стандартный синодальный перевод в `ProPresenter 7`
![image](https://user-images.githubusercontent.com/15382949/123508125-defcc000-d686-11eb-9bdb-d9dbfc32f8eb.png)
- Исправленный синодальный перевод
![image](https://user-images.githubusercontent.com/15382949/123508329-26378080-d688-11eb-97af-f20a1d7f35e3.png)

#### Заменены кавычки
- Стандартный синодальный перевод в `ProPresenter 7`
![image](https://user-images.githubusercontent.com/15382949/123508153-153a3f80-d687-11eb-95b0-2c0deabc709c.png)
- Исправленный синодальный перевод
![image](https://user-images.githubusercontent.com/15382949/123508333-318aac00-d688-11eb-9788-182d9e8badbb.png)

#### Двойное тире заменено на длинное
- Стандартный синодальный перевод в `ProPresenter 7`
![image](https://user-images.githubusercontent.com/15382949/123508141-fd62bb80-d686-11eb-8807-47e911290c13.png)
- Исправленный синодальный перевод
![image](https://user-images.githubusercontent.com/15382949/123508339-3bacaa80-d688-11eb-9bdc-8ae4acd8003d.png)
