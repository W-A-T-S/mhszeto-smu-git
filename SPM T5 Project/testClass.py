import unittest
from classDomain import Class

class testClass(unittest.TestCase):
    def test_find_all_class(self):
        s = Class('CR101','CL1','Jane','JaneBestEngineer','LarryThepaperCHaser','2021-10-15 00:00:00.000Z','2021-10-25 00:00:00.000Z','2021-10-26 00:00:00.000Z','2021-11-26 00:00:00.000Z',45,20)
        trainer_username = s.trainer_username()
        class_size = s.class_size()
        class_available_slots = s.class_available_slots()
        self.assertEqual(trainer_username,JaneBestEngineer)
        self.assertEqual(class_size,45)
        self.assertEqual(class_available_slots,20)

        


    