# greeting/views.py

from django.http import HttpResponse, HttpResponseBadRequest

def hello_view(request):
    name = request.GET.get("name")
    message = request.GET.get("message")

    # Если кто-то совсем забыл параметры — можно выдать 400 Bad Request
    if not name or not message:
        return HttpResponseBadRequest("Missing parameters: ?name=…&message=…")

    # Просто подставляем то, что пришло из GET
    return HttpResponse(f"Hello {name}! {message}!", content_type="text/plain; charset=utf-8")
