
# coding: utf-8

# In[1]:

import cryptocompare
import requests
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import time
from pymongo import MongoClient
import datetime
import dns
import sys
import os
import websocket
from pprint import pprint
from queue import Queue
from threading import Thread
import urllib.request as urllib


# In[2]:

def on_subadd_response(*args):
    
    client = MongoClient('localhost',
                    authSource='bitcoin')
    db = client.bitcoin
    
    daily_data = db.daily_data
    
    data = list(args)[0].split('~')
    pprint(data)

def on_connect():    
    print("Opened")
def on_error():
    print("error")
def on_disconnect():
    print("Closed")


# In[3]:

def run_update():
    ws = websocket.WebSocketApp('wss://api.bitfinex.com/ws/2')

    ws.on_open = lambda self: self.send('{ "event": "subscribe", "channel": "ticker", "symbol": "tBTCUSD"}')
    ws.on_error = lambda self, err: print(err)

    ws.on_message = lambda self, evt:  print (evt)
    ws.run_forever()


# In[4]:

run_update()


# In[ ]:



