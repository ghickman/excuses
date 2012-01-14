# Excuses, Excuses...

Never get stuck for an excuse again!

A small deployable application that randomly shows one of your most used excuses.


## Installation
Make sure you have mongodb installed, then run pip:

    pip install -r requirements.txt

Get the site id from mongo:

    python manage.py tellsiteid

Paste the generated `SITE_ID` into a `local_settings.py` file at the same level as `settings.py`.


## Deployment
Use your favourite Django deployment strategy.


## Usage
Add some excuses at `/admin/core/excuse/add/` then visit the homepage for a random one!

