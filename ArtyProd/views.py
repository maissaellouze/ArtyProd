from django.shortcuts import render
from django.views import View
from .models import *
from django.shortcuts import render, redirect 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .models import Task
from .forms import PositionForm,ProjetForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required # Importer le décorateur login_required
# Create your views here.
from datetime import datetime

class HomeView(View):
    def get(self, request):
        personnel = Personnel.objects.all()
        projets = Projet.objects.all()
        services = Service.objects.all()
        details = Detail.objects.all()
        equipes = Equipe.objects.all()

        context = {
            'personnel': personnel,
            'projets': projets,
            'services': services,
            'details': details,
            'equipes': equipes,
        }
        return render(request, 'artyprod/index.html', context)



class index(HomeView):
    template_name = 'artyprod/index.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    




class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')

    
        
        

class RegisterPage(FormView):
    template_name = 'account/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    template_name = 'artyprod/index.html'
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context



def service_detail(request, service_id):
    print(service_id)
    # Récupérer l'objet service correspondant à l'ID fourni dans l'URL
    service = get_object_or_404(Service, id=service_id)
    # Récupérer le détail associé à ce service
    detail = Detail.objects.filter(service=service)

    # Passer le détail à la template
    context = {'service': service, 'detail': detail}
    return render(request, 'artyprod/service_detail.html', context)


def tous_projets(request):
    projets = Projet.objects.all()
    context = {'projets': projets}
    return render(request, 'artyprod/tout_projet.html', context)

def blog(request):
    
    blogs = Blog.objects.all()  # Retrieve all blog objects from the database
    return render(request, 'artyprod/blog.html',{'blogs': blogs})

def writeblog(request):

    if request.method == 'POST':
        u = request.user
        name = request.POST.get("name", "")
        print(name)
        text = request.POST.get("text", "")
        image = request.FILES.get("image")
        current_date = datetime.now()
        
        print(u)
        # Créer une instance de Blog avec les données saisies
        b = Blog(utilisateur=u, nom=name, texte=text,  date_depot=current_date,Img=image)
        # Enregistrer le blog dans la base de données
        b.save()
        success_message = "Blog enregistré avec succès."
        # Rediriger vers une autre page après l'enregistrement du blog
        
        return render(request, 'artyprod/writeblog.html', {'success_message': success_message})


    return render(request, 'artyprod/writeblog.html')





def equipe(request):
    
    equipe = Equipe.objects.annotate()
    context = {'equipes': equipe}
    return render(request, 'artyprod/equipe.html', context)

def liste_membre(request, equipe_id):

    equipe = get_object_or_404(Equipe, id=equipe_id)

    membres = Personnel.objects.filter(Equipe=equipe)

    # Passer le détail à la template
    context = {'equipe': equipe, 'membres': membres}
    return render(request, 'artyprod/liste_membre.html', context)

def liste_projet(request, equipe_id):

    equipe = get_object_or_404(Equipe, id=equipe_id)

    projet = Projet.objects.filter(equipe=equipe)

    # Passer le détail à la template
    context = {'equipe': equipe, 'projet': projet}
    return render(request, 'artyprod/liste_projet.html', context)


def service_detail(request, service_id):
    print(service_id)
    # Récupérer l'objet service correspondant à l'ID fourni dans l'URL
    service = get_object_or_404(Service, id=service_id)
    # Récupérer le détail associé à ce service
    detail = Detail.objects.filter(service=service)

    # Passer le détail à la template
    context = {'service': service, 'detail': detail}
    return render(request, 'artyprod/service_detail.html', context)



def mes_projets(request):
    utilisateur = request.user
    
    per = Personnel.objects.filter(user=utilisateur).first()
    demandes_approuvees = demande_projet.objects.filter(Personnel=per,approvee=True )
    context = {'projets': demandes_approuvees}

    
    return render(request, 'artyprod/mes_projets.html', context)




@login_required

def demander_projet(request, projet_id):
    proj = get_object_or_404(Projet, pk=projet_id)
    u = request.user
    per = Personnel.objects.filter(user=u).first()

    if per:
        print('success')
        demande = demande_projet(Personnel=per, Projet=proj)
        demande.save()
        messages.success(request, 'Votre demande a été envoyée avec succès !')
        print('success')
    return redirect(request.META.get('HTTP_REFERER', '/'))


def liste_tache(request, projet_id):
    print(projet_id)
    # Récupérer l'objet service correspondant à l'ID fourni dans l'URL
    p = get_object_or_404(Projet, id=projet_id)
    # Récupérer le détail associé à ce service
    tache = Tache.objects.filter(projet=p)
    t = Tache.objects.filter(projet=projet_id)
    total_taches = t.count()
    nbr= Tache.objects.filter(date_depot__isnull=False).count()
    porcent = (nbr / total_taches) * 100 
    print(porcent)
    p.pourcentage=porcent*100
    print(porcent)
    # Passer le détail à la template
    context = {'projet': p, 'tache': tache}
    return render(request, 'artyprod/liste_tache.html', context)



def deposser(request, tache_id):
    u = request.user
    per = Personnel.objects.filter(user=u).first()
    print(tache_id)
    tache = get_object_or_404(Tache, pk=tache_id)

    image = request.FILES.get('image')
    print('maissa')
        # Mettre à jour l'image de la tâche
    tache.Img = image
    tache.personne = per
    print('ellouze')
        
        # Mettre à jour la date avec la date actuelle
    tache.date_depot = date.today()
        
        # Enregistrer les modifications dans la base de données
    tache.save()
        
    return redirect(request.META.get('HTTP_REFERER', '/') )
def send_email(request):
    template_name = 'artyprod/contact.html'

    name = request.POST.get("name", "")
    from_email = request.POST.get("email", "")
    message = request.POST.get("message", "")
    
    if name and message and from_email:
       
        send_mail(
                name, 
                message, 
                from_email, 
                ["maissaellouze02@gmail.com"],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us!')

    # Redirection vers la même page avec un ancrage
        return redirect(request.META.get('HTTP_REFERER', '/') + '#footer')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return render(request, 'artyprod/send_email.html')
    

