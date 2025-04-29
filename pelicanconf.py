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

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/custom.css', 'extra/custom.js', 'extra/related-articles.js']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/custom.css': {'path': 'theme/css/custom.css'},
    'extra/custom.js': {'path': 'theme/js/custom.js'},
    'extra/related-articles.js': {'path': 'theme/js/related-articles.js'},
}

# Use Typogrify
TYPOGRIFY = True

# Theme settings
THEME="/Users/amit/Dropbox/DCode/ramblings/themes/attila"

# Custom CSS and JS files
CSS_OVERRIDE = ['theme/css/custom.css']
JS_OVERRIDE = ['theme/js/custom.js', 'theme/js/related-articles.js']

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
# Using default index.html as the blog page now

# Custom feature settings
SHOW_RELATED_ARTICLES = True  # Enable related articles feature
MAX_RELATED_ARTICLES = 15     # Maximum number of related articles to display
SHOW_COVER_IN_LISTING = True  # Show post cover images in article listings

# Show categories in navigation menu
SHOW_CATEGORIES_ON_MENU = False  # We're using MENUITEMS instead for more control

# Menu items
MENUITEMS = (
    ('Blog', '/'),
    ('Technical', '/category/technical.html'),
    ('Business', '/category/business.html'),
    ('Creative', '/category/creative.html'),
)
