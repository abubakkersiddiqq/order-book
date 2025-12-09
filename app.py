from flask import Flask,render_template,jsonify,request
from requests.adapters import HTTPAdapter, Retry
from requests.exceptions import Timeout
import requests

app = Flask(__name__,template_folder = "templates", static_folder = "static")

def get_symbol():
    symbol = request.args.get("symbol", "BTCUSDT")
    return symbol

def fetch_orderbook_data(url):
    session = requests.Session()
    retries = Retry(
        total = 3,
        backoff_factor = 1,
        status_forcelist = [500,502,504,503]
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    try:
        response = session.get(url,timeout=2)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except Timeout as to:
        print("Timeout Error: ",to)

@app.route("/orderbook_data")
def orderbook_data():

    symbol = get_symbol()
    url = f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit=20"

    data = fetch_orderbook_data(url)

    if data is None:
        return jsonify({"error":"Unable to Fetch the data"}),500
    bids = data.get("bids",[])
    asks = data.get("asks",[])

    return jsonify(
        {
            "symbol": symbol,
            "bids":bids,
            "asks":asks
        }
    )




@app.route("/")
def home():
    return render_template("orderbook.html")
if __name__ == '__main__':
    app.run(debug=True)