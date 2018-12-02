from django.contrib import admin
from django.urls import path

# ray test added
from notifier.views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),  # ray test added
    path('admin/', admin.site.urls),
]
