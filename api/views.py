from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from datetime import datetime
from .serialiazers import StoriesSerializer
from .models import Stories

# Create your views here.

@api_view(['GET'])
def get_routes(request):
    context = {
        "/api/v1/": "All Routes",
        "/api/v1/stories": "All Stories",
        "/api/v1/auth/users/": "Register User",
        "/api/v1/auth/users/me": "Current User",
        "/api/v1/auth/token/login": "LogIn User",
        "/api/v1/auth/token/logout": "LogOut User",
    }
    return Response(context, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted_view(request, *args, **kwargs):
    return Response(data='Only for logged in users', status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([AllowAny])
def all_stories(request, *args, **kwargs):
    stories = Stories.objects.all()
    serializer = StoriesSerializer(stories, many=True)
    print(serializer.data)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def create_story(request):
    story = request.data
    author = request.user
    serializer = StoriesSerializer(data=story, many=False)
    if serializer.is_valid():
        serializer.save(author=author)
        print(serializer.data)
        return Response({
            'status': True, 
            'message': 'success'
        }, status=status.HTTP_201_CREATED)
    else:
        return Response({
            'status': False, 
            'message': 'failed'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def test(request):
    date = datetime.now()
    print(date)
    return Response(
        {
            "working": True,
            "date": date
        }
    )


