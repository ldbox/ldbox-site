# Copyright 2015 Oleg Girko <ol@infoserver.lv>
#
# This file is part of ldbox.site Python package.
#
# ldbox.site Python package is free software: 
# you can redistribute it and/or modify
# it under the terms of the GNU Affero Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Foobar is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero Public License for more details.
#
# You should have received a copy of the GNU Affero Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

"""
Django settings for ldbox project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Import local secrets from file that is not imported to VCS
from .localsecrets import LDBOX_SECRET_KEY
from .localsecrets import LDBOX_DATABASE_ENGINE
from .localsecrets import LDBOX_DATABASE_NAME
from .localsecrets import LDBOX_DATABASE_USER
from .localsecrets import LDBOX_DATABASE_PASSWORD
from .localsecrets import LDBOX_DATABASE_HOST
from .localsecrets import LDBOX_DATABASE_PORT


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = LDBOX_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'ldbox.site',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'waliki',
    'waliki.git',
    'waliki.attachments',
    'waliki.pdf',
    'waliki.slides',
    'waliki.togetherjs',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ldbox.site.urls'

WSGI_APPLICATION = 'ldbox.site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': LDBOX_DATABASE_ENGINE,
        'NAME': LDBOX_DATABASE_NAME,
        'USER': LDBOX_DATABASE_USER,
        'PASSWORD': LDBOX_DATABASE_PASSWORD,
        'HOST': LDBOX_DATABASE_HOST,
        'PORT': LDBOX_DATABASE_PORT,
    }
}

# Context processors

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as CP

TEMPLATE_CONTEXT_PROCESSORS = CP + (
    'django.core.context_processors.request',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

SENDFILE_BACKEND = 'sendfile.backends.simple'

# Authentication settings

LOGIN_REDIRECT_URL = '/'

# Waliki settings

WALIKI_DATA_DIR = '/var/lib/waliki/ldbox/data'

WALIKI_DEFAULT_MARKUP = 'Markdown'

WALIKI_COMMITTER_EMAIL = 'nobody@ldbox.org'

WALIKI_COMMITTER_NAME = 'Anonymous'

WALIKI_ATTACHMENTS_DIR = '/var/lib/waliki/ldbox/attachments'

WALIKI_LOGGED_USER_PERMISSIONS = (
    'view_page',
    'add_page',
    'change_page',
    'delete_page'
)

