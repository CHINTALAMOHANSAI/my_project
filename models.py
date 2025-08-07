from __init__ import db

class Student(db.Model):
    __tablename__="Students"
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100),nullable=False)
    student_age=db.Column(db.Integer)
    student_marks=db.Column(db.Integer)

    def __repr__(self):
        return f"<Student {self.student_name}>"
    
    def to_dict(self):
        return {
            "id":self.student_id,
            "name":self.student_name,
            "age":self.student_age,
            "marks":self.student_marks
        }


class Student(db.Model):
    __tablename__="demo"
    student_id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(100),nullable=False)
    student_age=db.Column(db.Integer)
    student_marks=db.Column(db.Integer)

    def __repr__(self):
        return f"<Student {self.student_name}>"
    
    def to_dict(self):
        return {
            "id":self.student_id,
            "name":self.student_name,
            "age":self.student_age,
            "marks":self.student_marks
        }

