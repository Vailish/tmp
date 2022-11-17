from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_pk>/comments/', views.comment_create),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
