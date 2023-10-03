from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer)
    email = Column(String, unique=True)
    password = Column(String)
    city = Column(String)
    role = Column(String)

    courses = relationship('Course', back_populates='teacher')
    grades = relationship('Grade', back_populates='student')


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('users.id'))

    teacher = relationship('User', back_populates='courses')
    assignments = relationship('Assignment', back_populates='course')


class Assignment(Base):
    __tablename__ = 'assignments'

    id = Column(Integer, autoincrement=True, primary_key=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    description = Column(String)
    deadline = Column(String)

    course = relationship('Course', back_populates='assignments')
    grade = relationship('Grade', back_populates='assignment')


class Grade(Base):
    __tablename__ = 'grades'

    id = Column(Integer, autoincrement=True, primary_key=True)
    assignment_id = Column(Integer, ForeignKey('assignments.id'))
    student_id = Column(Integer, ForeignKey('users.id'))
    score = Column(Integer)

    student = relationship('User', back_populates='grades')
    assignment = relationship('Assignment', back_populates='grade')
