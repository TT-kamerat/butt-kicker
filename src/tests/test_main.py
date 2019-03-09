import unittest
from datetime import datetime, timedelta
from butt_kicker.notification.notificationqueue import NotificationQueue
from butt_kicker.notification.notification import Notification
from butt_kicker.notification.notifier import Notifier
from butt_kicker.calendar.event import Event
from butt_kicker.notification.queuemanager import QueueManager
from .butt_kicker.mockbot import MockBot
from .butt_kicker.mockcalendar import MockCalendar

class TestSomething(unittest.TestCase):
  def setUp(self):
    self.nq = NotificationQueue()
    n = Notification("Event", datetime.today())
    self.nq.add(n)
    self.nq.add(n)

  def test_1(self):  
    self.assertTrue(len(self.nq._NotificationQueue__items) == 2)
    self.nq.remove_first()
    self.assertTrue(len(self.nq._NotificationQueue__items) == 1)

  def test_2(self):
    n1 = Notification("Event", datetime.today())
    n2 = Notification("Event", datetime.today() - timedelta(seconds=1))
    self.assertTrue(n2.before(n1))
    # self.assertFalse(n1.before(n1))

  def test_3(self):
    for i in range(2):
      self.nq.remove_first()  

    with self.assertRaises(IndexError):
        self.nq.remove_first()
  
  def test_4(self):
    now = datetime.today()
    calendar = MockCalendar()
    calendar.add_event(Event(now - timedelta(1), "Event_same"))
    calendar.add_event(Event(now - timedelta(0), "Event_same"))
    calendar.add_event(Event(now - timedelta(2), "Event_same"))
    calendar.add_event(Event(now + timedelta(1), "Event2"))
    calendar.add_event(Event(now + timedelta(1), "Event_same"))
    calendar.add_event(Event(now + timedelta(7), "Event_same"))
    calendar.add_event(Event(now + timedelta(7), "Event_same1"))
    calendar.add_event(Event(now + timedelta(8), "Event_same1"))
    calendar.add_event(Event(now + timedelta(6), "Event_same1"))
    calendar.add_event(Event(now + timedelta(2), "Event4"))
    calendar.add_event(Event(now - timedelta(1), "Event5"))
    
    manager = QueueManager()
    queue = manager.get_notification_queue(calendar)

    bot = MockBot()
    notifier = Notifier()
    notifier.ping_attendees(bot, queue)
    
    self.assertEqual(len(bot.get_sent_messages()), 4)

  def test_5(self):
    now = datetime.today()
    calendar = MockCalendar()
    notifier = Notifier()    
    days = range(2*365)

    for i in range(7):
      calendar.add_event(Event(now - timedelta(i), "Event"))

    for i in days:
      calendar.add_event(Event(now + timedelta(i), "Event"))

    for i in days:
      bot = MockBot()
      manager = QueueManager(now + timedelta(i))
      queue = manager.get_notification_queue(calendar)
      notifier.ping_attendees(bot, queue)
      
      # Two intervals 7 and 1 day before
      messages = 2
      
      # 7 days before notifications done
      if len(days)-i < 8:
        messages = 1

      # 1 day notifications done        
      if i == len(days)-1: 
        messages = 0

      self.assertEqual(len(bot.get_sent_messages()), messages)
