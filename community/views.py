from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from django.http import JsonResponse
from .serializers import ReviewListSerializer, ReviewSerializer, CommentSerializer
from .models import Review, Comment


@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        review = get_list_or_404(Review)
        serializer = ReviewListSerializer(review, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print('ㅇㅅㅇ')
            print(serializer)
            print('ㅇㅁㅇ')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    # review = Review.objects.get(pk=review_pk)  # get특성상 중간에 퍼지면 404가 아니라 500을 줌, 끝까지 못가기 때문 -> get_object_oir_404 이런식으로해결가능
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)  # POST와 차이
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
def comment_create(request, review_pk):
    # review = Review.objects.get(pk=review_pk)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = CommentSerializer(data=request.data)  # request.POST 말고
    print('ㅇㅅㅇ')
    print(serializer)
    print('ㅇㅁㅇ')
    if serializer.is_valid(raise_exception=True):
        print('ㅁㅇㅁ')
        serializer.save(review=review)  # commit=False말고 이렇게
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def likes(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Comment, pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
            is_liked = False
        else:
            review.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    context = {}
    return JsonResponse(context)