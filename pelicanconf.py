#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'SkyLines Team'
SITENAME = u'SkyLines Blog'
SITEURL = ''

MENUITEMS = [
  ('General', 'general'),
  ('New Features', 'new-features'),
  ('Live Tracking', 'live-tracking'),
  ('Engineering', 'engineering'),
]

TIMEZONE = 'Europe/Berlin'

DEFAULT_CATEGORY = u'General'
DEFAULT_LANG = u'en'

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
