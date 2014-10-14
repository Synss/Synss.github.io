#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mathias Laurin'
SITENAME = u"Synss' Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Feeds
FEEDS = (('All posts', 'feeds/all.atom.xml'),)

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/Synss'),
          ('LinkedIn', 'https://de.linkedin.com/in/mathiaslaurin'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

ARTICLE_URL = "{date:%Y}/{slug}/"
ARTICLE_SAVE_AS = "{date:%Y}/{slug}/index.html"

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Theme
THEME = "pelican-themes/bootstrap"

# Plugins
PLUGIN_PATH = "pelican-plugins"
PLUGINS = ["neighbors", "summary"]
