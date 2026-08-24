# Import SQLite
import sqlite3

# Connect to the database
connection = sqlite3.connect("student_management.db")

# Create a cursor to execute SQL commands
cursor = connection.cursor()

# Execute SQL query to find students who scored above 80 in Python 
cursor.execute(""" SELECT student_id  FROM Grades
    WHERE course_id = 110   AND grade > 80     """)

ids = cursor.fetchall()

cursor.execute("""
    CREATE TEMP TABLE TempStudents (
        student_id INTEGER   )
""")

# Insert multiple  records
cursor.executemany(
    "INSERT INTO TempStudents VALUES (?)",
    ids
)


cursor.execute("""
    SELECT name
    FROM Students
    WHERE id IN (
        SELECT student_id
        FROM TempStudents
    )
""")

students = cursor.fetchall()

for student in students:
    print(student[0])


# Close the database connection
connection.close()