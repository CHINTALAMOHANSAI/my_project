from flask import Blueprint, request, jsonify,render_template
from models import Student
from __init__ import db

main = Blueprint('main', __name__)

@main.route('/')
def htm():
    return render_template("index.html")


@main.route('/add_student', methods=['POST'])
def create_user():
    data = request.get_json()
    new_student = Student(student_name=data["name"],student_age=data["age"],student_marks=data["marks"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

@main.route('/add_students', methods=['POST'])
def create_users():
    datas = request.get_json()
    new_students = [Student(student_name=data["name"],student_age=data["age"],student_marks=data["marks"]) for data in datas]
    db.session.add_all(new_students)
    db.session.commit()
    return jsonify([new_student.to_dict() for new_student in new_students]), 201

@main.route('/students', methods=['GET'])
def get_users():
    students = Student.query.all()
    return jsonify([i.to_dict() for i in students]),200 


@main.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = db.session.get(Student, id)
    if student:
        db.session.delete(student)
        db.session.commit()
        return jsonify({"message": "Student deleted"}), 200
    else:
        return jsonify({"error": "Student not found"}), 404


# @main.route("/remove",methods=["DELETE"])
# def remove_student():
#     data=request.json.get("id")
#     student=db.session.get(Student,data)
#     if(student):
#         db.session.delete(student)
#         db.session.commit()
#         # return "successfully deleted"
#         return jsonify({"message": "Student deleted"}), 200
#     else:
#         return jsonify({"error": "Student not found"}), 404




@main.route("/get_student",methods=['GET'])
def get_student():
    data=request.json.get("marks")
    # student=db.session.get(Student,data)
    students=Student.query.filter((Student.student_marks<data) & (Student.student_age>22)).all()
    print(students)
    if(students):
        return jsonify([student.to_dict() for student in students])
    return "incorrect student id"


@main.route("/change",methods=["PUT"])
def change():
    data=request.json.get("name")
    student=Student.query.filter(Student.student_marks<850).all()
    # print(student)
    if(student):
        for i in student:
            i.student_marks=1000
            i.student_name="user"
        db.session.commit()
        return "successfully update",201
    return "error occured"



@main.route('/delete_table', methods=['DELETE'])
def delete_student_table():
    try:
        Student.__table__.drop(db.engine) 
        return jsonify({"message": "Student table deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500