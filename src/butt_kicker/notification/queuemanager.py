from .notificationqueue import NotificationQueue
from .notification import Notification
from datetime import datetime, timedelta

class QueueManager():
  def __init__(self, today = None):
    self.__now = today if today else datetime.today()
    self.__intervals = [7, 1]

  def get_notification_queue(self, calendar):
    queue = NotificationQueue()
    events = calendar.get_events()

    for e in events:
      for i in self.__intervals:
        today = (self.__now + timedelta(i - 1)).date()
        day_after_tomorrow = (self.__now + timedelta(i + 1)).date()
        
        if today < e.get_datetime().date() < day_after_tomorrow:
          notification = Notification(e, self.__now)
          queue.add(notification)

    return queue
