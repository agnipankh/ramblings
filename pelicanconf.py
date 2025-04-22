AUTHOR = 'Amit Agrawal'
SITENAME = 'Play Deliberately'
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/Denver'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("TruU", "https://TruU.ai"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("Linked-in", "https://www.linkedin.com/in/agnipankh/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Use Typogrify
TYPOGRIFY = True


# THEME="/Users/amit/anaconda3/envs/blog/lib/python3.11/site-packages/pelican/themes/html5up-massively"

### Attila specific

HOME_COVER = 'https://geekyshacklebolt.github.io/blog/images/my-blog-header-bg.jpg'
# URLs
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
CATEGORIES_URL = 'categories.html'
CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'

# If your theme uses author pages
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'
