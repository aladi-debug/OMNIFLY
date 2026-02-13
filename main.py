from amadeus import Client, ResponseError
import requests
import datetime
import time

AMADEUS_KEY = "YOUR_AMADEUS_KEY"
AMADEUS_SECRET = "YOUR_AMADEUS_SECRET"
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

link = "https://aircargogroup.com/wp-content/uploads/2021/07/IATA-Code-List.pdf"
text = "here"

amadeus = Client(client_id=AMADEUS_KEY, client_secret=AMADEUS_SECRET)
origin_city = input(f"Enter departure city IATA (e.g., LON): you can find yours \u001b]8;;{link}\u001b\\{text}\u001b]8;;\u001b\\  ").upper()

search_date = (datetime.date.today() + datetime.timedelta(days=14)).isoformat()


# feel free to add to your wanted cities
global_hubs = [
    'PAR', 'BER', 'MAD', 'ROM', 'AMS', 'LIS', 'DUB', 'VIE', 'BCN', 'PRG',
    'IST', 'ATH', 'DXB', 'NYC', 'BKK', 'SIN', 'CPH', 'OSL', 'WAW', 'MIL',
    'FRA', 'ZRH', 'CDG', 'MUC', 'BRU', 'STO', 'HEL', 'VCE', 'DUS', 'MAN',
    'TYO', 'HKG', 'ICN', 'SYD', 'MEL', 'DEL', 'BOM', 'TOR', 'MEX', 'GRU',
    'SFO', 'LAX', 'CHI', 'MIA', 'SEA', 'ATL', 'DFW', 'DEN', 'LAS', 'CAI'
]

deals_list = []

print(f"Searching the globe for deals from {origin_city}...")

for dest in global_hubs:
    if dest == origin_city: continue
    try:
        
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin_city,
            destinationLocationCode=dest,
            departureDate=search_date,
            adults=1,
            max=1 
        )
        
        if response.data:
            deal = response.data[0]
            deals_list.append({
                'city': dest,
                'price': float(deal['price']['total']),
                'currency': deal['price']['currency']
            })
            print(f"found flight to {dest} ...") # paste this {deal['price']['total']} {deal['price']['currency']} to the print after {dest} if you wanna see it like FRA: 113.72 EUR
        
        time.sleep(0.1) 
            
    except ResponseError as error:
        continue

if deals_list:
    deals_list.sort(key=lambda x: x['price'])
    
    top_30 = deals_list[:30]
    
    msg = f"🌎 TOP {len(deals_list)}CHEAPEST GLOBAL DEALS 🌎\n"
    msg += f"Origin: {origin_city} | Date: {search_date}\n"
    msg += "--------------------------------\n\n"
    
    for i, d in enumerate(top_30, 1):
        msg += f"{i}. {d['city']}: {d['price']} {d['currency']}\n"
        if i % 10 == 0:
            msg += "\n"
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})
    print(f"\n Found {len(deals_list)} deals. All {len(deals_list)} sent to Telegram.")
else:
    print("\n No deals found across the global list.")