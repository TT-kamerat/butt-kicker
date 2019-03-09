class Event():
  def __init__(self, datetime, title):
    self.__datetime = datetime
    self.__title = title
    self.__users = []

  def get_datetime(self):
    return self.__datetime

  def get_title(self):
    return self.__title

  def add_user(self, user):
    self.__users.append(user)
    