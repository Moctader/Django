from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# Create your views here.
def contact(request):
    return render(request, './first_app/index.html', {"name": "I am Rahim", "marks":86, "courses": [
        
        {
            'id':1,
            'course':'C',
            'Teacher':'Rahim'
        },
        {
            'id':2,
            'course':'C++',
            'Teacher':'kahim'
        },
        {
            'id':3,
            'course':'C',
            'Teacher':'Mahim'
        }
    ]})
    
