import datetime


class index():
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Hanabi2020@39.108.6.87:3306/face_test2?charset=utf8mb4'
    #SQLALCHEMY_TRACK_MODIFICATIONS = True
    #PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=30)
    SEND_FILE_MAX_AGE_DEFAULT = datetime.timedelta(days=7)
    #PERMANENT_SESSION_LIFETIME = datetime.timedelta(seconds=10)


    DEBUG = True