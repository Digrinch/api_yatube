from django.db.models import QuerySet
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from api.permissions import AllowOnlyAuthorizedUsers, AllowOnlyAuthorUser
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer
from posts.models import Group, Post


class PostViewSet(ModelViewSet):
    permission_classes = [AllowOnlyAuthorUser, AllowOnlyAuthorizedUsers]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer: ModelSerializer) -> None:
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(ModelViewSet):
    permission_classes = [AllowOnlyAuthorUser, AllowOnlyAuthorizedUsers]

    serializer_class = CommentSerializer

    def get_queryset(self) -> QuerySet:
        return Post.objects.get(pk=self.kwargs.get('post_id')).comments

    def perform_create(self, serializer: ModelSerializer) -> None:
        post = Post.objects.get(pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)
