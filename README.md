# Example CS2 Website

This is an example website for a CS2 course to accompany [Your First Year Teaching Computer Science](https://yourfirstyearteaching.com), by Chris Gregg. The site is built with [Flask](http://flask.pocoo.org), [JQuery](https://jquery.com), and [Bootstrap](http://getbootstrap.com). You may modify and use it freely (see the associated MIT license).

# Setup

To set up a static website, perform the following steps:

1. Install the necessary python3 requirements (the site should work with python2 if the shebang line in the python scripts are changed to `#!/usr/bin/env python2`:
```
pip3 install flask
pip3 install flask_frozen
```

1. Clone this repository into a `WWW`, `www`, or `public_html` folder on a server, and `cd` into that folder. *(Note: this will put the basic website into your WWW folder, which may not be empty -- you should clone into an empty directory)* E.g.:
```
git clone https://github.com/yourfirstyearteaching/example_cs2_website.git WWW
cd WWW 
```
2. Modify `freeze.py` to refer to your website, e.g.:
```
app.config['FREEZER_BASE_URL'] = 'https://yourSchool.edu/yourCourseNumber/example_cs2_website/'
```

3. Run `freeze.py` to set up the website:
```
./freeze.py
```

4. Test your website by going to `http://yourSchool.edu/yourCourseNumber/example_cs2_website`.
