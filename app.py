from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from requests.adapters import HTTPAdapter, Retry
from requests.exceptions import Timeout
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory="static"), name="static")

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

@app.get("/orderbook_data")
def orderbook_data(symbol: str = "BTCUSDT"):

    url = f"https://api.binance.com/api/v3/depth?symbol={symbol}&limit=20"

    data = fetch_orderbook_data(url)

    if data is None:
        return {"error":"Unable to Fetch the data"}
    bids = data.get("bids",[])
    asks = data.get("asks",[])

    return {
            "symbol": symbol,
            "bids":bids,
            "asks":asks
        }
    
@app.get("/")
def home(request : Request):
    return templates.TemplateResponse("orderbook.html", {"request" : request})
