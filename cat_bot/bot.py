import os
import random
import time

import slack

import cats_pics


class SlackBot(object):

    def __init__(self):
        self.slack_client = slack.WebClient(os.environ["SLACK_API_TOKEN"], timeout=30)
        self.channel_id = os.environ["SLACK_CHANNEL_ID"]
        self.cats_db = cats_pics.cats_db

    def send_user_hi(self):
        self.slack_client.chat_postMessage(
            channel=self.channel_id,
            text='Hi! Im your cat bot, I promise I will only send you cute cats!')

    def send_user_a_cat(self, cat):
        self.slack_client.chat_postMessage(
            channel=self.channel_id,
            attachments=[{"title": "Cat", "image_url": cat}],
            text="")


if __name__ == '__main__':
    bot = SlackBot()
    bot.send_user_hi()

    for i in range(0, 5):
        random_cat = random.choice(bot.cats_db)
        bot.send_user_a_cat(random_cat)
        time.sleep(5)
