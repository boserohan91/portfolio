import sqlalchemy
from sqlalchemy.sql.functions import OrderedSetAgg
from sqlalchemy.sql.schema import ForeignKey
from .database import Base
from sqlalchemy import Column, Integer, Float ,String, Unicode, Date
from sqlalchemy.orm import relationship

class BasicDetails(Base):
    __tablename__ = "basic_details"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    address = Column(String)
    telephone = Column(Unicode(20))
    email = Column(String)
    gender = Column(Unicode(6))
    dob = Column(Date)
    nationality = Column(String)

    education = relationship("Education", back_populates="basicdetails")
    work = relationship("Work", back_populates="basicdetails")
    certifications = relationship("Certifications", back_populates="basicdetails")
    skills = relationship("Skills", back_populates="basicdetails")

class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, autoincrement=True)
    period_from = Column(Date)
    period_to = Column(Date)
    degree = Column(String)
    institute = Column(String)
    university = Column(String)
    marks = Column(Float)
    max_marks =  Column(Float)

    basicdetails_id = Column(Integer, ForeignKey("basic_details.id"))

    basicdetails = relationship("BasicDetails", back_populates="education")

class Work(Base):
    __tablename__ = "work"

    id = Column(Integer, primary_key=True, autoincrement=True)
    period_from = Column(Date)
    period_to = Column(Date)
    organisation = Column(String)
    role = Column(String)
    description = Column(String)

    basicdetails_id = Column(Integer, ForeignKey("basic_details.id"))

    basicdetails = relationship("BasicDetails", back_populates="work")

class Certifications(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    provider = Column(String)
    marks = Column(Float)
    max_marks = Column(Float)

    basicdetails_id = Column(Integer, ForeignKey("basic_details.id"))

    basicdetails = relationship("BasicDetails", back_populates="certifications")


class Skills(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    basicdetails_id = Column(Integer, ForeignKey("basic_details.id"))

    basicdetails = relationship("BasicDetails", back_populates="skills")

