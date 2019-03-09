class GoogleCalendar():
  def __init__(self, url, credentials, update_interval=60):
    self.__url = url
    self.__credentials = credentials
    self.__update_interval = update_interval

  def set_update_interval(self, update_interval):
    self.__update_interval = update_interval

  def get_events(self):
    return []
