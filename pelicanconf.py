AUTHOR = "Jose Ariel Romero"
SITEURL = "/"
SITENAME = "Coding Interview Questions"
SITETITLE = SITENAME
SITESUBTITLE = "A portfolio with solution and explanation of all coding interview questions I have taken while applying for a job or practicing."
SITEDESCRIPTION = f"{SITETITLE} - {SITESUBTITLE}"
# SITELOGO = "/images/profile.jpg"
# FAVICON = '/images/favicon.ico'

BROWSER_COLOR = "#123456"
PYGMENTS_STYLE = "emacs"
PYGMENTS_STYLE_DARK = "monokai"
DISABLE_URL_HASH = True
PATH = 'content'
OUTPUT_PATH = "blog"
THEME = 'themes/Flex'
THEME_STATIC_DIR = 'theme'
PLUGIN_PATHS = [ 'pelican-plugins' ]
PLUGINS = [ 'sitemap', 'post_stats', 'feed_summary', 'render_math' ]

ARTICLE_URL = 'interview/{category}/{slug}'
ARTICLE_SAVE_AS = f'{ARTICLE_URL}.html'
DRAFT_URL = 'interview_draft/{category}/{slug}.html'
DRAFT_SAVE_AS = f'{DRAFT_URL}.html'
CATEGORY_URL = 'interviewer/{slug}'
CATEGORY_SAVE_AS = f'{CATEGORY_URL}.html'
CATEGORIES_URL = 'interviewers'
CATEGORIES_SAVE_AS = f'{CATEGORIES_URL}.html'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = f'{PAGE_URL}.html'
PAGES_URL = 'pages'
PAGES_SAVE_AS = f'{PAGES_URL}.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = f'{TAG_URL}.html'
TAGS_URL = 'tags'
TAGS_SAVE_AS = f'{TAGS_URL}.html'
USE_FOLDER_AS_CATEGORY = True

ROBOTS = "index, follow"
TIMEZONE = 'America/Havana'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    #('Pelican', 'https://getpelican.com/'),
    #('Python.org', 'https://www.python.org/'),
    #('Jinja2', 'https://palletsprojects.com/p/jinja/'),
    #('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/jose-ariel-romero/'),
    ('github', 'https://github.com/jromero132/'),
    ('envelope', 'mailto:josea132.romero@gmail.com')
    #('Another social link', '#'),
)

MAIN_MENU = True
MENUITEMS = (
    #("Archives", "/archives.html"),
    ("Blog", "/blog"),
    ("Interviewers", "/interviewers"),
    ("Tags", "/tags"),
)

DEFAULT_PAGINATION = 13
COPYRIGHT_YEAR = "2021"

# THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True
# USE_LESS = True

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.toc': {
            'title': 'Table of Contents:' 
        },
        'markdown.extensions.codehilite': {
            'css_class': 'highlight',
            'linenums': True
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.md_in_html': {},
        'markdown.extensions.meta': {},
        'mdx_include': {
            'base_path': 'solutions/'
        }
    },
    'output_format': 'html5',
}