import requests
from telethon_module import TelegramBot
from time import sleep

### https://my.telegram.org/ ### CREATE API HERE

api_id = 'ID APP' ## API ID TELEGRAM INT
api_hash = 'API HASH' # API HASH TELEGRAM
bot = TelegramBot('USER SESION', api_id, api_hash)
client = bot.client

async def main():

    r = requests.get("https://www.etherchain.org/api/gasnow?utm_source=gasnow-fetcher")

    data = r.json()['data']

    eth_price = data['priceUSD']

    gas_rapid = round((data['rapid'] / 1000000000))

    comision_contract = round( ( ( ( gas_rapid * eth_price ) / 10000000 ) * eth_price ) / 2, 2 )

    comssion_for_send = round( ( ( ( gas_rapid * eth_price ) / 100000000 ) * eth_price ) / 2, 2 )

    print(gas_rapid)

    print(round(comision_contract, 2))
    print(round(comssion_for_send, 2))

    await bot.SendAlert(eth_price, gas_rapid, comision_contract, comssion_for_send)

with client:
    while True:
        client.loop.run_until_complete(main())
        sleep(900)