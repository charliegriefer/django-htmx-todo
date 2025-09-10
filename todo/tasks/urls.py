from django.urls import path

from . import views

# "edit_task" is used via HTMX to display and submit the inline edit form

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("form/", views.task_form, name="task_form"),
    path("add/", views.add_task, name="add_task"),
    path("<int:pk>/toggle/", views.toggle_task, name="toggle_task"),
    path("<int:pk>/edit/", views.edit_task, name="edit_task"),
    path("<int:pk>/row/", views.get_task_row, name="get_task_row"),
    path("messages/", views.messages_view, name="messages"),
    path("messages/dismiss/", views.dismiss_message, name="dismiss_message"),
]
