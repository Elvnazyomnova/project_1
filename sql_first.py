import sqlite3
connection = sqlite3.connect('teatcherss.db')
cursor = connection.cursor()

cursor.execute("""SELECT * FROM Teatcher""")
columnname = cursor.description
print(columnname)

def get_connection():
  connection = sqlite3.connect('teatcherss.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_student(student_id):
  connection = get_connection()
  cursor = connection.cursor()
  query = """SELECT * FROM School JOIN Students ON School.School_Id = Students.School_Id WHERE Student_Id = ?"""
  cursor.execute(query, (student_id,))
  records = cursor.fetchall()
  print(records)
  connection.close()
  print ("Данные по студенту")
  for row in records:
    print ("ID студ", row[3])
    print ("Имя", row[4])
    print ("ID школы", row[0])
    print ("Название школы", row[1])

get_student(202)

def get_student(student_id):
  connection = sqlite3.connect('Students.db')
  cursor = connection.cursor()
  query = """SELECT * FROM Students Where Student_Id = ?"""
  cursor.execute(query, (student_id,))
  records = cursor.fetchall()
  connection.close()
  for row in records:
    print ("ID студ", row[0])
    print ("Имя", row[1])
    print ("ID школы", row[2])
    #print(row[2])
    school_id = row[2]
  get_schoolname(school_id)

def get_schoolname(school_id):
  connection = sqlite3.connect('Schools.db')
  cursor = connection.cursor()
  query = """SELECT * FROM School WHERE School_Id = ?"""
  cursor.execute(query, (school_id,))
  record = cursor.fetchone()
  connection.close()
  print ("Название школы", record[1])


get_schholname(2)
