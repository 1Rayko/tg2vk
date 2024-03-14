
# tg2vk

Утилита для проброса сообщений/записей из телеграм бота в ВКонтакте

## Установка системных зависимостей

### Arch Linux
```bash
sudo pacman -S git python python-pip --noconfirm
```
### Debian, Ubuntu
```bash
sudo apt-get install -y git python python-pip
```
### Void Linux
```bash
sudo xbps-install -S git python3 python3-pip
```

### Клонирование репозитория и установка утилиты

```bash
  git clone https://github.com/1Rayko/tg2vk; 
  cd tg2vk;
  chmod +x install.sh;
  ./install.sh;
```
    
## Редактирование конфига

```python
# config.py

mode = 1 # 1 - отправка в личные сообщения; 2 - отправка публикации

# Vk
user_id =  # user_id пользователя, которому будут приходить сообщения(Если нет, то  None)
group_id= #  id сообщества, в котором будет создаваться публикация (Если нет, то  None)

vk_token="" # токен пользователя или сообщества

# Imgur
# READ  https://apidocs.imgur.com/
# https://api.imgur.com/oauth2/addclient
imgur_client_id=''
imgur_client_secret=''

#Telegram
bot_token='' # токен телеграм бота

```
## Запуск
```bash
cd tg2vk; python main.py
```
## Авторы

- [@1Rayko](https://www.github.com/1rayko)


## Лицензия

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)
