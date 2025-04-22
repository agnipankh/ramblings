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


THEME="/Users/amit/Dropbox/DCode/ramblings/themes/attila"

### Attila specific

HOME_COVER = 'https://geekyshacklebolt.github.io/blog/images/my-blog-header-bg.jpg'
# URLs
TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
CATEGORIES_URL = 'categories.html'
CATEGORIES_SAVE_AS = 'categories.html'
ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'

# URL and path settings
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
INDEX_SAVE_AS = 'blog.html'  # Move the default index to blog.html

# Show post cover images in article listings
SHOW_COVER_IN_LISTING = True

# Show categories in navigation menu
SHOW_CATEGORIES_ON_MENU = False  # We're using MENUITEMS instead for more control

# Menu items
MENUITEMS = (
    ('Home', '/'),
    ('Blog', '/blog.html'),
    ('Technical', '/category/technical.html'),
    ('Business', '/category/business.html'),
    ('Creative', '/category/creative.html'),
)
