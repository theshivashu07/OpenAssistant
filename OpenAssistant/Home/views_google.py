import json
import requests
from django.http import JsonResponse
from django.contrib.auth import login
from django.contrib.auth.models import User
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests

GOOGLE_CLIENT_ID = "608674038178-m2afsu45qt7le6vvejra469bhvq40a1l.apps.googleusercontent.com"  # Replace with your actual Client ID

def google_login(request):
    if request.method == "POST":
        data = json.loads(request.body)
        token = data.get("token")

        try:
            # Verify the token with Google
            idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), GOOGLE_CLIENT_ID)
            email = idinfo["email"]
            name = idinfo.get("name", "")

            # Check if user exists, if not, create one
            user, created = User.objects.get_or_create(username=email, defaults={"email": email, "first_name": name})

            # Log the user in
            login(request, user)

            return JsonResponse({"success": True, "new_user": created})  # Send if the user is new

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})

    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
