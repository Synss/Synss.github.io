from __future__ import unicode_literals
import os, sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://blog.synss.me'
RELATIVE_URLS = False
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
DELETE_OUTPUT_DIRECTORY = True
