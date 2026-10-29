import pandas as pd
from mydb import db
df=pd.read_csv("kaggledata.csv")




##print(df.head())
#print(df.info())
#print(df.describe())


#print(df.isnull().sum())



##Based on this ouput, We are going to remove previous_gpa, attendance_percentage, note_quality, sleep_quality, device_availabilty, and time_management_score 
##because we find them to be to subjective or not important to our big thesis question that we want to figure out.

df = df.drop(columns=['previous_gpa', 'notes_quality', 'sleep_quality', 'device_availability', 'time_management_score'])

##Our group is also deciding to drop education_level, age, sleep_quality, motivation_level, educational_app_usage, questions_correct, questions_attempted, online_course_hours, exam_anxiety_level, time_management_score, break_frequency, previous_gpa, 
##We want to keep parent_education because we need this as a statistic for our conclusions. We are going to drop these null values so we do not skew the data

df= df.drop(columns=['education_level', 'age', 'study_environment', 'motivation_level','private_tuition', 'educational_app_usage', 'questions_correct','stress_level', 'questions_attempted', 'online_course_hours', 'exam_anxiety_level', 'break_frequency', 'class_participation', "exam_difficulty", 'performance_level'])
##We decided to drop these columns because either they are too arbitrary for someone to fill out in a form themselves, or we found contradictions in our data (21 year old in high school, 14 year old in college)

df=df.dropna()

print(df.head())
print(df.info())
#print(df.describe())
#print(df.isnull().sum())

##We want to keep parent_education and attendance_percentage because we need this as a statistic for our conclusions. We are going to drop these null values so we do not skew the data. We deleted about 15% of our data by dropping NAs and keep about 84,000 rows in 23 columns
# for index, row in df.iterrows():
#     columns = [row['student_id'], row['gender']]
#     #print(columns)
#     query = """INSERT INTO STUDENT (student_id, gender) VALUES(%s,%s)"""
#     column_info, data, insert_id, error, warnings = db.query(query, columns)
#     print([column_info, data, insert_id, error, warnings])

# for index, row in df.iterrows():
#     columns = [row['student_id'], row['school_type'], row["family_income"],row["parent_education"], row["urban_rural"], row["internet_access"]]
#     #print(columns)
#     query = """INSERT INTO UNCONTROLLABLES (student_id, school_type, family_income, parent_education, urban_rural, internet_access) VALUES(%s,%s,%s,%s,%s,%s)"""
#     column_info, data, insert_id, error, warnings = db.query(query, columns)
#     print([column_info, data, insert_id, error, warnings])

for index, row in df.iterrows():
    columns = [row['student_id'], row['attendance_percentage'], row['assignment_completion_rate'], row['study_hours_per_day'], row['self_study_hours'], row['online_learning_hours'], row['revision_frequency'], row['practice_tests_completed'], row['sleep_hours'], row['daily_screen_time'], row['physical_activity_hours']]
    #print(columns)
    query = """INSERT INTO CONTROLLABLES (student_id, attendance_percentage, assignment_completion_rate, study_hours_per_day, self_study_hours, online_learning_hours, revision_frequency, practice_tests_completed, sleep_hours, daily_screen_time, physical_activity_hours) VALUES(%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"""
    column_info, data, insert_id, error, warnings = db.query(query, columns) 
    print([column_info, data, insert_id, error, warnings])
    


for index, row in df.iterrows():
    columns = [row['student_id'], row['exam_score'], row['exam_preparation_days'], row['performance_grade'], row['pass_status']]
    #print(columns)
    query = """INSERT INTO PERFORMANCE (student_id, exam_preparation_days, exam_score, performance_grade, pass_status) VALUES(%s,%s, %s,%s,%s)"""
    column_info, data, insert_id, error, warnings = db.query(query, columns)

