from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer


@api_view(["POST"])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_all_todos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_todo_by_id(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response({"message": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo)
    return Response(serializer.data)


@api_view(["PUT"])
def update_todo_by_id(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response({"message": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_todo_by_id(request, todo_id):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except Todo.DoesNotExist:
        return Response({"message": "Todo not found"}, status=status.HTTP_404_NOT_FOUND)

    todo.delete()
    return Response(
        {"message": "Todo deleted successfully"}, status=status.HTTP_204_NO_CONTENT
    )
