# DROP TABLES
symbols_table_drop = "DROP TABLE IF EXISTS symbols;"
ohlcv_table_drop = "DROP TABLE IF EXISTS ohlcv;"

# CREATE TABLES
symbols_table_create = ("""
    CREATE TABLE IF NOT EXISTS symbols(
        id INTEGER PRIMARY KEY, 
        name VARCHAR (3)
    )
""")

ohlcv_table_create = ("""
    CREATE TABLE IF NOT EXISTS ohlcv(
        id SERIAL PRIMARY KEY, 
        symbol_id INTEGER REFERENCES symbols(id),
        time_period_start date,
        time_period_end date,
        time_open date,
        time_close date,
        price_open float,
        price_high float,
        price_low float,
        price_close float,
        volume_traded float,
        trades_count int
    )
""")

# INSERT RECORDS
symbols_table_insert = ("""
    INSERT INTO symbols
    (id, name)
    VALUES (%s, %s)
""")

ohlcv_table_insert = ("""
    INSERT INTO ohlcv
    (symbol_id, time_period_start, time_period_end, time_open, 
    time_close, price_open, price_high, price_low, price_close,
    volume_traded, trades_count)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
""")

create_table_queries = [symbols_table_create, ohlcv_table_create]
drop_table_queries = [ohlcv_table_drop, symbols_table_drop]