# greeting/views.py

from django.http import HttpResponse
from django.shortcuts import render

def hello_view(request):
    name = request.GET.get("name")
    message = request.GET.get("message")

    # оба параметра переданы и совпадают?
    if name == "Recruto" and message == "Давай дружить":
        return HttpResponse(f"Hello {name}! {message}", content_type="text/plain; charset=utf-8")

    # иначе показываем форму
    return render(request, "greeting/form.html")
