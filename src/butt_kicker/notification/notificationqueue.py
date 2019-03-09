class NotificationQueue():
  def __init__(self):
    self.__items = []

  def get_next(self):
    return self.__items[0] if len(self.__items) != 0 else None

  def add(self, notification):
    for i, item in enumerate(self.__items):
      if notification.before(item):
        self.__items.insert(i, notification)
        return

    self.__items.append(notification)

  def remove_first(self):
    self.__items.pop(0)
