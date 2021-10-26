from telethon import TelegramClient
import asyncio

class TelegramBot:

    def __init__(self, user: str, api_id: int, api_hash: str):
        self.__loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.__loop)
        self.user = user
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient(self.user, self.api_id, self.api_hash, loop=self.__loop)
        self.client.start()


    async def SendAlert(self, eth_price, gas_rapid, comission):
        print('Enviando Alerta')
        await self.client.send_message('me', f'Alert Gas ETH price: {str(eth_price)}$\nGas: {str(gas_rapid)}\nCommision (USD): {str(comission)}$')



