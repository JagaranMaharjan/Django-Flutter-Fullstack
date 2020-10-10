from django.contrib import messages
from django.shortcuts import render
from .models import Todo
from .forms import ToDoForm


# Create your views here.
# display all data
def display_to_do_data(request):
    show_all = Todo.objects.all()
    return render(request, 'APIDemo/index.html', {"data": show_all})


# insert new things to do
def insert_to_do(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('description'):
            save_record = Todo()
            save_record.title = request.POST.get('title')
            save_record.description = request.POST.get('description')
            save_record.save()
            messages.success(request, 'To Do Data Added Successfully !!!')
            return render(request, 'APIDemo/insert.html')
        else:
            messages.success(request, 'Text Fields Are Empty !!!')
            return render(request, 'APIDemo/insert.html')
    else:
        return render(request, 'APIDemo/insert.html')


# this function allows us to edit to do data according to to_do id
def edit_to_do_data(request, id):
    edit_to_do_obj = Todo.objects.get(id=id)
    return render(request, 'APIDemo/edit.html', {"ToDoModel": edit_to_do_obj})


# this function allows us to update the to do data according to to_do id
def update_to_do_data(request, id):
    update_to_do_obj = Todo.objects.get(id=id)
    form = ToDoForm(request.POST, instance=update_to_do_obj)
    if form.is_valid():
        form.save()
        messages.success(request, "Record Updated Successfully.. !")
        return render(request, 'APIDemo/edit.html', {"ToDoModel": update_to_do_obj})


# this function remove to do from local database according to to_do id
def delete_to_do_data(request, id):
    delete_to_do_obj = Todo.objects.get(id=id)
    delete_to_do_obj.delete()
    show_all = Todo.objects.all()
    return render(request, 'APIDemo/index.html', {"data": show_all})
