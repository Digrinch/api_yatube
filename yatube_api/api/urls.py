from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from api.apps import ApiConfig
from api.views import GroupViewSet, PostViewSet, comment_detail, comment_list

app_name = ApiConfig.name

router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    path('api/v1/posts/<int:post_id>/comments/', comment_list),
    path(
        'api/v1/posts/<int:post_id>/comments/<int:comment_id>/',
        comment_detail,
    ),
]
