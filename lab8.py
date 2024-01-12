from flask import Blueprint, render_template, request, jsonify
from flask import abort
import datetime
lab8=Blueprint('lab8', __name__)

@lab8.route('/lab8/')
def main():
    return render_template('lab8/index.html')

courses=[
    {"name": "C++", "videos": 3, "price": 3000, "date_": "2023-12-19"},
    {"name": "basic", "videos": 30, "price": 0, "date_": "2023-12-21"},
    {"name": "C#", "videos": 8, "date_": "2023-12-21"}
]

@lab8.route('/lab8/api/courses/', methods=['GET'])
def get_courses():
    return jsonify (courses)

@lab8.route('/lab8/api/courses/<int:course_num>', methods=['GET'])
def get_courses2(course_num):
    
    if 0<= course_num< len(courses)-1:
        return courses[course_num]
    else:
        return abort(404)
    
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['DELETE'])
def get_courses3(course_num):

     if 0<= course_num <len(courses)-1:
        del courses [course_num]
        return '', 204
     else:
         return abort(404)
     
@lab8.route('/lab8/api/courses/<int:course_num>', methods=['PUT'])
def put_courses3(course_num):
    course=request.get_json()
    courses[course_num]=course
    
    if 0<= course_num <len(courses)-1:
        return courses[course_num] 
    else:
        return abort(404)