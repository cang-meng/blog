"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os ,blog

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kt70%hfkxh+n@w(2c5$o*355^j_)hlij=^4fp*o_)%p9=4xeyp'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',#系统后台组件
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'index',#首页
    'fun',#游戏和一些小玩意
    'user',#登陆和用户后台
    'search',#站内搜索
    'set_config',#用户配置
    'post_tools',#用户工具
    'captcha',#验证码
    'haystack',# 添加haystack组件
    'xadmin',#添加xadmin系统后台组件
    'crispy_forms',#xadmin组件依赖
    'reversion',#xadmin组件依赖
    #https组件
    'werkzeug_debugger_runserver',
    'django_extensions',

]

# 配置haystack
HAYSTACK_CONNECTIONS = {
    'default': {
        # 设置搜索引擎，文件是index的whoosh_cn_backend.py
        'ENGINE': 'index.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
        'INCLUDE_SPELLING': True,
    },
}
# 设置每页显示的数据量
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
# 当数据库改变时，会自动更新索引，非常方便
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# django_simple_captcha 验证码基本配置
# 设置验证码的显示顺序，一个验证码识别包含文本输入框、隐藏域和验证码图片，该配置是设置三者的显示顺序
# CAPTCHA_OUTPUT_FORMAT = ' %(text_field)s %(hidden_field)s%(image)s'
CAPTCHA_OUTPUT_FORMAT = ' %(image)s&ensp;%(text_field)s%(hidden_field)s'
# 设置图片噪点
CAPTCHA_NOISE_FUNCTIONS = ( 'captcha.helpers.noise_null',# 设置样式
                           'captcha.helpers.noise_arcs',# 设置干扰线
                           'captcha.helpers.noise_dots',# 设置干扰点
                        )
# 图片大小
CAPTCHA_IMAGE_SIZE = (120, 30)
# 设置图片背景颜色
#CAPTCHA_BACKGROUND_COLOR = '#76EE00'
CAPTCHA_BACKGROUND_COLOR  = blog.RGB()
# 图片中的文字为随机英文字母，如 mdsh
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'
# 图片中的文字为英文单词
# CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.word_challenge'
# 图片中的文字为数字表达式，如1+2=</span>
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
# 设置字符个数
CAPTCHA_LENGTH = 4
# 设置超时(minutes)
CAPTCHA_TIMEOUT = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # 使用中文
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'fun/templates'),
                 os.path.join(BASE_DIR, 'index/templates'),
                 os.path.join(BASE_DIR, 'user/templates'),
                 os.path.join(BASE_DIR, 'search/templates'),
                 os.path.join(BASE_DIR, 'post_tools/templates'),
                 os.path.join(BASE_DIR, 'set_config/templates'),]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3','NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# SECURITY WARNING: don't run with debug turned on in production!
#项目上线时设置 DEBUG = False
DEBUG = True
#允许所有域名访问
ALLOWED_HOSTS = ['*']

# 配置自定义用户表MyUser
AUTH_USER_MODEL = 'user.MyUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# STATIC_ROOT用于项目部署上线的静态资源文件
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# STATICFILES_DIRS用于收集admin的静态资源文件
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),]

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/uploads/hp/')
MEDIA_ROOT_FILE = os.path.join(BASE_DIR, 'static/uploads/file/')
#邮件配置
# 邮件配置信息
EMAIL_USE_SSL = True
# 邮件服务器，如果是 163 改成 smtp.163.com
EMAIL_HOST = 'smtp.qq.com'
# 邮件服务器端口
EMAIL_PORT = 465
# 发送邮件的账号
EMAIL_HOST_USER = ''
# SMTP服务密码
EMAIL_HOST_PASSWORD = ''

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DANDANLOCAL = True
DANDANAPIKEY = "" 
DANDANAPISECRET = ""

'''
http://www.itpk.cn/     注册 api
DANDANLOCAL = False  #拿到了api后设置成False
DANDANAPIKEY = ""   #你的api key
DANDANAPISECRET = ""  #你的 api secret
'''

