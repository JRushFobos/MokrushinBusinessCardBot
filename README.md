# MokrushinBusinessCardBot
### Бот визитка Мокрушина Евгения

MokrushinBusinessCardBot - бот позволяющий получить информацию обо мне о разработчике ине только
- Информация обо мне
- Мои навыки
- Получить ссылку на резюме (Goodle doc)
- Получить резюме в формате PDF
- Получить информацию о моем опыте работы
- Получить информацию о моих проектах
- Получить информацию о моих контактах

### 1. Настроен CI/CD на VPS sweb.ru с помощью Git Actions
Телеграм бот автоматически обновляется при обновлении main ветки

### 2. Бот развернут в Docker контейнере на VPS sweb.ru (ручной деплой)
Сайт https://sweb.ru/

Команды ручного развертывания и запуска:

Local
```bash
docker ps -a
docker images

docker tag businesscardbot:latest jrush/businesscardbot:latest
docker push jrush/businesscardbot:latest
```
Remote
```bash
sudo apt update
sudo apt install docker.io

sudo systemctl status docker
sudo systemctl start docker

sudo docker login

docker pull jrush/businesscardbot:latest
docker run -d -p 8081:80 --name businesscardbot jrush/businesscardbot:latest

docker stop businesscardbot
```

### 3. Запуск бота (локально)
4.1. Клонируем проект:

```bash
git clone https://github.com/JRushFobos/businesscardbot.git
```

4.2. Устанавливаем виртуальное окружение

```bash
python -m venv venv
```

4.3. Активируем виртуальное окружение

```bash
source venv/Scripts/activate
```

4.4. Устанавливаем зависимости

```bash
pip install -r requirements.txt
```

4.5. Запускаем бота

```bash
python businesscardbot.py
```

### Об авторе
Мокрушин Евгений [@JRushFobos](https://github.com/JRushFobos)
