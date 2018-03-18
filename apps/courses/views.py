from django.shortcuts import render, redirect
from models import Course, Description
from django.contrib import messages
# Create your views here.
def index(request):
    # courses = Course.objects.all()
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def create(request):
    if request.method != "POST":
        return redirect('/courses')
        
    # Validation for creating new course
    errors = Course.objects.create_validator(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/courses')

    # Assign the saved course to newcourse
    newcourse = Course.objects.create(name = request.POST['course'])
    # Save description that belongs to newcourse - one to one relationship
    Description.objects.create(course = newcourse, description = request.POST['description'])

    # redirect to the display route
    return redirect('/courses')

def delete_confirm(request, id):
    if request.method != "POST":
        return render(request, "courses/confirm.html", { "course": Course.objects.get(id=id) })
    else:
        Course.objects.get(id=id).delete()
        return redirect("/courses")
