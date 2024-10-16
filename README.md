# Управление электронным дневником

## Что за проект?

Этот проект представляет собой систему управления электронным дневником для школьников. С помощью этого скрипта вы можете:

- Исправлять плохие оценки учеников.
- Удалять замечания (жалобы) учеников.
- Добавлять похвалы от учителей.

Скрипт написан на Python и использует Django для работы с базой данных.

## Установка:

- **Клонируйте репозиторий**:
   Перейдите в директорию, где вы хотите сохранить проект, и выполните команду:
   ```bash
   git clone <ссылка на репозиторий>
   ```
   
- Вы увидите файл scripts.py, в который нужно перейти и сделать необходимые настройки:

   ![Настройки](https://i.postimg.cc/KjhLfg2k/image.jpg)
   
   FULL_NAME = Необходимо ввести ** !ПОЛНОЕ! ** фио ученика,что бы избежать ошибки выбора ученика, иначе скрипт выдаст исключение.
   
   SUBJECT_TITLE = Введите предмет,по которому хотите добавить похвалу.
   
   PRAISE_TEXT = Введите текст похвалы.
   
   BAD_GRADES = [2, 3] Выбор плохих оценок.
   
   NEW_GRADE = 5 На какую оценку хотите исправить.
   
## Запуск:

- После выполнения всех настроек, пришло время их применить.Для этого открываем терминал и переходим в режим python shell командой 
```
python manage.py shell
```

Запустится Django shell, о чём сообщит надпись:

![shell](https://i.postimg.cc/zGxcQq3X/image.jpg)

- Далее копируем строку импорта, наши настройки, вспомогательную функцию для точного нахождения ученика по фио и вводим в терминал shell.

- После этого нам остается выбрать необходимую нам функцию (они подписаны), так же скопировать ее и вставить в терминал shell.
При удачном выполнении скрипта,вы увидите вывод в терминале:

![Замечания](https://i.postimg.cc/zGkyZc1f/image.jpg)

![Похвала](https://i.postimg.cc/Y9T9zcQd/image.jpg)

- Переходим на сайт, видим все наши изменения, радуемся успешной учебе)

![Работа скрипта](https://i.postimg.cc/7LfJ3npY/image.jpg)


## Цель проекта:

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).