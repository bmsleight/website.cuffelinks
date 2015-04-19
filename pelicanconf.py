#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brendan M. Sleight'
SITENAME = u'Cuffelinks'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (
          ('vine', 'https://vine.co/u/1184667419080282112'),
          ('twitter', 'https://twitter.com/bmsleight'),
          ('github', 'https://github.com/bmsleight'),
          ('github', 'https://github.com/bmsleight/cuffelink'),
         )

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Look at https://github.com/fle/fle.github.io/tree/content

#THEME
THEME = './pelican-bootstrap/'
PELICAN_SOBER_ABOUT = "A site documenting my fun in developing electronic cufflinks aka cuffelinks"
# https://gifvine.co/