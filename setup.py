import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '1.0.1'
PACKAGE_NAME = 'asterix4py'
AUTHOR = 'Filip Jonckers'
AUTHOR_EMAIL = 'jof@skeyes.be'
URL = 'https://github.com/filipjonckers/asterix4py'
LICENSE = 'MIT License'
DESCRIPTION = 'Pure python library for decoding Eurocontrol Asterix binary data'
KEYWORDS = 'asterix radar artas eurocontrol mode-s'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
CLASSIFIERS = [
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Intended Audience :: Developers',
      'Intended Audience :: Information Technology',
      'Intended Audience :: Science/Research',
      'Operating System :: MacOS',
      'Operating System :: Microsoft :: Windows',
      'Operating System :: POSIX :: Linux',
      'License :: OSI Approved :: MIT License',
      'Topic :: Software Development',
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Topic :: Scientific/Engineering',
      'Topic :: Scientific/Engineering :: Information Analysis',
      'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator'
]

INSTALL_REQUIRES = [
      # 'xml.dom',
      # 'json'
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )
