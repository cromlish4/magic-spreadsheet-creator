import urllib.request, json 
#Downloads the latest version of the English card set as of 5-30-22 is 256 mbs
def bulk_downloader():
    with urllib.request.urlopen("https://api.scryfall.com/bulk-data") as url:
        dict_object = json.loads(url.read().decode())
        download_url = dict_object['data'][2]['download_uri']
        response = urllib.request.urlretrieve(download_url, "card_data.json")
