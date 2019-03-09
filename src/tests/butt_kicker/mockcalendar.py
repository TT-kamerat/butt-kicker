class MockCalendar():
  def __init__(self):
    self.__events = []
  
  def get_events(self):
    return self.__events
  
  def add_event(self, event):
    self.__events.append(event)