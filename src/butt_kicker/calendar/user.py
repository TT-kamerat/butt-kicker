class User():
  def __init__(self, tg_nick, name_in_calendar):
    self.__tg_nick = tg_nick
    self.__name_in_calendar = name_in_calendar

  def get_tg_nick(self):
    return self.__tg_nick

  def get_name_in_calendar(self):
    return self.__name_in_calendar
    