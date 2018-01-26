# -*- coding:utf-8 -*-

# Настройки Redis(сохранение кэшированных данных)
# Оставить дефолтные для текущего docker-compose
ANTI_REDIS_CONF = {'host': 'redis', 'port': 6379}

# Настройки rabbit(брокер сообщений)
# Оставить дефолтные для текущего docker-compose
ANTI_AMQP_CONF = 'amqp://guest:guest@rabbit:5672/'


# Оставить пустым, если сохранять позиции в реляционную DB не нужно
# SQLAlchemy style uri
ANTI_SQLALCHEMY_DATABASE_URI = ''

# Ключ от api https://anti-captcha.com/
# Обязательно
KEY_ANTIGATE = ''

# Ключ от прокси серверов https://proxy6.net/
# Опционально
PROXY_API_KEY = ''

# Данные для google
# Опционально
GOOGLE_USER = ''
GOOGLE_PASS = ''
GOOGLE_ANSWER = ''
