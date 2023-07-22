import requests
import asyncio
import time
from bs4 import BeautifulSoup
from telegram import Bot

url = 'https://zehabesha.com/'

bot_token = '6189595360:AAHi9bDFlKbS9yPqZn__rrVJOsiQZhSxM7k'
chat_id = '@Newscraps'

bot = Bot(token=bot_token)

async def send_news():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    titles = soup.find_all('div', class_='elementor-post__text') 
    links = soup.find_all('a', class_='elementor-post__thumbnail__link')
    descriptions = soup.find_all('div', class_='elementor-post__excerpt')
    images = soup.find_all('a', class_='elementor-post__thumbnail__link')

    num_messages = min(6, len(titles))

    for i in range(num_messages):
        title = titles[i].get_text()
        link = links[i].get('href')
        description = descriptions[i].get_text('p') if i < len(descriptions) else "Description not found"
        image = images[i].find('img')['data-src']
        
        # print(image)
  
        message = f"*{description}*\n{title} Read more...\n{link}\n\n"

        # await bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')
        await bot.send_photo(chat_id=chat_id, photo=image, caption=message, parse_mode='Markdown')

# async def main():
#     while True:
#         await send_news()
#         time.sleep(10)

# asyncio.run(main())
# 
asyncio.run(send_news())
