from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_to_do_data, name='home'),
    path('insert', views.insert_to_do, name='insert_to_do'),
    path('edit/<int:id>', views.edit_to_do_data, name='edit_to_do'),
    path('update/<int:id>', views.update_to_do_data, name='update_to_do'),
    path('delete/<int:id>', views.delete_to_do_data, name='delete_to_do'),
]
