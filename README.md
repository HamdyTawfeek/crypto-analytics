## crypto-analytics

-----    
    
### Introduction

This is a simple single web application to visualize [coinAPI](https://www.coinapi.io/) data using [Chart.js](https://www.chartjs.org/) for cryptocurrencies Bitcoin (BTC), Ethereum (ETH), Ripple (XRP) and Litecoin (LTC)

### Tech Stack

Our tech stack will include:

* **Python3** and **Flask** as our server language and server framework
* **PostgreSQL** as our database of choice
* **Chart.js** For Data Visualization
* **Google Analytics** For Event Tracking 
* **Docker** , **Docker Compose** Application Containerization 


### Main Files: Project Structure
```sh
├── app.py
├── docker-compose.yml
├── Dockerfile
├── etl
│   ├── coin_api.py
│   ├── create_tables.py
│   ├── etl.py
│   ├── __init__.py
│   └── sql_queries.py
├── __init__.py
├── README.md
├── requirements.txt
└── templates
    └── line_chart.html
```

## Quick start

To run the project locally,

1. Open a terminal:
  ```shell
  git clone https://github.com/HamdyTawfeek/crypto-analytics.git
  cd crypto-analytics
  docker-compose up
  ```

2. Navigate to Home page [http://localhost:8000/]( http://localhost:8000/) to view the charts.


## Enhancements I will add soon

1. Add Google Analytics Tracking ID 