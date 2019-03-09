class MockBot():
  def __init__(self):
    self.__messages = []
  
  def get_sent_messages(self):
    return self.__messages
  
  def send_message(self, msg):
    self.__messages.append(msg)