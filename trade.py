import requests
from config import KEY, SECRET
import time
from urllib.parse import urlencode
import hmac
import hashlib

def get_info():

    values = dict()
    values["method"] = "getInfo"
    values["nonce"] = str(int(time.time()))

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()
    # print(sign)

    headers = {
        "key": KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.text

def get_deposit_addrerss(coin_name="btc"):
    values = dict()
    values["method"] = "GetDepositAddress"
    values["coinName"] = coin_name
    values["need_new"] = 0
    values["nonce"] = str(int(time.time()))

    body = urlencode(values).encode("utf-8")
    sign = hmac.new(SECRET.encode("utf-8"), body, hashlib.sha512).hexdigest()

    headers = {
        "key": KEY,
        "sign": sign
    }

    response = requests.post(url="https://yobit.net/tapi/", headers=headers, data=values)
    return response.text


def main():
    coin_name = input("Enter a coin name: ")
    print(get_deposit_addrerss(coin_name=coin_name))
    print(get_info())

if __name__ == '__main__':
    main()

     

