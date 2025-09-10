from django.contrib import messages
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task
from .services import (
    create_task_from_form,
    toggle_task_completion,
    update_task_from_form,
)


def task_list(request):
    tasks = Task.objects.order_by("-created_at")
    form = TaskForm()
    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": tasks,
            "form": form,
        },
    )


def task_form(request):
    form = TaskForm()
    html = render_to_string(
        "tasks/_task_form.html",
        {
            "form": form,
            "form_action": "/tasks/add/",
            "button_label": "Add",
        },
        request=request,
    )
    return HttpResponse(html)


@require_POST
def add_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = create_task_from_form(form)
        messages.success(request, "Task added successfully.")
        html = render_to_string("tasks/_task_row.html", {"task": task}, request=request)
        response = HttpResponse(html)
        # Add a header to trigger an HTMX request to update the messages
        response['HX-Trigger'] = 'messagesChanged'
        return response
    else:
        html = render_to_string(
            "tasks/_task_form.html",
            {
                "form": form,
                "form_action": "/tasks/add/",
                "button_label": "Add",
            },
            request=request,
        )
        return HttpResponseBadRequest(html)


@require_POST
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task = toggle_task_completion(task)
    html = render_to_string("tasks/_task_row.html", {"task": task}, request=request)
    return HttpResponse(html)


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task = update_task_from_form(form)
            html = render_to_string(
                "tasks/_task_row.html", {"task": task}, request=request
            )
            return HttpResponse(html)
        else:
            html = render_to_string(
                "tasks/_task_form.html",
                {
                    "form": form,
                    "form_action": f"/tasks/{task.pk}/edit/",
                    "button_label": "Save",
                },
                request=request,
            )
            return HttpResponseBadRequest(html)

    else:  # GET request to show the edit form
        form = TaskForm(instance=task)
        html = render_to_string(
            "tasks/_task_form.html",
            {
                "form": form,
                "form_action": f"/tasks/{task.pk}/edit/",
                "button_label": "Save",
            },
            request=request,
        )
        return HttpResponse(html)


def messages_view(request):
    """Return rendered messages."""
    return render(request, 'tasks/_messages.html')


def dismiss_message(request):
    """Handle HTMX request to dismiss a message."""
    return HttpResponse("")  # Return empty response to remove the message
