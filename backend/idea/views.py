from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from idea.models import Idea
from idea.serializers import IdeaSerializer

@csrf_exempt
def get_ideas(request):
    if request.method == 'GET':
        idea = Idea.objects.all()
        serializer = IdeaSerializer(idea, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = IdeaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def idea_detail(request, pk):
    try:
        idea = Idea.objects.get(pk=pk)
    except Idea.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = IdeaSerializer(idea)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = IdeaSerializer(idea, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        idea.delete()
        return HttpResponse(status=204)