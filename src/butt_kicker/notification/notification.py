class Notification():
  def __init__(self, event, date):
    self.__event = event
    self.__date = date

  def get_date(self):
    return self.__date

  def before(self, b):
    # return self.__date < b.__date
    return True
