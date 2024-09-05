from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response

# Etape 0 : charger le token d'un endroit sur
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Etape 1 : Bot setup
intents: Intents = Intents.default()
intents.message_content = True # NOQA
client: Client = Client(intents=intents)

# Etape 2 : Fonctionalités des messages
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message vide car "intents" ne sont pas activé correctement)')
        return
    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

# Etape 3 : Parametrer le demarrage du bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} est en marche !')

# Etape 4 : parametrer les messages entrants
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str   = message.content
    channel: str = (message.channel)

    if message.content.startswith('!'):
        print(f'[{channel}] {username} : "{user_message}"')
        await send_message(message, user_message)

# Etape 5 : Point d'entrée principal
def main() -> None:
    client.run(TOKEN)

if __name__ == '__main__':
    main()