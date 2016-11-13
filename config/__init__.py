from datetime import date

class DefaultConfig(object):

    # Set this to be true for debugging
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    APPLICATION_VERSION = '0.0.0'
    APPLICATION_TITLE = 'Peephole'
    APPLICATION_CONFIG_DIR = '/instances'
    ADMINS = ['leerenchang@gmail.com', 'leeren@berkeley.edu', 'mayaah@berkeley.edu']
    APPLICATION_COPYRIGHT = '%s - Leeren Chang' % date.today().year
    SECRET_KEY = 'kx02j4lksaF'

    FACEBOOK_APP_ID = '211755832600216'
    FACEBOOK_APP_SECRET = '179af417990a308468246f52decbff38'

class DevConfig(object):

    DEBUG = False

    ENVIRONMENT_STAGE = 'Dev'

class StageConfig(object):

    DEBUG = False

class ProdConfig(object):

    DEBUG = False
