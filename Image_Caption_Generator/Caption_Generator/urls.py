from django.urls import path
from Caption_Generator import views

urlpatterns = [
    path('home/', views.home,name='home'),
    path('Authenticate/', views.AuthenticatePage,name='Authenticate'),
    path('upload-image/', views.upload_image,name='upload_image'),
    path('get-endpoint/<str:image_name>', views.handle_get_request, name='get_endpoint'),
]
