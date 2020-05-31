import psycopg2
import pandas as pd
from coin_api import get_data
from sql_queries import symbols_table_insert, ohlcv_table_insert


def process_data(conn, cur):
    for index, crypto_symbol in enumerate(['BTC', 'ETH', 'XRP', 'LTC']):
        response = get_data(crypto_symbol)
        df = pd.DataFrame.from_dict(response)
        
        # insert symbols data
        symbols_data = (index, crypto_symbol)
        cur.execute(symbols_table_insert, symbols_data)
        conn.commit()
        
        # insert ohlcv data
        for record in df.values:
            time_period_start, time_period_end, time_open, time_close, \
            price_open, price_high, price_low, price_close, volume_traded, trades_count = record

            ohlcv_data = (
                index, time_period_start, time_period_end, time_open, time_close,
                price_open, price_high, price_low, price_close, volume_traded, trades_count
            )
            
            cur.execute(ohlcv_table_insert, ohlcv_data)
            conn.commit()


def main():
    conn = psycopg2.connect("host=db dbname=cryptodb user=postgres password=postgres port=5432")
    cur = conn.cursor()
    process_data(conn, cur)



if __name__ == "__main__":
    main()
