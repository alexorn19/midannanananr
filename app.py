from flask import Flask, render_template
import flask
from flask_bootstrap import Bootstrap
from api_utils import *
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def company_list():
    companies = companieset()
    lprices = lowestprices()
    last_updated = timestamps()['timestampPriceCheck']
    ctx = {'companies': companies, 'last_updated': last_updated}
    ctx.update(lprices)
    return render_template('home.html', **ctx)


@app.route('/company/<name>/')
def company_details(name):
    company = compinfo(name)
    return render_template('company.html', company=company, name=name)


@app.route('/station/<key>/')
def station_details(key):
    stations = stationinfo(key)
    loc = stations[0]["geo"]
    return render_template('station.html', stations=stations, loc=loc)


@app.errorhandler(404)
def error404(error):
 return '<h1>Síðan er ekki til!! <br><a href="/"> Smelltu Hér Til Að Komast Aftur Heim</a></h1>', 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)
