from datetime import timedelta


class Config(object):
    DEBUG = True
    SECRET_KEY = "2A462D4A614E645266556A586E327235"
    SECURITY_PASSWORD_SALT = "Jg2F07qoedc5s8XI"
    RECAPTCHA_SITE_KEY = "6LffXoUcAAAAAGh90pZfRStkbZZmUprl0m_6GkOi"
    RECAPTCHA_SECRET_KEY = "6LffXoUcAAAAAIB1_CpN5r73NQGo4lEUeqwSd2sF"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_USERNAME = "noreplyBluedit@gmail.com"
    MAIL_PASSWORD = "a@g4246bvvs.0"
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465
    MAIL_DEFAULT_SENDER = "noreplyBluedit@gmail.com"

    # Image default path (need to add more param behind)
    IMAGE_UPLOADS = "static/"
    # Image allowed extensions, reject all other extensions
    ALLOWED_IMAGE_EXTENSIONS = ["JPEG", "JPG", "PNG"]
    # All file input, not only image (our app only allow image upload). Max size 5mb
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024

    # Testing config
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)

    # Section 1: Allow session to only exist in HTTPs connection. Ensure cookie/session will never be sent on
    # unencrypted wire TO REMOVE IF IT CAUSES SESSION ERROR ON DEPLOYMENT
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True

    # Section 2: For XSS prevention, add httponly tag
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True

    SESSION_PROTECTION = "strong"


class SQL_CONFIG(Config):
    MYSQL_DATABASE_HOST = "localhost"
    MYSQL_DATABASE_PORT = 3306
    MYSQL_DATABASE_USER = "root"
    MYSQL_DATABASE_PASSWORD = "P@ssw0rd"
    MYSQL_DATABASE_DB = "ict3103_ssd"
