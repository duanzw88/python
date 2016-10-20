

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My Project',
    'author':'duanzw',
    'url':'www.jcble.com',
    'download_url':'www.jcble.com',
    'author_email':"duanzhongwei@jcble.com",
    'version':'0.1'
    'install_requires':['noise'],
    'packages':['ex47'],
    'scripts':[]
    'name':'ex47'
}

setup(**config)
