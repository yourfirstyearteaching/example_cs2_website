#!/home2/ecosimul/public_html/yourfirstyearteaching.com/cgi-bin/python3/bin/python3

import sys
import cgitb
cgitb.enable()
sys.path.insert(0, '/home2/ecosimul/public_html/yourfirstyearteaching.com/cgi-bin/python3/lib/python3.6/site-packages')

from wsgiref.handlers import CGIHandler
from myapp import app

CGIHandler().run(app)
