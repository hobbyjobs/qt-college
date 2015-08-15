# Introduction #

The Database Model is on the first draft.

User:
userID Integer (One2Many studentID, One2Many staffID, One2Many instructorID)
name Char
familyName Char
email Char
address Char
username Char
password Char
date Date
description Text



Student:
studentID Integer (Many2Many classID)
userID Integer (Many2One)


Staff:
staffID Integer
userID Integer (Many2One)
position Char
departmentID


Instructor:
instructorID Integer (One2Many classID)
userID Integer (Many2One)



Class:
classID Integer (Many2Many studentID, Many2Many enrollID)
moduleID Integer (One2One)
intakeID Integer (One2One)
instructorID Integer (Many2One)
calssDescription Text

Class\_Enroll:
classID Integer (One2Many)
enrollID Integer (One2Many)

Student\_Class:
studentID Integer (One2Many)
classID Integer (One2Many)

Enroll:
enrollID Integer (Many2Many classID)
enrollDate Date
status Char

Schedule:
scheduleID Integer
classID Integer (Many2One)
scheduleDate Date
duration Time

Exam:
examID Integer (One2Many markID)
classID Integer
examTypeID Integer (Many2One)
examDate Date

ExamType:
examTypeID Integer (One2Many examID)
examTypeName Char
weightage Integer

Assignment:
assignmentID Integer (One2Many markID)
classID Integer
assignementTitle Char
submissionDate Date
weightage Integer


Mark:
markID Integer
studentID Integer (Many2One)
assignmentID Integer
examID Integer
assignmentMark Integer
examMark Integer

Intake:
intakeID Integer
intakeDate Integer

Module:
moduleID Integer (One2Many classID)
moduleTitle Char
creditHours Integer
moduleDescription Text

Department:
departmentID Integer (One2Many classID)
description Text

Course:
courseID Integer
departmentID Integer
courseTitle Char
courseDescription Text

# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages