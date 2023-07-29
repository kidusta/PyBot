from bs4 import BeautifulSoup
import requests
import telebot

# ... (your existing code)
url = 'https://zehabesha.com/'
esat_radio_url = 'https://zehabesha.com/topics/esat-radio-news-update-zehabesha/'
Awaze_News_url = 'https://zehabesha.com/topics/awaze-news-today-breaking-politics-news-zehabesha/'
Politics_url = 'https://zehabesha.com/topics/politics-news-today-breaking-politics-news-zehabesha/'
World_news_url = 'https://zehabesha.com/topics/world-news-today-breaking-news-ethiopia-zehabesha/'
Business_news_url = 'https://zehabesha.com/topics/latest-business-news-business-headlines-zehabesha/'

bot_token = '6189595360:AAHi9bDFlKbS9yPqZn__rrVJOsiQZhSxM7k'
chat_id = '@Newscraps'

bot = telebot.TeleBot(token=bot_token)
@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_send_news = telebot.types.KeyboardButton(text="Send News")
    button_esat_radio_news = telebot.types.KeyboardButton(text="ESAT Radio News")
    button_awaze_news = telebot.types.KeyboardButton(text="Awaze News")
    button_politics_news = telebot.types.KeyboardButton(text="Politics")
    button_world_news = telebot.types.KeyboardButton(text="World News")
    button_business_news = telebot.types.KeyboardButton(text="Business News")
    
    keyboard.add(button_send_news, button_esat_radio_news, button_awaze_news, button_politics_news, button_world_news, button_business_news)

    bot.send_message(message.chat.id, "Hello! Press the buttons to get the latest news.", reply_markup=keyboard)

    # Create inline buttons for each option
    # Creating the inline buttons one by one and adding them to the inline_keyboard
    btn1 = telebot.types.InlineKeyboardButton(text="Send News", callback_data="send_news")
    btn2 = telebot.types.InlineKeyboardButton(text="ESAT Radio News", callback_data="esat_radio_news")
    btn3 = telebot.types.InlineKeyboardButton(text="Awaze News", callback_data="awaze_news")
    btn4 = telebot.types.InlineKeyboardButton(text="Politics", callback_data="politics_news")
    btn5 = telebot.types.InlineKeyboardButton(text="World News", callback_data="world_news")
    btn6 = telebot.types.InlineKeyboardButton(text="Business News", callback_data="business_news")

# Creating the inline_keyboard and adding the buttons to it
    inline_keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
    inline_keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6)


    # Send the welcome message with inline buttons
    bot.send_message(message.chat.id, "If you have any questions before you start, please feel free to ask.", reply_markup=inline_keyboard)

# Handle inline button presses
@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    message = call.message

    if call.data == "send_news":
        send_news(message)
    elif call.data == "esat_radio_news":
        send_esat_radio_news(message)
    elif call.data == "awaze_news":
        send_awaze_news(message)
    elif call.data == "politics_news":
        send_politics_news(message)
    elif call.data == "world_news":
        send_world_news(message)
    elif call.data == "business_news":
        send_business_news(message)

# ... (your existing code)
@bot.message_handler(func=lambda message: message.text == "Send News")
def send_news(message):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles = soup.find_all('h3', class_='elementor-post__title')
    links = soup.find_all('a', class_='elementor-post__thumbnail__link')
    descriptions = soup.find_all('div', class_='elementor-post__excerpt')
    images = soup.find_all('a', class_='elementor-post__thumbnail__link')

    num_messages = min(6, len(titles))

    for i in range(num_messages):
        title = titles[i].get_text() if i < len(titles) else "Title not found"
        link = links[i].get('href') if i < len(links) else "Link not found"
        description = descriptions[i].get_text('p') if i < len(descriptions) else "Description not found"
        image = images[i].find('img')['data-src']  if i < len(images) else "Image not found"

        message = f"*{description}*\n{title} Read more...\n{link}\n\n"

        bot.send_photo(chat_id=chat_id, photo=image, caption=message, parse_mode='Markdown')
        
@bot.message_handler(func=lambda message: message.text == "ESAT Radio News")
def send_esat_radio_news(message):
    response = requests.get(esat_radio_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles1 = soup.find_all('h2', class_='entry-title')
    
    titles = []
    for t in titles1:
        t = t.find('a')['href']
        titles.append(t)

    links1 = soup.find_all('div', class_='post-thumb-img-content post-thumb')
    descriptions1 = soup.find_all('div', class_='entry-content clear')
    images1 = soup.find_all('img', class_='attachment-large size-large wp-post-image')

    num_messages = min(6, len(titles1))

    for i in range(num_messages):
        title = titles1[i].get_text() if i < len(titles1) else "Title not found"
        link = links1[i].find('a')['href'] if i < len(links1) else "Link not found"
        description = descriptions1[i].get_text('p') if i < len(descriptions1) else "Description not found"
        image = images1[i]['data-src'] if i < len(images1) else "Image not found"

        message = f"*{description}*\n\n{title} Read more...\n{link}\n\n"

        bot.send_photo(chat_id=chat_id, photo=image, caption=message, parse_mode='Markdown')


@bot.message_handler(func=lambda message: message.text == "Awaze News")
def send_awaze_news(message):
    response = requests.get(Awaze_News_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles1 = soup.find_all('h2', class_='entry-title')
    
    titles = []
    for t in titles1:
        t = t.find('a')['href']
        titles.append(t)

    links1 = soup.find_all('div', class_='post-thumb-img-content post-thumb')
    descriptions1 = soup.find_all('div', class_='entry-content clear')
    images1 = soup.find_all('img', class_='attachment-large size-large wp-post-image')

    num_messages = min(6, len(titles1))

    for i in range(num_messages):
        title = titles1[i].get_text() if i < len(titles1) else "Title not found"
        link = links1[i].find('a')['href'] if i < len(links1) else "Link not found"
        description = descriptions1[i].get_text('p') if i < len(descriptions1) else "Description not found"
        image = images1[i]['data-src'] if i < len(images1) else "Image not found"

        message = f"*{description}*\n{title} Read more...\n{link}\n\n"

        bot.send_photo(chat_id=chat_id, photo=image, caption=message, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "Politics")
def send_politics_news(message):
    response = requests.get(Politics_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles1 = soup.find_all('h2', class_='entry-title')
    
    titles = []
    for t in titles1:
        t = t.find('a')['href']
        titles.append(t)

    links1 = soup.find_all('div', class_='post-thumb-img-content post-thumb')
    descriptions1 = soup.find_all('div', class_='entry-content clear')
    images1 = soup.find_all('img', class_='attachment-large size-large wp-post-image')

    num_messages = min(6, len(titles1))

    for i in range(num_messages):
        title = titles1[i].get_text() if i < len(titles1) else "Title not found"
        link = links1[i].find('a')['href'] if i < len(links1) else "Link not found"
        description = descriptions1[i].get_text('p') if i < len(descriptions1) else "Description not found"
        image = images1[i]['data-src'] if i < len(images1) else "Image not found"

        message = f"*{title}*\n\n{description}\n{link}\n\n"

        bot.send_photo(chat_id=chat_id, photo=image, caption=message, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "World News")
def send_world_news(message):
    response = requests.get(World_news_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles1 = soup.find_all('h2', class_='entry-title')
    
    titles = []
    for t in titles1:
        t = t.find('a')['href']
        titles.append(t)

    links1 = soup.find_all('div', class_='post-thumb-img-content post-thumb')
    descriptions1 = soup.find_all('div', class_='entry-content clear')
    images1 = soup.find_all('img', class_='attachment-large size-large wp-post-image')

    num_messages = min(6, len(titles1))

    for i in range(num_messages):
        title = titles1[i].get_text() if i < len(titles1) else "Title not found"
        link = links1[i].find('a')['href'] if i < len(links1) else "Link not found"
        description = descriptions1[i].get_text('p') if i < len(descriptions1) else "Description not found"
        image = images1[i]['data-src'] if i < len(images1) else "Image not found"

        message = f"*{title}*\n\n{description}\n{link}\n\n"

        bot.send_photo(chat_id=chat_id, photo=image, caption=message, parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.text == "Business News")
def send_business_news(message):
    response = requests.get(Business_news_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titles1 = soup.find_all('h2', class_='entry-title')
    
    titles = []
    for t in titles1:
        t = t.find('a')['href']
        titles.append(t)

    links1 = soup.find_all('div', class_='post-thumb-img-content post-thumb')
    descriptions1 = soup.find_all('div', class_='entry-content clear')
    images1 = soup.find_all('img', class_='attachment-large size-large wp-post-image')

    num_messages = min(6, len(titles1))

    for i in range(num_messages):
        title = titles1[i].get_text() if i < len(titles1) else "Title not found"
        link = links1[i].find('a')['href'] if i < len(links1) else "Link not found"
        description = descriptions1[i].get_text('p') if i < len(descriptions1) else "Description not found"
        image = images1[i]['data-src'] if i < len(images1) else "Image not found"

        message = f"*{title}*\n\n{description}\n{link}\n\n"

        bot.send_photo(chat_id=chat_id, photo=image, caption=message, parse_mode='Markdown')

if __name__ == "__main__":
    bot.polling()
