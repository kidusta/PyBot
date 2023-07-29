# PyBot
# Telegram News Bot with Web Scraping

This is a Python script that fetches the latest news from a website and sends it to a Telegram channel using a Telegram bot. The bot uses the BeautifulSoup library to perform web scraping on the website, extracting the necessary news information such as titles, links, and descriptions.

## Requirements

- Python 3.6 or higher
- `requests`
- `beautifulsoup4`
- `python-telegram-bot`
- `schedule`
- `telebot`

## Installation

1. Clone the repository:


git clone https://github.com/your_username/telegram-news-bot.git
cd telegram-news-bot

## Install the required packages:
pip install requests beautifulsoup4 python-telegram-bot schedule

## Configuration
1.Obtain your Telegram bot token by creating a bot on Telegram and getting the API token.

2.Replace 'YOUR_BOT_TOKEN' in the script with your actual bot token.

3.Replace '@Newscraps' in the script with the chat_id of the Telegram channel where you want to post the news.

4.Adjust the url variable in the script to target the website you want to scrape news from.

## Usage

To run the bot, simply execute the Python script:
python newscrap.py

The bot will start posting the latest news to the specified Telegram channel every hour.

## Customization

You can modify the num_messages variable in the send_news function to control the number of news items sent in each message.

Adjust the schedule.every().hour.do(job) line to customize the frequency of news updates.



