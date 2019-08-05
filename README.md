Crawler agent
======

<p align="left">
    <a href='https://pypi.python.org/pypi/Scrapy'><img src='https://img.shields.io/pypi/v/Scrapy.svg'></a>
    <a href='https://pypi.python.org/pypi/Scrapy'><img src='https://img.shields.io/pypi/pyversions/Scrapy.svg'></a>
    <a href='https://pypi.python.org/pypi/Scrapy'><img src='https://img.shields.io/badge/wheel-yes-brightgreen.svg'></a>
    <a href='https://travis-ci.org/scrapy/scrapy'><img src='https://img.shields.io/travis/scrapy/scrapy/master.svg'></a>
</p>

# crawlerBot
The bot is used to iterately access the link for a specified entry URL;
It can click on inner links and post a form against input fields for more deep links;
Bot will run inside a headless browser for more humanlity operations;
If needed, can mock the Header for a real user simulation;
All Paths and actions, response should be stored and can be recalled.

## Features
* Crawler for deep links
* PhantomJS 
* Headless Chromium
* WebDriver
* Report
* Redis based Request Queue

Install
=======

The quick way::

    pip install scrapy
    pip install selenium
    pip install sqlalchemy

For more details see the install section in the documentation:
https://docs.scrapy.org/en/latest/intro/install.html
