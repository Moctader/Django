from django.shortcuts import render

# Create your views here.
# def home (request):
#     return request(request, './first_app/home.html')
def about(request):
    return render(request, './first_app/about.html',{'author':'glenn maxwell'})

def home(request):
    return render(request, './first_app/home.html', {'courses': [
        
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
