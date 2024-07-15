# preload_database.py
"""
This script preloads the habit database with predefined habits.
"""

import json
from db import Database
from habits_class import Habit
from datetime import datetime

def preload_db():
    """
    Preloads the database with predefined habits.
    """
    db = Database()

    # Clear existing habits to avoid duplication
    db.habits = []
    db.save_db()

    # Define the predefined habits
    predefined_habits = [
        {
            "name": "Morning Yoga",
            "start_date": "2024-07-01 06:30:00",
            "log": [
                "2024-07-01 06:30:00",
                "2024-07-02 07:00:00",
                "2024-07-03 07:30:00",
                "2024-07-04 08:00:00",
                "2024-07-05 08:30:00",
                "2024-07-06 09:00:00",
                "2024-07-07 09:30:00",
                "2024-07-08 10:00:00",
                "2024-07-09 10:30:00",
                "2024-07-10 11:00:00",
                "2024-07-11 11:30:00",
                "2024-07-12 12:00:00",
                "2024-07-13 12:30:00",
                "2024-07-14 13:00:00",
                "2024-07-15 13:30:00"
            ],
            "periodicity": "daily"
        },
        {
            "name": "Reading a Book",
            "start_date": "2024-07-01 20:45:00",
            "log": [
                "2024-07-01 20:45:00",
                "2024-07-02 21:00:00",
                "2024-07-03 21:15:00",
                "2024-07-04 21:30:00",
                "2024-07-05 21:45:00",
                "2024-07-06 22:00:00",
                "2024-07-07 22:15:00",
                "2024-07-08 22:30:00",
                "2024-07-09 22:45:00",
                "2024-07-10 23:00:00",
                "2024-07-11 23:15:00",
                "2024-07-12 23:30:00",
                "2024-07-13 23:45:00",
                "2024-07-14 00:00:00",
                "2024-07-15 00:15:00"
            ],
            "periodicity": "daily"
        },
        {
            "name": "Learning Python",
            "start_date": "2024-07-01 08:00:00",
            "log": [
                "2024-07-01 08:00:00",
                "2024-07-02 08:30:00",
                "2024-07-03 09:00:00",
                "2024-07-04 09:30:00",
                "2024-07-05 10:00:00",
                "2024-07-06 10:30:00",
                "2024-07-07 11:00:00",
                "2024-07-08 11:30:00",
                "2024-07-09 12:00:00",
                "2024-07-10 12:30:00",
                "2024-07-11 13:00:00",
                "2024-07-12 13:30:00",
                "2024-07-13 14:00:00",
                "2024-07-14 14:30:00",
                "2024-07-15 15:00:00"
            ],
            "periodicity": "daily"
        },
        {
            "name": "Family Call",
            "start_date": "2024-07-01 18:00:00",
            "log": [
                "2024-07-01 18:00:00",
                "2024-07-08 19:00:00",
                "2024-07-15 20:00:00"
            ],
            "periodicity": "weekly"
        },
        {
            "name": "House Cleaning",
            "start_date": "2024-07-01 07:30:00",
            "log": [
                "2024-07-01 07:30:00",
                "2024-07-08 08:00:00",
                "2024-07-15 09:00:00"
            ],
            "periodicity": "weekly"
        },
        {
            "name": "Quit Nail Biting",
            "start_date": "2024-07-01 13:25:00",
            "log": [
                "2024-07-01 13:25:00",
                "2024-07-02 13:25:00",
                "2024-07-03 13:25:00",
                "2024-07-04 13:25:00",
                "2024-07-05 13:25:00",
                "2024-07-06 13:25:00",
                "2024-07-07 13:25:00",
                "2024-07-08 13:25:00",
                "2024-07-09 13:25:00",
                "2024-07-10 13:25:00",
                "2024-07-11 13:25:00",
                "2024-07-12 13:25:00",
                "2024-07-13 13:25:00",
                "2024-07-14 13:25:00",
                "2024-07-15 13:25:00"
            ],
            "periodicity": "daily"
        }
    ]

    for habit_data in predefined_habits:
        habit = Habit(
            name=habit_data['name'],
            start_date=datetime.strptime(habit_data['start_date'], '%Y-%m-%d %H:%M:%S'),
            log=[datetime.strptime(log, '%Y-%m-%d %H:%M:%S') for log in habit_data['log']],
            periodicity=habit_data['periodicity']
        )
        db.add_habit(habit)

    print("Predefined habits have been added to the database.")

if __name__ == "__main__":
    preload_db()
