"""
This module provides the Database class for managing habits stored in a JSON file.
"""

import json
from habits_class import Habit
from datetime import datetime

class Database:
    """
    Manages the database of habits.
    """

    def __init__(self, db_file="db.json"):
        """
        Initializes the Database with a specified file.

        Args:
            db_file (str): The path to the JSON file storing the habits.
        """
        self.db_file = db_file
        self.habits = self.load_db()

    def load_db(self):
        """
        Loads habits from the JSON file.

        Returns:
            list: List of Habit objects.
        """
        try:
            with open(self.db_file, "r") as file:
                data = json.load(file)
                habits = []
                for item in data:
                    habits.append(Habit(
                        name=item['name'],
                        start_date=datetime.strptime(item['start_date'], '%Y-%m-%d %H:%M:%S'),
                        log=[datetime.strptime(log_datetime, '%Y-%m-%d %H:%M:%S') for log_datetime in item['log']],
                        periodicity=item.get('periodicity', 'daily')
                    ))
                return habits
        except FileNotFoundError:
            return []

    def save_db(self):
        """
        Saves the current habits to the JSON file.
        """
        data = []
        for habit in self.habits:
            data.append({
                'name': habit.name,
                'start_date': habit.start_date.strftime('%Y-%m-%d %H:%M:%S'),
                'log': [log_datetime.strftime('%Y-%m-%d %H:%M:%S') for log_datetime in habit.log],
                'periodicity': habit.periodicity
            })
        with open(self.db_file, "w") as file:
            json.dump(data, file, indent=4)

    def get_all_habits(self):
        """
        Retrieves all habits.

        Returns:
            list: List of all Habit objects.
        """
        return self.habits

    def get_habit(self, name):
        """
        Retrieves a habit by name.

        Args:
            name (str): Name of the habit.

        Returns:
            Habit: Habit object with the specified name.
        """
        for habit in self.habits:
            if habit.name == name:
                return habit
        return None

    def add_habit(self, habit):
        """
        Adds a new habit to the database.

        Args:
            habit (Habit): Habit object to add.
        """
        self.habits.append(habit)
        self.save_db()

    def delete_habit(self, name):
        """
        Deletes a habit by name.

        Args:
            name (str): Name of the habit to delete.
        """
        self.habits = [habit for habit in self.habits if habit.name != name]
        self.save_db()

    def get_habits_by_periodicity(self, periodicity):
        """
        Retrieves habits by periodicity.

        Args:
            periodicity (str): Filter by periodicity.

        Returns:
            list: List of Habit objects.
        """
        return [habit for habit in self.habits if habit.periodicity == periodicity]

    def get_longest_streak_all_habits(self):
        """
        Retrieves the longest streak of all habits.

        Returns:
            int: Longest streak and the name of the habit.
        """
        if not self.habits:
            return 0, None
        longest_streak_habit = max(self.habits, key=lambda habit: habit.calculate_streak())
        return longest_streak_habit.calculate_streak(), longest_streak_habit.name

    def get_longest_streak_for_habit(self, name):
        """
        Retrieves the longest streak for a specific habit.

        Args:
            name (str): Name of the habit.

        Returns:
            int: The longest streak for the specific habit.
        """
        habit = self.get_habit(name)
        return habit.calculate_streak() if habit else 0
