"""
This module contains the test cases for the Habit Tracking application.
"""

import unittest
import json
from datetime import datetime
from habits_class import Habit
from db import Database

class TestHabit(unittest.TestCase):
    """
    Test cases for the Habit class.
    """

    def setUp(self):
        """
        Sets up the test cases.
        """
        self.habit_daily = Habit(
            name="Test Daily Habit",
            start_date=datetime.strptime("2024-07-01", '%Y-%m-%d'),
            log=[
                datetime.strptime("2024-07-01 08:00", '%Y-%m-%d %H:%M'),
                datetime.strptime("2024-07-02 08:00", '%Y-%m-%d %H:%M')
            ],
            periodicity="daily"
        )

        self.habit_weekly = Habit(
            name="Test Weekly Habit",
            start_date=datetime.strptime("2024-07-01", '%Y-%m-%d'),
            log=[
                datetime.strptime("2024-07-01 08:00", '%Y-%m-%d %H:%M'),
                datetime.strptime("2024-07-08 08:00", '%Y-%m-%d %H:%M')
            ],
            periodicity="weekly"
        )

    def test_calculate_streak_daily(self):
        """
        Tests the calculation of the current streak for a daily habit.
        """
        self.assertEqual(self.habit_daily.calculate_streak(), 2)

    def test_calculate_streak_weekly(self):
        """
        Tests the calculation of the current streak for a weekly habit.
        """
        self.assertEqual(self.habit_weekly.calculate_streak(), 2)

    def test_log_entry_daily(self):
        """
        Tests logging an entry for a daily habit.
        """
        new_log_date = datetime.strptime("2024-07-03 08:00", '%Y-%m-%d %H:%M')
        self.habit_daily.log_entry(new_log_date)
        self.assertIn(new_log_date, self.habit_daily.log)

    def test_log_entry_weekly(self):
        """
        Tests logging an entry for a weekly habit.
        """
        new_log_date = datetime.strptime("2024-07-15 08:00", '%Y-%m-%d %H:%M')
        self.habit_weekly.log_entry(new_log_date)
        self.assertIn(new_log_date, self.habit_weekly.log)

class TestDatabase(unittest.TestCase):
    """
    Test cases for the Database class.
    """

    def setUp(self):
        """
        Sets up the test cases.
        """
        self.db = Database(db_file="test_db.json")
        self.habit = Habit(
            name="Test Habit",
            start_date=datetime.strptime("2024-07-01", '%Y-%m-%d'),
            log=[
                datetime.strptime("2024-07-01 08:00", '%Y-%m-%d %H:%M'),
                datetime.strptime("2024-07-02 08:00", '%Y-%m-%d %H:%M')
            ],
            periodicity="daily"
        )
        self.db.add_habit(self.habit)

    def tearDown(self):

        """Cleans up after the test cases."""

        import os
        os.remove("test_db.json")

    def test_add_habit(self):
        """
        Tests adding a new habit to the database.
        """
        new_habit = Habit(
            name="New Test Habit",
            start_date=datetime.strptime("2024-07-03", '%Y-%m-%d'),
            log=[],
            periodicity="daily"
        )
        self.db.add_habit(new_habit)
        self.assertIn(new_habit, self.db.get_all_habits())

    def test_delete_habit(self):
        """
        Tests deleting a habit from the database.
        """
        self.db.delete_habit(self.habit.name)
        self.assertNotIn(self.habit, self.db.get_all_habits())

    def test_get_habits_by_periodicity(self):
        """
        Tests retrieving habits by their periodicity.
        """
        habits = self.db.get_habits_by_periodicity("daily")
        self.assertIn(self.habit, habits)

    def test_get_longest_streak_all_habits(self):
        """
        Tests retrieving the longest streak of all habits.
        """
        longest_streak, habit_name = self.db.get_longest_streak_all_habits()
        self.assertEqual(longest_streak, 2)
        self.assertEqual(habit_name, "Test Habit")

    def test_get_longest_streak_for_habit(self):

    """Tests retrieving the longest streak for a specific habit."""

        longest_streak = self.db.get_longest_streak_for_habit(self.habit.name)
        self.assertEqual(longest_streak, 2)

    def test_save_db(self):
        """
        Tests saving the database to a JSON file.
        """
        self.db.save_db()
        with open("test_db.json", "r") as file:
            data = json.load(file)
            self.assertEqual(len(data), 1)

    def test_load_db(self):
        """
        Tests loading the database from a JSON file.
        """
        self.db.save_db()
        new_db = Database(db_file="test_db.json")
        self.assertEqual(len(new_db.get_all_habits()), 1)

if __name__ == "__main__":
    unittest.main()
