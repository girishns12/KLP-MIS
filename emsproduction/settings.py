#!/usr/bin/python
# -*- coding: utf-8 -*-
# Django settings for klp project.

DEBUG = True #False
TEMPLATE_DEBUG = True #False

SERVER_EMAIL = 'support@mahiti.org'

SEND_BROKEN_LINK_EMAILS = True

IGNORABLE_404_ENDS = ('.css', '.html', 'favicon.ico')

ADMINS = (('Girish',
          'girish.n.s@mahiti.org'))  # ('Your Name', 'your_email@domain.com'),
import os.path
PROJECT_ROOT1 = os.path.realpath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_ROOT1,
                               os.path.pardir))
PYTHON_PATH = 'python'  # os.path.abspath(os.path.join(PROJECT_ROOT, os.path.pardir))+'/bin/python'
PROJECT_NAME = os.path.basename(PROJECT_ROOT)

MANAGERS = ADMINS

TESTING = 0
REPORTMAIL_SENDER = 'KLP TEAM <dev@klp.org.in>'
REPORTMAIL_RECEIVER = ['girish.n.s@mahiti.org',
                       ]
SESSION_COOKIE_AGE = 3600
SESSION_SAVE_EVERY_REQUEST = True

DATABASES = {'default': {  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
                           # Or path to database file if using sqlite3.
                           # Not used with sqlite3.
                           # Not used with sqlite3.
                           # Set to empty string for localhost. Not used with sqlite3.
                           # Set to empty string for default. Not used with sqlite3.
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #'NAME': 'dev3clone',
    #'USER': 'dev3clone',
    #'PASSWORD': 'vjshndfj7t6r5',
    'NAME': 'production',
    'USER': 'production',
    'PASSWORD': 'production',
    'HOST': '',
    'PORT': '',
    'OPTIONS': {'autocommit': True},
    }}

# DATABASES = {
#    'default': {
#        'ENGINE': 'postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'klpmaster',                      # Or path to database file if using sqlite3.
#        'USER': 'klpmaster',                      # Not used with sqlite3.
#        'PASSWORD': 'TVwhUXxj3kriFyF9',                  # Not used with sqlite3.
#        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.

#    'OPTIONS': {
#    'autocommit': True,
# }
#    }
ALLOWED_HOSTS = ['*']
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ems@klp.org.in'
EMAIL_HOST_PASSWORD = 'k1P3Ms854'
EMAIL_PORT = 587

# DEFAULT_FROM_EMAIL = 'support@mahiti.org'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.

TIME_ZONE = 'Asia/Kolkata'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.

USE_I18N = True



NUM_OF_FLEXI_ANSWER_FORM_RECORDS = 20

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale

USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"

MEDIA_ROOT = PROJECT_ROOT + '/static_media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"

MEDIA_URL = '/static_media/'
STATIC_URL='/static/'
# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".

ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.

SECRET_KEY = 'j*q8aa_ftzsx6y&cn-p6hx(b_^ddoo9z34dx=)tx3n!2to3v4e'

# List of callables that know how to import templates from various sources.

TEMPLATE_LOADERS = ('django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader')

#     'django.template.loaders.eggs.Loader',

MIDDLEWARE_CLASSES = (  # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'fullhistory.fullhistory.FullHistoryMiddleware',
    #'schools.middleware.QueryLogMiddleware',
    )

ROOT_URLCONF = 'emsproduction.urls'

TEMPLATE_CONTEXT_PROCESSORS = \
    ('django.contrib.auth.context_processors.auth',
     'django.core.context_processors.debug',
     'django.core.context_processors.i18n',
     'django.core.context_processors.media',
     'django.contrib.messages.context_processors.messages')

TEMPLATE_DIRS = PROJECT_ROOT + '/schools/templates/'  # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".                                                        # Always use forward slashes, even on Windows.
                                                          # Don't forget to use absolute paths, not relative paths.

INSTALLED_APPS = (  # Uncomment the next line to enable the admin:
                    # 'django_extensions',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'django.contrib.admin',
    'schools',
    'object_permissions',
    'fullhistory',
    )

