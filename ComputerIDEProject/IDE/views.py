import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.views.decorators.http import require_POST
from .models import Submission


def landing(request):
    return render(request, "IDE/landing.html")


@ensure_csrf_cookie
def index(request):
    return render(request, "IDE/index.html")


@require_POST
def submit_code(request):
    try:
        data = json.loads(request.body)
        name = data.get("name", "").strip()
        code = data.get("code", "").strip()

        if not name:
            return JsonResponse({"status": "error", "message": "Please enter your name."}, status=400)
        if not code:
            return JsonResponse({"status": "error", "message": "Please write some code first."}, status=400)

        _, created = Submission.objects.update_or_create(
            name=name,
            defaults={"code": code},
        )

        action = "submitted" if created else "updated"
        return JsonResponse({"status": "ok", "message": f"Code {action} successfully!"})

    except Exception:
        return JsonResponse({"status": "error", "message": "Something went wrong."}, status=500)
