from datetime import date

class DefaultConfig(object):

    # Set this to be true for debugging
    DEBUG = True

    APPLICATION_VERSION = '0.0.0'
    APPLICATION_TITLE = 'Peephole'
    APPLICATION_CONFIG_DIR = '/instances'
    ADMINS = ['leerenchang@gmail.com', 'leeren@berkeley.edu', 'mayaah@berkeley.edu']
    APPLICATION_COPYRIGHT = '%s - Leeren Chang' % date.today().year

class DevConfig(object):

    DEBUG = False

    ENVIRONMENT_STAGE = 'Dev'

class StageConfig(object):

    DEBUG = False

class ProdConfig(object):

    DEBUG = False
