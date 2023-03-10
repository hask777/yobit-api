import requests
import json

def get_info():
    response = requests.get(url="https://yobit.net/api/3/info")
    with open('files/info.txt', 'w') as f:
        f.write(response.text)
    return response.text

def get_ticker(coin1="btc", coin2="usd"):
    response = requests.get(url=f"https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1")
    with open('files/ticker.txt', 'w') as f:
        f.write(response.text)
    return response.text

def get_depth(coin1="btc", coin2="usd", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")
    with open('files/depth.txt', 'w') as f:
        f.write(response.text)

    bids = response.json()[f"{coin1}_usd"]["bids"]
    total_bids_amount = 0
    for item in bids:
        price = item[0]
        coin_amount = item[1]
        total_bids_amount += float(price) * float(coin_amount)
    return f"Total : {total_bids_amount}$"

def trades(coin1="btc", coin2="usd", limit=150):
    response = requests.get(url=f"https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1")

    with open('files/trades.txt', 'w') as f:
        f.write(response.text)

    total_trade_ask = 0
    total_trade_bid = 0

    for item in response.json()[f"{coin1}_{coin2}"]:
        if item["type"] == "ask":
            total_trade_ask += item["price"] * item["amount"]
        else:
            total_trade_bid += item["price"] * item["amount"]

    info = f"[-] TOTAL {coin1} SELL: {round(total_trade_ask, 2)} $\n[-] TOTAL {coin1} BUY: {round(total_trade_bid, 2)} $"
     
    return info

def main():
    # get_info()
    # get_ticker()
    # print(get_depth())
    print(trades())

if __name__ == '__main__':
    main()