from django import template
from django.template.loader import get_template

register=template.Library()

def my_template(value, arg):
    if arg=='change':
        value="Rahim"
        return value
    if arg == 'title':
        return value.title()
    

def show_courses():
    courses= [
        
        {
            "id":1,
            "name":"C",
            "Teacher":"Rahim"
        },
        {
            "id":2,
            "name":"C++",
            "Teacher":"kahim"
        },
        {
            "id":3,
            "name":"C",
            "Teacher":"Mahim"
        },
    ]
    return {'courses': courses}

courses_template=get_template('first_app/courses.html')
register.filter('change_name', my_template)
register.inclusion_tag(courses_template)(show_courses)