# Example CS2 Website

This is an example website for a CS2 course to accompany [Your First Year Teaching Computer Science](https://yourfirstyearteaching.com), by Chris Gregg. The site is built with [Flask](http://flask.pocoo.org), [JQuery](https://jquery.com), and [Bootstrap](http://getbootstrap.com). You may modify and use it freely (see the associated MIT license).

# Setup

To set up a static website, perform the following steps:

1. Clone this repository into a `WWW`, `www`, or `public_html` folder on a server, and `cd` into that folder. E.g.:
```git clone https://github.com/yourfirstyearteaching/example_cs2_website.git
cd example_cs2_website
```

1. Modify `freeze.py` to refer to your website, e.g.:
`app.config['FREEZER_BASE_URL'] = 'https://yourSchool.edu/yourCourseNumber/example_cs2_website/'`
