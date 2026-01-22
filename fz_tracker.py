"""
Objectives: 
1. To design a simple program that records and monitors student scores and grades.  
2. To predict student performance trends based on previous results.  
3. To provide notification reminders for studying.  
4. To allow exporting or saving student grade records for reference.  
5. To create an easy-to-use academic tracking tool for both students and teachers.
"""

# Placeholding values

# formative assessments - 30%
short_quiz = 0.1
homework = 0.05
long_quiz = 0.15
# Alternative assessments - 20%
recitation = 0.05
presentations = 0.15
# Projects - 20%
projects = 0.20

def process_score():
    print("")
def view_scores():
    print("")
def view_report():
    print("")
    
# displays menu

def display_home():
    print("Welcome to FZ A-Tracker")
    print("""
          ------Menu------
          1. Enter score.
          2. View scores.
          3. View report. 
          4. View prediction.
          0. Exit.          
          """)
    choice=int(input("Enter choice: "))
    return choice

# processes your choice

def process_choice(choice):
    if choice == 1:
        process_score()
    elif choice == 2:
        view_scores()
    elif choice == 3:
        view_report()

display_home()
