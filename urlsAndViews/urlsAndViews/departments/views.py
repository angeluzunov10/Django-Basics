from django.http import HttpResponse
from django.shortcuts import render, redirect

from urlsAndViews.departments.models import Department


# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")


def view_with_name(request, variable):
    # return HttpResponse(f"<h1>Variable: {variable}</h1>")
    return render(request,  'departments/name_template.html', {"variable": variable})


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args} Kwargs: {kwargs}</h1>")


def view_with_integer(request, pk):
    return HttpResponse(f"<h1>Int pk with pk: {pk}</h1>")


def view_with_slug(request, pk, slug):
    department = Department.objects.get(pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>The year is: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_to_view(request):
    return redirect('http://localhost:8000')