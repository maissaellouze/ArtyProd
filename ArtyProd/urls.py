from django.urls import path,include
from django.conf.urls.static import static as statistics
from django.conf import settings
from django.contrib import admin, auth
from .views import send_email,writeblog,deposser,blog,mes_projets,tous_projets,liste_tache, demander_projet,equipe,CustomLoginView, index, RegisterPage ,index,service_detail,liste_membre,liste_projet
from django.contrib.auth.views import LogoutView


from .views import (
    HomeView,
)

urlpatterns = [
    path('',index.as_view(),name='index'),
    path('projet/', tous_projets, name='tous_projets'),
    path('service/<int:service_id>/', service_detail, name='service_detail'),
    path('equipe', equipe, name='equipe'),
    path('blog', blog, name='blog'),


    path('writeblog', writeblog, name='writeblog'),
    path('liste_membre/<int:equipe_id>/', liste_membre, name='liste_membre'),
    path('liste_projet/<int:equipe_id>/', liste_projet, name='liste_projet'),
    path('mes_projets/', mes_projets, name='mes_projets'),
    path('demander_projet/<int:projet_id>/', demander_projet, name='demander_projet'),
    path('liste_tache/<int:projet_id>/', liste_tache, name='liste_tache'),
    path('deposser/<int:tache_id>/', deposser, name='deposser'),
    
    path('send_email/', send_email, name='send_email'),
    path('send_email/', send_email, name='send_email'),
    path('login/',CustomLoginView.as_view(template_name='account/login.html'), name = 'login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
   


   
]+ statistics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
