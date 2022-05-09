# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from PIL import Image
import zbarlight

from flask import Blueprint, render_template,request,redirect,url_for
from flask_migrate import Migrate
from sys import exit
from decouple import config

from apps.config import config_dict
from apps import create_app, db

# WARNING: Don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

# The configuration
get_config_mode = 'Debug' if DEBUG else 'Production'

try:

    # Load the configuration using the default values
    app_config = config_dict[get_config_mode.capitalize()]

except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Production] ')

app = create_app(app_config)
Migrate(app, db)

if DEBUG:
    app.logger.info('DEBUG       = ' + str(DEBUG))
    app.logger.info('Environment = ' + get_config_mode)
    app.logger.info('DBMS        = ' + app_config.SQLALCHEMY_DATABASE_URI)

if __name__ == "__main__":
    app.run()

# @app.route('/run-script')
# def run_script():
#     app.logger.info("I am at the QR page")
#     with open("randomfile.txt", "a") as o:
#         o.write('Hello')
#         o.write('This text will be added to the file')
#     return render_template('/apps/templates/home/ui-camera.html', **locals())

@app.route("/qr_read",methods=['GET', 'POST'])
def qr_read():
    if request.method == 'POST':
        if request.form['button'] == 'no_value':
            pass 
        elif request.form['button'] == 'value':
            with open("randomfile.txt", "a") as o:
                o.write('Hello')
                o.write('This text will be added to the file')
        else:
            pass # unknown
    elif request.method == 'GET':
        file_path = 'qrImg.jpg'
        with open(file_path, 'rb') as image_file:
            image = Image.open(image_file)
            image.load()
        codes = zbarlight.scan_codes(['qrcode'], image)
        with open("randomfile.txt", "w") as o:
            o.write('QR codes: %s' % codes)
        return render_template('home/index.html', segment='index')
        # return redirect(url_for('home_blueprint.index'))  