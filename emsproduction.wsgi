import sys
import os
import newrelic.agent

sys.path.append('/home/klp');
sys.path.append('/home/klp/ems-production');

newrelic.agent.initialize('/home/klp/ems-production/newrelic.ini')


os.environ['DJANGO_SETTINGS_MODULE'] = 'emsproduction.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()

