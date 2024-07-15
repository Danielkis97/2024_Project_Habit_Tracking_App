"""
This module provides functions to analyze habits stored in the database.
"""

import questionary
from db import Database
from habits_class import Habit

def analyze_habits():
    """
    Displays the current streak for a selected habit from the database.
    """
    db = Database()
    habits = db.get_all_habits()

    if not habits:
        print("No habits found.")
        return

    habit_names = [habit.name for habit in habits]
    habit_name = questionary.select(
        "Select a habit to analyze:",
        choices=habit_names
    ).ask()

    if habit_name is None:
        print("No habit selected.")
        return

    habit = db.get_habit(habit_name)
    if habit is None:
        print("Habit not found.")
        return

    print(f"Analyzing habit: {habit.name}")

    # Perform analysis
    streak = habit.calculate_streak()
    print(f"Current streak: {streak} {habit.periodicity} entries")

def analyze_specific_habit(db):
    """
    Analyzes a specific habit selected by the user from the database.

    Args:
        db (Database): The database used for analysis.
    """
    habits = db.get_all_habits()

    if not habits:
        print("No habits found.")
        return

    habit_names = [habit.name for habit in habits]
    habit_name = questionary.select(
        "Select a habit to analyze:",
        choices=habit_names
    ).ask()

    if habit_name is None:
        print("No habit selected.")
        return

    habit = db.get_habit(habit_name)
    if habit is None:
        print("Habit not found")
        return

    print(f"Analyzing habit: {habit.name}")

    # Perform analysis
    streak = habit.calculate_streak()
    print(f"Current streak: {streak} {habit.periodicity} entries")

def list_habits_by_periodicity(db):
    """
    Lists habits by their periodicity (daily/Weekly).

    Args:
        db (Database): The database instance to use for analysis.
    """
    periodicity = questionary.select(
        "Select periodicity:",
        choices=["daily", "weekly"]
    ).ask()

    habits = db.get_habits_by_periodicity(periodicity)
    print(f"Habits with {periodicity} periodicity:")
    for habit in habits:
        print(f"- {habit.name}")

def longest_streak_for_habit(db):
    """
    Displays the longest streak for a specific habit.

        db (Database): The database instance to use for analysis.
    """
    habits = db.get_all_habits()

    if not habits:
        print("No habits found.")
        return

    habit_names = [habit.name for habit in habits]
    habit_name = questionary.select(
        "Select a habit to analyze:",
        choices=habit_names
    ).ask()

    if habit_name is None:
        print("No habit selected.")
        return

    streak = db.get_longest_streak_for_habit(habit_name)
    print(f"The longest streak is {streak} by habit '{habit_name}'")
