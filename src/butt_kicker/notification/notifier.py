class Notifier():
  def __init__(self):
    pass
  
  def ping_attendees(self, bot, notification_queue):
    while True:
      notification = notification_queue.get_next()
      if notification is None:
        break
      
      msg = self.get_message(notification)
      bot.send_message(msg)

      notification_queue.remove_first()

  def get_message(self, notification):
    return "asd"
