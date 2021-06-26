# ProPresenterBibles


Репозиторий с исправленными русскими переводами библии для `ProPresentor 7`

- Исправлен синодальный перевод для Macos
- Исправлен синодальный перевод для Windows
- Добавлен [Новый русский перевод](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html) для Windows


## Скачать необходимые файлы

1. Выбрать релиз:

![image](https://user-images.githubusercontent.com/15382949/123510831-0d829700-d697-11eb-95c7-16e981aea303.png)

2. Скачать архив `artifat.zip`:

![image](https://user-images.githubusercontent.com/15382949/123510839-1e330d00-d697-11eb-86c8-65d8700eb8be.png)

---

### Установка Windows

#### Синодальный перевод
1. Запустить `ProPresentor`
2. Установить Синодальный русский перевод

![image](https://user-images.githubusercontent.com/15382949/123508598-d5288c00-d689-11eb-9d18-f911955cec48.png)

3. Закрыть `ProPresentor`
4. Перейти в каталог `C:\ProgramData\RenewedVision\ProPresenter\Bibles`
5. Открыть файл `BibleData.proPref` в текстовом редакторе (блокноте)
6. В файле найти название каталога, который отвечает за Синодальный перевод и перейти в него (на скриншоте - это `eeac8c52-b8a1-4efa-b526-4c5de7490f2a`, соответственно полный путь к каталогу в который надо перейти выглядит так: `C:\ProgramData\RenewedVision\ProPresenter\Bibles\eeac8c52-b8a1-4efa-b526-4c5de7490f2a`) 

![image](https://user-images.githubusercontent.com/15382949/123508776-ee7e0800-d68a-11eb-87cb-c9bbfdd9d759.png)

7. Заменить файл `bible.db3` на `res\Windows\Russian Synodal Translation\bible.db3` из скачанного архива
8. Открыть `ProPresentor` и убедиться, что исправления подтянулись (Псалтирь 54:1)

---

#### Новый русский перевод [ссылка](https://bookscafe.net/book/bibliya-bibliya_novyy_russkiy_perevod_ibs-200255.html)
1. Запустить `ProPresentor`
2. Установить библию `A Conservative Version` из стандартной библиотеки `ProPresentor`

![image](https://user-images.githubusercontent.com/15382949/123509033-af50b680-d68c-11eb-95ff-361e4ed0ae16.png)

3. Закрыть `ProPresentor`
4. Перейти в каталог `C:\ProgramData\RenewedVision\ProPresenter\Bibles`
5. Открыть файл `BibleData.proPref` в текстовом редакторе (блокноте)
6. В файле найти название каталога, который отвечает за `A Conservative Version` и перейти в него (на скриншоте - это `77f2a51a-5539-42e0-8e22-4cf74847d339`, соответственно полный путь к каталогу в который надо перейти выглядит так: `C:\ProgramData\RenewedVision\ProPresenter\Bibles\77f2a51a-5539-42e0-8e22-4cf74847d339`) 

![image](https://user-images.githubusercontent.com/15382949/123509100-0bb3d600-d68d-11eb-995f-e48ab68a68c7.png)

7. Заменить файлы `bible.db3` и `rvmetadata.xml` на файлы из скачанного архива `res\Windows\New Russian Translation`
8. Открыть `ProPresentor` и убедиться, что появился новый перевод `New Russian Translation` 

![image](https://user-images.githubusercontent.com/15382949/123509520-6e0dd600-d68f-11eb-913a-295feee101f0.png)

---

### Установка Windows

#### Синодальный перевод
1. Файл `res\MacOS\Russian Synodal Translation\ntc-rst-ru.rvbible` скопировать в каталог `/Library/Application Support/RenewedVision/RVBibles/v2/`
2. Запустить `ProPresentor`
3. Убедиться, что появился новый перевод `(NTC) Russian Synodal Translation`
![Снимок экрана 2021-06-14 в 18 18 28](https://user-images.githubusercontent.com/15382949/123508496-4ae02800-d689-11eb-9b6c-b3fbed078172.png)

---

## Примеры исправлений

#### Удалены лишние символы
- Стандартный синодальный перевод в `ProPresentor 7`
![image](https://user-images.githubusercontent.com/15382949/123508125-defcc000-d686-11eb-9bdb-d9dbfc32f8eb.png)
- Исправленный синодальный перевод
![image](https://user-images.githubusercontent.com/15382949/123508329-26378080-d688-11eb-97af-f20a1d7f35e3.png)

#### Заменены кавычки
- Стандартный синодальный перевод в `ProPresentor 7`
![image](https://user-images.githubusercontent.com/15382949/123508153-153a3f80-d687-11eb-95b0-2c0deabc709c.png)
- Исправленный синодальный перевод
![image](https://user-images.githubusercontent.com/15382949/123508333-318aac00-d688-11eb-9788-182d9e8badbb.png)

#### Двойное тире заменено на длинное
- Стандартный синодальный перевод в `ProPresentor 7`
![image](https://user-images.githubusercontent.com/15382949/123508141-fd62bb80-d686-11eb-8807-47e911290c13.png)
- Исправленный синодальный перевод
![image](https://user-images.githubusercontent.com/15382949/123508339-3bacaa80-d688-11eb-9bdc-8ae4acd8003d.png)
