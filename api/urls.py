from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

router = DefaultRouter()
router.register("",views.UserViewSet)

urlpatterns = [
    path('swagger/',schema_view),
    path('tasks/', views.task_list),
    path('tasks/<int:pk>/', views.task_detail),
]
urlpatterns += router.urls