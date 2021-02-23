from flask import Flask, render_template, request, g
from markupsafe import escape
from strat import strat
from utils import db

app = Flask(__name__, template_folder='views')

@app.route('/')
def welcome():
    return "Welcome to GigaSwap Trader Suite"

@app.route('/strategy')
def strategyOverview():
    if request.method == 'POST':
        if strat.validStrategy(request.form['STRAT'], request.form['DICT']):

            return strat.initStrategy() # request.form)
        else:
            return "Invalid strategy."                       
    else:
        return render_template("stratOverview.html.j2", STRATS=db.query_db('select * from strategy'))

@app.route('/strategy/<strategy>')
def strat(strategy):
    return render_template("stratView.html.j2", STRAT=db.query_db(f'select * from strategy where name is "{strategy}"')) # TODO: change to %s

@app.route('/func')
def func():
    return render_template("func.html.j2")

if __name__ == '__main__':
    app.run()
