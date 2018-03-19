from django.shortcuts import render, redirect
from models import Course, Description
from django.contrib import messages
from dateutil import tz
from datetime import datetime

# Create your views here.
def index(request):
    
    # METHOD 2: Auto-detect zones:
    from_zone = tz.tzutc()
    # to_zone = tz.tzlocal()
    to_zone = tz.gettz('US/Pacific')
    print "local tz===>", to_zone
    # Tell the datetime object that it's in UTC time zone since 
    # datetime objects are 'naive' by default
    utc = Course.objects.first().created_at
    print utc, "<-- UTC format"
    utc = utc.replace(tzinfo=from_zone)

    # Convert time zone
    central = utc.astimezone(to_zone)
    print central, "<== PST format"

    
    courses = Course.objects.all()
    
    #Convert from UTC to PST
    for i in range(0,len(courses)):
        utc = courses[i].created_at
        utc = utc.replace(tzinfo=from_zone)
        # it needs the string format, convert your datetime field to string field
        # if it's a datetime object djago template will render the format as the UTC
        courses[i].created_at = utc.astimezone(to_zone).strftime("%Y-%m-%d %H:%M:%S")
        print courses[i].created_at

    # courses = Course.objects.all()
    context2 = {
        'coursesssss': courses,
    }
  

    return render(request, 'courses/index.html', context2)

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
