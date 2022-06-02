import json,time
def search_by_name(card_file,card_name):
    print("Searching for card name: \""+card_name+"\"")
    #card_info = card_file['name':card_name]
    #print(card_info)
    #start_time = time.time()
    found_card = ""
    for card in card_file:
        if (card['name'].lower() == card_name.lower()):
            print("Card Found")
            #print("Price: "+card['prices']['usd'])
            #end_time = time.time()
            #print("Took "+str(end_time-start_time)+" seconds to find")
            found_card = card
            return card
            
    if found_card == "":
        return card_name+" not found"

def name(card):
    try:
        return card["name"]
    except:
        #return "Card Not Found"
        return None

def price(card):
    try:
        return card["prices"]["usd"]
    except:
        return "Card Price Not Found"

def oracle_text(card):
    try:
        return card["oracle_text"]
    except:
        return "Oracle Text not available"

def card_type(card):
    try:
        return card["type_line"]
    except:
        return "Card Type Error"

def released_date(card):
    try:
        return card["released_at"]
    except:
        return "Release Date N/A"
    