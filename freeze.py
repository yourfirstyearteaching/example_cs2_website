#!/usr/bin/env python3

from flask_frozen import Freezer
from myapp import app

freezer = Freezer(app)

if __name__ == '__main__':
    app.config['FREEZER_DESTINATION'] = 'example_cs2_website'
    app.config['FREEZER_BASE_URL'] = 'https://yourfirstyearteaching.com/cs/example_cs2_website/'
    freezer.freeze()
