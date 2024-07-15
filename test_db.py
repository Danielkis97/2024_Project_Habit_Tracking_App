from db import Database
from habits_class import Habit
from datetime import datetime

def test_database():
    db = Database("db.json")

    # Test loading habits
    print("All habits loaded from db.json:")
    for habit in db.get_all_habits():
        print(f"Name: {habit.name}, Start Date: {habit.start_date}, Log: {habit.log}, Periodicity: {habit.periodicity}")

    # Test adding a new habit
    new_habit = Habit(
        name="New Habit",
        start_date=datetime.strptime("2024-07-01 09:00:00", '%Y-%m-%d %