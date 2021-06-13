from django.shortcuts import render
from rest_framework.views import APIView
from apps.user.models import User
from apps.user.serializers import UserSerializer
from django.http import JsonResponse
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserAPI(APIView):
    serializer = UserSerializer

    def get(self, request, format=None):
        list = User.objects.all()
        response = self.serializer(list, many=True)
        return JsonResponse(response.data, status=200, safe=False)

    def post(self, request, format=None):
        print(request.data)
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAPIDetail(APIView):
    serializer = UserSerializer

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = self.serializer(user, data=request.data);
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
