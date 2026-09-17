import psycopg2

## Bu değeri localinde çalışırken kendi passwordün yap. Ama kodu pushlarken 'postgres' olarak bırak.
password = 'postgres'

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password=password)
    return conn

# DATE_TRUNC ile ay bazlı kayıt sayılarını listele
def question_1_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select DATE_TRUNC('month', e.enrollment_date), count(e.student_id)
                        from enrollments as e
                        GROUP BY DATE_TRUNC('month', e.enrollment_date)
                        ORDER by DATE_TRUNC('month', e.enrollment_date)''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# DATE_PART ile sadece kayıtların yıl bilgisini al
def question_2_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select date_part('year', e.enrollment_date) as "year"
                        from enrollments as e
                        ORDER by DATE_TRUNC('month', e.enrollment_date);
                    ''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Tüm öğrencilerin yaşlarının toplamını dönen bir sql sorgusu yaz.
def question_3_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select Sum(s.age) as "SUM"
                        from students as s;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Tüm kurs sayısını bul
def question_4_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select Count(c.course_id) as "total_course"
                        from courses as c;
                    ''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Yaşı ortalama yaştan büyük olan öğrencileri getir
def question_5_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select*
                        from students as s
                        WHERE s.age > (
	                            Select AVG(s.age)
	                            from students as s)
                        ORDER BY s.student_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kursun en eski kayıt tarihini bul
def question_6_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select c.course_id, min(e.enrollment_date) as "first_enrollment"
                        from courses as c
                        JOIN enrollments as e
                        ON e.course_id = c.course_id
                        GROUP by c.course_id
                        ORDER BY c.course_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# Her kurs için öğrencilerin ortalama yaşlarını bulun. 
# Sorgu course_name ve ortalama yaş(avg_age) değerlerini dönmelidir.
def question_7_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select c.course_name, Avg(s.age) as "avg_age"
                        from courses as c
                        JOIN enrollments as e
                        ON e.course_id = c.course_id
                        JOIN students as s
                        ON s.student_id = e.student_id
                        GROUP by c.course_id
                        ORDER BY c.course_id;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


# En genç öğrencinin yaşını getiren sorguyu yazınız.
def question_8_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute('''select Min(s.age) as "MIN"
                        from students as s;''')
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

# Her derse kayıt olmuş öğrenci sayısını bulunuz.
def question_9_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select c.course_name, Count(s.student_id) as "student_count"
                        from courses as c
                        JOIN enrollments as e
                        ON e.course_id = c.course_id
                        JOIN students as s
                        ON s.student_id = e.student_id
                        GROUP by c.course_id
                        ORDER BY c.course_id;""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#Tüm kayıt olunmuş derslerin sadece isimlerini getirinz.
def question_10_query():
    connection = connect_db()
    cursor = connection.cursor()
    cursor.execute("""select c.course_name
                        from courses as c
                        JOIN enrollments as e
                        ON e.course_id = c.course_id
                        GROUP by c.course_name
                        ORDER BY c.course_name;""")
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
