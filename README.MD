# OMNIFLY BOT
we all have the dream to go to every major/favourite cities across the globe but none of us want to pay $500-$1000 and would wish to catch $50-$250 flights but never do. well Fret not.
# WELCOME TO  OMNIFLY

## what it does
OMNIFLY finds the absolute cheapest flight deals from your home airport to major global hubs. It checks for available flights for the next 14 days, sorts them by cheapness, and pings the top 30 directly to your Telegram.
## features
- **amadeus** uses [amadeus's](https://developers.amadeus.com/) API to get the flights
- **Telegram** uses [Telegram's](https://web.telegram.org/a/) bot as IM(Instant messaging) to send and sends it to your telegram 
 - **requests** uses the [requests](https://requests.readthedocs.io/en/latest/) modulo to post the msg to your telegram 
- **datetime** uses the [datetime](https://docs.python.org/3/library/datetime.html) modulo so the searched flights could be exactly the days you want
- **time** uses the time modulo so make the program does not make too many requests in a very short time, possibly making your program crash  

## 🛠 Setup
1. **Install Dependencies:**
   ```bash
   pip install amadeus

2. **Requirements**
    - **AMADEUS KEY** 
    - **AMADEUS SECRET**
    - **TELEGRAM TOKEN**
    - **TELEGRAM CHAT ID**
    you can get those requirements in their respective webs

## config
    In main.py, you can customize the global_hubs list. Want to focus only on Europe? Delete the Asian hubs. Want to find flights to Antarctica? Add it (though Amadeus might laugh at you).

> [!ALERT]
> Amadeus's Free Tier is World-class documentation providing you with a front-row seat to a 500 error and a 2021 regurgitated almanac. don't blame me for it if some parts of the
> program break for you. 
> as Bjarne Stroustrup’s (the creator of C++) said "There are only two kinds of software: the ones developers complain about and the ones nobody uses." but Amadeus is neither
> since we all collectively despise you but have no other choice. i genuinely believe you want to piss us off so much that we buy your enterprise. like kevin o'leary gives the worst
> shark tank deals so others may sound heavenly. 

> [!NOTE]
> you won't be able to get any really good flights or any at all since this is using the free tier
