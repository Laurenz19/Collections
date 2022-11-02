"""FGS_collection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500


from pages.views import *
from myCollection.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', registerPage, name="register"),
    path('', loginPage, name="login"),
    path('login/', loginPage, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('home/', homePage, name="home"),  
   
    path('collection_add/', new_Collection, name="new_collection"),
    path('collection/update/<int:id>/', update_Collection, name="update_collection"),
    path('collection/<int:id>/', details_Collection, name="details_collection"),
    path('collection/delete/<int:id>/', delete_Collection, name="delete_collection"),
    path('collection/', get_AllCollections, name="collections"),
    path('collection/film', get_AllFilm, name="film"),
    path('collection/game', get_AllGame, name="game"),
    path('collection/serie', get_AllSerie, name="serie"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'pages.views.error_404'
