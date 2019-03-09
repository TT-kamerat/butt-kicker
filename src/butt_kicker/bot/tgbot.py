import telegram

class TgBot():
  def __init__(self, token, channel):
    self.__token = token
    self.__channel = channel
    self.__bot = telegram.Bot(self.__token)

  def send_message(self, message):
    self.__bot.send_message(self.__channel, message)
