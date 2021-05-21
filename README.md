### Алгоритм работы
- Создание нового аккаунта с iOS устройства
- Добавление этого аккаунта вам в друзья
- Создание комнаты 1 на 1 на 2500
- Приглашение вашего аккаунта
- Выкидывание 5 карт, чтобы засчитался рейтинг за победу
- Бот сдается вашему аккаунту
- Удаление аккаунта бота из друзей

### Запуск бота
Для начала нужно заполнить файл config.py
- RUCAPTCHA_KEY - ключ от сайта рекапчи, чтобы решать игровую капчу(xevil ее не решает)
- NAME - точное имя вашего аккаунта(оно должно быть уникальным)
- USER_ID - user_id  вашего аккаунта
- TOKEN - токен вашего аккаунта
- HUMAN_CAPTCHA_SOLVE - если True, то капчу вы будуте решать вручную
- level - уровень логирования, если хотите посмотреть ответы от сервера, впишите DEBUG
- SIGN_KEY - ключ подписи запроса, на момент 21.05.2021 он валидный, был получен с iOS версии игры
Далее

```
pip3 install -r requirements.txt
python3 main.py
```

### Получение user_id и токена от вашего аккаунта
1. Скачиваем HTTP Canary на ваш телефон, где установленна игра
2. Запускаем игру
3. Ищем в запросах TCP и находим там запрос auth, рядом с ним будет токен от аккаунта
[Видео гайд](https://i.imgur.com/X9ckvSw.mp4)

### О блокировках
Крутить можно, но без фанатизма, меня банило(обнуление + пару дней за победы будет награда 0), если крутил больше 400к в день
В планах придумать как это обходить
