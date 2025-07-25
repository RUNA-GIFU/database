# backend/api/hello_db/movies/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
import json

from api.hello_db.models import Hello  # Helloモデルが存在する前提

# 確認用の簡単なエンドポイント
def backend(request):
    data = {'message': 'Hello from Django backend!'}
    return JsonResponse(data)

# フロントエンドからの POST を受け取るAPI
@csrf_exempt
def movies(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            return JsonResponse({'received': data})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'POST only'}, status=405)

# DBから1件だけ取得する確認用API
class Db(APIView):
    def get(self, request, format=None):
        try:
            entry = Hello.objects.get(id=1)  # id=1 のデータを取得
            return Response({"message": entry.world})
        except Hello.DoesNotExist:
            return Response({"error": "Hello object not found"}, status=404)
