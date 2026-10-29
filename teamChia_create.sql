DROP TABLE IF EXISTS STUDENT;
DROP TABLE IF EXISTS UNCONTROLLABLES;
DROP TABLE IF EXISTS CONTROLLABLES;
DROP TABLE IF EXISTS PERFORMANCE;

CREATE TABLE STUDENT (
    student_id VARCHAR(50),
    gender VARCHAR(50),
    CONSTRAINT PK_STUDENT PRIMARY KEY (student_id)
);



CREATE TABLE UNCONTROLLABLES (
    student_id VARCHAR(50),
    school_type VARCHAR(50),
    family_income VARCHAR(50),
    parent_education VARCHAR(50),
    urban_rural VARCHAR(50),
    internet_access BOOLEAN,
    CONSTRAINT PK_student_id PRIMARY KEY (student_id),
    CONSTRAINT FK_UNCONTROLLABLES_STUDENT FOREIGN KEY (student_id)
        REFERENCES STUDENT(student_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);



CREATE TABLE CONTROLLABLES (
    student_id VARCHAR(50),
    attendance_percentage FLOAT,
    assignment_completion_rate FLOAT,
    study_hours_per_day FLOAT,
    self_study_hours FLOAT,
    online_learning_hours FLOAT,
    revision_frequency VARCHAR(50),
    practice_tests_completed  INT,
    sleep_hours FLOAT,
    daily_screen_time FLOAT,
    physical_activity_hours FLOAT,
    CONSTRAINT PK_STUDENT PRIMARY KEY (student_id),
    CONSTRAINT FK_CONTROLLABLES_STUDENT FOREIGN KEY (student_id)
        REFERENCES STUDENT(student_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);




CREATE TABLE PERFORMANCE (
    student_id VARCHAR(50),
    exam_preparation_days INT,
    exam_score  INT,
    performance_grade VARCHAR(50),
    pass_status VARCHAR(50),
    CONSTRAINT PK_STUDENT PRIMARY KEY (student_id),
    CONSTRAINT FK_PERFORMANCE_STUDENT FOREIGN KEY (student_id)
        REFERENCES STUDENT(student_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

