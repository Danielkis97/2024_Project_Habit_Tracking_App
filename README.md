# Habit Tracker Application

## Overview
The Habit Tracker App assists users in creating, monitoring, and analyzing their habits. Users can define habits with specific periodicities (daily or weekly), log their completions, and review their progress. This application aims to help users set personal goals and track their habits, ultimately promoting a healthier and more organized lifestyle.

## UML Class Diagram
The following UML class diagram illustrates the structure of the Habit Tracker App, including the classes and their interactions:
![class_diagram](https://github.com/user-attachments/assets/a636a8d4-53d1-4f1b-826d-0ace748575d9)


## Main Features
The Habit Tracker App offers the following features:
- **Create New Habits:** Define new habits with a start date and periodicity.
- **Log Completions:** Record when habits are completed on specific dates and times.
- **View All Habits:** Display all habits with relevant details like name, start date, and periodicity.
- **Analyze Progress:** Gain insights into habit performance, including current and longest streaks, and view habits grouped by periodicity.
- **Delete Habits:** Remove habits that are no longer being tracked.

## Setup and Installation
> [!IMPORTANT]
> Follow these instructions to set up the Habit Tracker App:



### Prerequisites
- Python 3.7 or later
- Virtual environment setup (recommended)


### Installation Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/Habit_Tracker.git
    cd Habit_Tracker
    ```

2. **Set up a virtual environment (Windows):**
   ```sh
    python -m venv venv
    venv\Scripts\activate
   
   
3. **Install dependencies:**
    ```sh
   pip install -r requirements.txt
    ```

4. **Preload the database with sample data (optional for testing):**
    ```sh
    python preload_database.py
    
    ```
## Using the Application

Here's how to use the Habit Tracking App:

1. **Run the application:**
    ```sh
    python main.py
    ```
   The program will present a menu with options to add a habit, view habits, analyze habits, log entries, and delete habits.

2. **Add a new habit:**

     Follow the prompts to enter the habit name, start date, and periodicity (daily or weekly).


3. **Log an entry:**

     Select a habit and enter the date (YYYY-MM-DD) and timeof the completion. If no time is entered, the current time will be used.


4. **Analyze habits:**

      Choose from various analysis options to see streaks, longest streaks, and habits grouped by periodicity. Let's stop the Nailbiting :D 


5. **Delete a habit:**

      Remove habits that are no longer relevant to keep your list current and focused.

Running Tests

To ensure that all functionalities of the Habit Tracker App work correctly, you can run tests using pytest.
Running the tests:

 Install pytest (if not already installed):


    pip install pytest

Run the tests:



    pytest .
    
> [!NOTE]
>This will execute all test cases and provide a report on the functionality of the application.

## Directory Structure

**main.py:**  Main script to start the Habit Tracker.
  
**db.py:** Manages the database of habits stored in a JSON file.

**habits_class.py:** Defines the Habit class for managing individual habits.

**analyze_habits.py:** Functions to analyze the habits stored in the database.

**preload_database.py:** Script to preload the database with sample habits.

**test_habits.py:** Contains test cases for the Habit Tracker application.

**requirements.txt:** Lists the required Python packages.

**db.json:** JSON file that stores the habit data.
    
  ### Example
    
Imagine you're determined to improve your mindfulness and flexibility through a daily yoga routine. Use the Habit Tracker App predefined habit called "Morning Yoga" or create your own. Each day, log your session, noting the time and duration. Over time, analyze your habit to see how many consecutive days you've maintained your practice. Celebrate your streaks and let the app encourage you to keep going! You'll enjoy the benefits of increased flexibility, reduced stress, and a greater sense of well-being.

> [!TIP]
> Building new habits requires consistency and patience. Celebrate small victories and don't get discouraged by occasional setbacks. The Habit Tracker App helps you track your progress and stay motivated. Remember, small steps lead to big changes. Keep going!
