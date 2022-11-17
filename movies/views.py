from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import MovieListSerializer, MovieSerializer, CommentSerializer
from .models import Movie, Comment


@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movie = get_list_or_404(Movie)
        serializer = MovieListSerializer(movie, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)  # get특성상 중간에 퍼지면 404가 아니라 500을 줌, 끝까지 못가기 때문 -> get_object_oir_404 이런식으로해결가능
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)  # POST와 차이
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comment = get_list_or_404(Comment)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    # comment = Comment.objects.get(pk=comment_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)  # POST와 차이
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, movie_pk):
    # movie = Movie.objects.get(pk=movie_pk)
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)  # request.POST 말고
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie)  # commit=False말고 이렇게
        return Response(serializer.data, status=status.HTTP_201_CREATED)
