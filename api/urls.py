from django.urls import path
from .views import (
    create_todo,
    get_all_todos,
    get_todo_by_id,
    update_todo_by_id,
    delete_todo_by_id,
)

urlpatterns = [
    path("api/todo/", get_all_todos, name="get_all_todos"),
    path("api/todo/create/", create_todo, name="create_todo"),
    path("api/todo/<int:todo_id>/", get_todo_by_id, name="get_todo_by_id"),
    path("api/todo/update/<int:todo_id>/", update_todo_by_id, name="update_todo_by_id"),
    path("api/todo/delete/<int:todo_id>/", delete_todo_by_id, name="delete_todo_by_id"),
]
