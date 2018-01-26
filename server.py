#!/usr/local/bin/python

from itertools import zip_longest
from flask import Flask, render_template, request
from anti.anti import openYandex


app = Flask(__name__)
app.debug = True


@app.route('/')
def home():
    return render_template('index.html', yandex=True, google=True, mobile=False)


@app.route('/', methods=['POST'])
def getpos():
    phrase = request.form.get('phrase')
    obj = openYandex()
    yandex = []
    google = []
    if request.form.get('yandex'):
        yandex = obj.get_yandex_cache_pos(phrase, cache=False)
    if request.form.get('google'):
        google = obj.get_google_cache_pos(phrase, cache=False)
    data = zip_longest(yandex, google)
    return render_template(
        'index.html',
        data=data,
        request=request,
        yandex=request.form.get('yandex'),
        google=request.form.get('google'),
        mobile=request.form.get('mobile')
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0')
