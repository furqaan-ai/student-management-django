from django.shortcuts import render, redirect
from ..models import Student, School
from ..forms.student_forms import StudentForm
from django.contrib import messages

# SHOW DATA (with search + filter)
def ShowData(request):
    query = request.GET.get('q')
    status = request.GET.get('status')

    StudentData = Student.objects.all()

    if query:
        StudentData = StudentData.filter(name__icontains=query)

    if status == "active":
        StudentData = StudentData.filter(is_active=True)
    elif status == "inactive":
        StudentData = StudentData.filter(is_active=False)

    return render(request, "students/ShowData.html", {'Data': StudentData})


# ADD DATA
def AddData(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            school = form.cleaned_data['school']
            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            is_active = form.cleaned_data["is_active"]

            Student.objects.create(
                school=school,
                name=name,
                age=age,
                is_active=is_active
            )

            messages.success(request, "Student added successfully")
            return redirect("show_data")
    else:
        form = StudentForm()

    return render(request, 'students/form.html', {"form": form})


# DELETE DATA
def DeleteData(request, id):
    if request.method == "POST":
        student = Student.objects.get(id=id)
        student.delete()
        messages.success(request, "Student deleted successfully")
    return redirect('show_data')


# UPDATE DATA
def UpdateData(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.is_active = request.POST.get('is_active') is not None
        student.save()

        messages.success(request, "Student updated successfully")
        return redirect('show_data')

    return render(request, 'students/UpdateData.html', {'Data': student})


# HOME PAGE
def GoTo(request):
    return render(request, 'students/goto.html')


# SCHOOL FILTER
def StudentsBySchool(request, id=1):
    if request.method == 'GET' and id:
        data = Student.objects.filter(school_id=id)
        return render(request, "students/ShowData.html", {"Data": data})
    else:
        schools = School.objects.all()
        return render(request, "students/ShowSchool.html", {"school": schools})