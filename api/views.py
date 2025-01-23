from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Author
from api.serializers import AuthorSerializer


@api_view(['POST', 'GET'])
def list_authors(request):

    if request.method == 'POST':
        # get data from request
        data = request.data
        # serialize data
        serializer = AuthorSerializer(data=data)
        # check if data is valid
        if serializer.is_valid():
            # save data
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    else:
        # get authors from db
        authors = Author.objects.all()
        # serialize authors
        serializer = AuthorSerializer(authors, many=True)
        # print(serializer.data)
        return Response(serializer.data)


class AuthorList(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AuthorModelViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer