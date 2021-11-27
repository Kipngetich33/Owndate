from blog.models import Post,Category,Comment
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

# ViewSets define the view behavior.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer