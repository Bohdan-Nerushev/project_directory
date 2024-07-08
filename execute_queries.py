import sqlite3

# Підключення до бази даних
conn = sqlite3.connect('university.db')
cursor = conn.cursor()

# Визначення змінних, які будуть використовуватись у запитах
subject_id = 1  # Вкажіть відповідний ID предмета для запиту 2
group_id = 1    # Вкажіть відповідний ID групи для запиту 6 та 7
teacher_id = 1  # Вкажіть відповідний ID викладача для запиту 5 та 8
student_id = 1  # Вкажіть відповідний ID студента для запиту 9 та 10

# Перелік запитів з відповідними параметрами
queries = [
    ("query_1.sql", ()),
    ("query_2.sql", (subject_id,)),
    ("query_3.sql", (subject_id,)),
    ("query_4.sql", ()),
    ("query_5.sql", (teacher_id,)),
    ("query_6.sql", (group_id,)),
    ("query_7.sql", (group_id, subject_id)),
    ("query_8.sql", (teacher_id,)),
    ("query_9.sql", (student_id,)),
    ("query_10.sql", (student_id, teacher_id)),
    ("query_11.sql", (student_id, teacher_id)),
    ("query_12.sql", (group_id, subject_id)),
]

# Виконання кожного запиту та вивід результатів
for query_file, params in queries:
    try:
        with open(query_file, 'r') as file:
            sql_query = file.read()
        cursor.execute(sql_query, params)
        results = cursor.fetchall()
        print(f"Results for {query_file}:\n\n {results}\n\n============")
        
    except FileNotFoundError:
        print(f"File {query_file} not found. Skipping.")
    except Exception as e:
        print(f"An error occurred while executing {query_file}: {e}")

# Закриття з'єднання з базою даних
conn.close()
