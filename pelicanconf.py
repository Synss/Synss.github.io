#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mathias Laurin'
SITENAME = "Synss' Blog"
SITEURL = 'http://blog.synss.me'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DELETE_OUTPUT_DIRECTORY = True

# Blogroll
LINKS = (('Archives', 'archives.html'),
         ('Tags', 'tags.html'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/mathiaslaurin/'),
          ('github', 'https://github.com/Synss'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Static paths and metadata
STATIC_PATHS = ['images', 'extra/robots.txt']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
}

GOOGLE_ANALYTICS = 'UA-56056810-1'
DISQUS_SITENAME = 'synssblog'
