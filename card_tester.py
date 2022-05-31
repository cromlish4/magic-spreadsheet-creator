import bulk_downloader as bd
import bulk_wrapper as bw
import json
import xlwt
from xlwt import Workbook
from datetime import datetime
import collections
userIn = input("Update Master Card list(y/n): ")
if userIn == "y":
    try:
        bd.bulk_downloader()
    except:
        print("Master Card List download failed. Ending Program")
        exit()
    print("Master Card List downloaded")
else:
    print("Using Previous Copy")
with open("card_data.json") as f:
        card_file = json.load(f)

#bw.name(card_file,"Black lotus")
cont = True
while cont:
    userIn = input("Card Name: ")
    if userIn == 'q':
        break
    card = bw.search_by_name(card_file,userIn)
    print("Card: \""+bw.name(card)+"\"")
    print("Card Type: "+bw.card_type(card))
    print("Oracle Text: "+bw.oracle_text(card))
    print("Release Date: "+bw.released_date(card))
    print("Price USD: "+bw.price(card))
