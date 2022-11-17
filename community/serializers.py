from rest_framework import serializers
from .models import Review, Comment


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'title',
            'content',
        )


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review', 'user',)  # 유효성 검사에서 빼서 읽기전용필드로 만들기


class ReviewSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('review', 'user',)
