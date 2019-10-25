import os


class Config:

    '''
    Describes the general configurations
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')


    DATABASE_PASS = os.environ.get('DATABASE_PASS')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # emails configuration

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    
    DEBUG = True

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):

    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')




class DevConfig(Config):

    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitched'



class TestConfig(Config):

    '''
    Test configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/pitched'


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}
