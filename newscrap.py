
import requests
import asyncio
from bs4 import BeautifulSoup
from telegram import Bot
import schedule
import time

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

    num_messages = min(6, len(titles))
    message = ''
    for i in range(num_messages):
        title = titles[i].get_text()
        link = links[i].get('href')
        description = descriptions[i].get_text('p') if i < len(descriptions) else "Description not found"
  
        message += f"*========================================================\nTitle:{title}*\n\n{description}\n\n{link}\n\n"

    await bot.send_message(chat_id=chat_id, text=message, parse_mode='Markdown')

def job():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(send_news())
    

# Schedule the job to run every hour
schedule.every().hour.do(job)

# Keep the script running indefinitely
while True:
    schedule.run_pending()
    time.sleep(1)

