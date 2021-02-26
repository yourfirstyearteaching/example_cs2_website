#!/usr/bin/env python3

from flask_frozen import Freezer
from myapp import app
import os

freezer = Freezer(app)

@freezer.register_generator
def assignments_gen():
    return ['/assignments/'+x+'/' for x in os.listdir('templates/assignments') if x.endswith('html')]

if __name__ == '__main__':
    app.config['FREEZER_DESTINATION'] = '/home/yourfiy4/public_html/cs/example_cs2_website'
    app.config['FREEZER_BASE_URL'] = 'https://yourfirstyearteaching.com/cs/example_cs2_website/'
    freezer.freeze()
