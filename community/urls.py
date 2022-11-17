from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list),
    path('reviews/<int:review_pk>/', views.review_detail),
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('reviews/<int:review_pk>/comments/', views.comment_create),
    path('<int:review_pk>/likes/', views.likes, name='likes'),

    # swagger settings
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui')
]
