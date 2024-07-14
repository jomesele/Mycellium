from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import os
import json

@csrf_exempt
def upload(request):
    data = json.loads(request.body)
    image_data = data['image']
    image_data = base64.b64decode(image_data.split(',')[1])
    
    with open(os.path.join('path/to/save/image', 'image.png'), 'wb') as f:
        f.write(image_data)
    
    return JsonResponse({"status": "ok"})