import os


class Config:
    '''
    main configuration class for the application
    '''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    child class for production configuration
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevConfig(Config):
    '''
    child class for the development configuration
    '''
    SQLALCHEMY_DATABASE_URI = ''

    DEBUG = True

    config_options = {'development': DevConfig, 'production': ProdConfig}
