from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import render_template



app = Flask(__name__)

host, dbname, user, password, port= "db", "cryptodb", "postgres", "postgres", 5432
DB_URI = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app) # instance of the database


@app.route('/')
def line():
    crypto_symbol = request.args.get('crypto_symbol', None)
    if crypto_symbol is None:
        crypto_symbol = 'BTC'

    sql_statement = f'''
        SELECT ohlcv.time_close, ohlcv.price_open, ohlcv.price_close, 
                ohlcv.price_low, ohlcv.price_high, ohlcv.volume_traded, ohlcv.trades_count
        FROM ohlcv
        JOIN symbols
        ON ohlcv.symbol_id = symbols.id
        WHERE symbols.name = '{crypto_symbol}'

    '''

    query_data = db.engine.execute(sql_statement).fetchall()
    dates, price_open, price_close, price_low, price_high, volume_traded, trades_count= zip(*query_data)
    dates = [str(date.year) + '-' + str(date.month) for date in dates]

    data = {
        'dates': dates, 'price_open': price_open, 
        'price_close': price_close, 'price_low': price_low,
        'price_high':price_high, 'volume_traded':volume_traded,
        'trades_count':trades_count
    }
    price_title =  crypto_symbol + ' Monthly Price in USD'
    trade_title = crypto_symbol + ' Volcume and Trades Count in USD'
    return render_template('line_chart.html', price_title=price_title, trade_title=trade_title, data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
