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

#with open("card_data.json") as f:
wb = xlwt.Workbook()
ws = wb.add_sheet('All Cards',True)

#style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',
#num_format_str='#,##0.00')

#style1 = xlwt.easyxf(num_format_str='D-MMM-YY')
#ws.write(0, 0, 1234.56, style0)
#ws.write(1, 0, datetime.now(), style1)

col_width = 4000
ws.col(0).width = col_width+1000
ws.col(1).width = 2*col_width
ws.col(2).width = 3*col_width
ws.col(3).width = col_width
ws.col(4).width = col_width
ws.col(5).width = col_width

while True:
    filename = input("Collection Filename: ")
    loc = filename.find(".txt")
    if loc < 0:
        spreadsheet_name = filename
        filename = filename+".txt"
    else:
        spreadsheet_name = filename[0:loc]
    try:
        f = open(filename, "r")
    except:
        print("Error opening file, please try again.")
    else:
        break

ws.write(0, 0, "Card Name")
ws.write(0, 1, "Card Type")
ws.write(0, 2, "Oracle Text")
ws.write(0, 3, "Count")
ws.write(0, 4, "Release Date")
ws.write(0, 5, "Price per card")
#ws.write(2, 2, xlwt.Formula("A3+B3"))
card_read_name = f.readline()
cards_processed = dict
count_loc = dict
i = 1
while card_read_name != "":
    
    card_read_name = card_read_name.strip()
    card = bw.search_by_name(card_file,card_read_name)
    card_name = bw.name(card)
    if card_name == None:
        card_name = card_read_name

    try:
        cards_processed[card_name]
    except:
        cards_processed = {card_name:1}
        ws.write(i, 0, card_name)
        ws.write(i, 1, bw.card_type(card))
        ws.write(i, 2, bw.oracle_text(card))
        ws.write(i, 3, cards_processed[card_name])
        count_loc = {card_name:i}
        ws.write(i, 4, bw.released_date(card))
        ws.write(i, 5, bw.price(card))
        i+=1
    else:
        count = cards_processed[card_name]
        cards_processed = {card_name:count+1}
        ws.write(count_loc[card_name], 3, cards_processed[card_name])
    card_read_name = f.readline()    
#wb.save(input("Spreadsheet Name: ")+'.xls')
wb.save(spreadsheet_name+'.xls')
f.close()
