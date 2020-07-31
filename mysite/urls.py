"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from polls import views
# http://localhost:8000/admin => 관리자페이지
# http://localhost:8000/polls => 모든 투표질문을 화면에 출력
#                   ->URL 들어왔을때 처리할 view의 메서드가 여기서 명시



# URL패턴을 명시할때는 순서도 중요해
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
]
