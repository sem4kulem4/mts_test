from django.urls import path, include

app_name = 'api'

urlpatterns = [
   path('', include('main_app.urls', namespace='main_app')),
]