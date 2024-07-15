"""
This module provides the Habit class for managing individual habits.
"""

from datetime import datetime, timedelta

class Habit:
    """
    Represents a habit.
    """

    def __init__(self, name, start_date, log, periodicity='daily'):
        """
        Initializes a new Habit.

        Args:
            name (str): Name of the habit.
            start_date (datetime): Start date of the habit.
            log (list): List of completion datetimes.
            periodicity (str): Periodicity of the habit ('daily' or 'weekly').
        """
        self.name = name
        self.start_date = start_date
        self.log = log
        self.periodicity = periodicity

    def calculate_streak(self):
        """
        Calculates the current streak of the habit.

        Returns:
            int: Current streak of consecutive completions.
        """
        streak = 0
        today = datetime.today().date()

        if not self.log:
            return streak

        sorted_log = sorted(self.log, reverse=True)
        current_date = sorted_log[0].date()

        if self.periodicity == 'daily':
            for log_datetime in sorted_log:
                log_date = log_datetime.date()
                if log_date == current_date:
                    streak += 1
                    current_date -= timedelta(days=1)
                else:
                    break
        elif self.periodicity == 'weekly':
            for log_datetime in sorted_log:
                log_date = log_datetime.date()
                if log_date >= current_date - timedelta(days=6):
                    streak += 1
                    current_date -= timedelta(days=7)
                else:
                    break

        return streak

    def log_entry(self, log_datetime):
        """
        Logs a new entry for the habit.

        Args:
            log_datetime (datetime): Datetime to log for the habit.
        """
        log_datetime = log_datetime.replace(second=0, microsecond=0)
        if log_datetime not in self.log:
            self.log.append(log_datetime)
            self.log = sorted(self.log)
