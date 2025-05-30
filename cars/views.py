from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm
from django.views import View
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

#uma outra maneira de fazer o CarsView
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    #defindo quais carros quero que apareçam neste view (filtro) / uma busca personalizada
    def get_queryset(self):
        cars = super().get_queryset().order_by('-model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    
# o @ é a sintaxe padrao do python para decorators
@method_decorator(login_required(login_url='login'), name='dispatch') #decorator para proteger a view, ou seja, só pode acessar se estiver logado / o login_url é a url que o usuário será redirecionado caso não esteja logado / o dispatch é o método que é chamado quando a view é acessada
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm #deve sempre informar o form quando utilizamos o CreateView
    template_name = 'new_car.html'
    success_url = '/cars/' #quando cadastrar o carro com sucesso, o usuário será redirecionado para esta url

@method_decorator(login_required(login_url='login'), name='dispatch')    
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm #mesmo form do CreateView, mas agora para editar
    template_name = 'car_update.html'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk}) #depois de editar o carro, o usuário será redirecionado para a página de detalhes do carro editado
        #reverse_lazy: é uma função que retorna a url da view, sem precisar passar a url diretamente. O reverse_lazy é usado para evitar problemas de importação circular, pois ele não tenta resolver a URL até que seja necessário.
        ##kwargs: é um dicionário que contém os argumentos nomeados que serão passados para a URL. Neste caso, estamos passando o pk do objeto que foi editado.

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'


# ------------------------------------------------------------------------------------- #

# def cars_view(request):
#     cars = Car.objects.all().order_by('-model') #o menos, faz um "order by desc"
#     search = request.GET.get('search')

#     if search: #neste caso, se o usuário digitar algo, irá percorrer o if, e se não, o sistema vai carregar todos os carros
        # cars = Car.objects.filter(model__icontains=search) #desta forma, está filtrando pelo o que o usuário digitou

        #através deste bloco do html, o usuário vai digitar, e o sistema vai compreender que tem que fazer a busca conforme ele procurar
        #<form method="GET" action="{% url 'cars_list' %}">
        #    <input type="text" name="search" placeholder="Buscar carro...">
        #    <button type="submit">Buscar</button>
        #</form>

    #para filtrar por caracter, é feito da seguinte forma: nome da coluna + dois underlines + icontains, ex: model__contains='Civ', como se fosse um like
    #para filtrar por um campo que não está na tabela cars, utilizamos dois underlines, ex: brand__name='Honda', como se fosse uma subquery. 

    # return render(
    #     request, 
    #     'cars.html',
    #     {'cars': cars}
    # )


# def new_car_view(request):
#     if request.method == 'POST':
#         new_car_form = CarModelForm(request.POST, request.FILES) #request files pois tem fotos
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list') #leva o usuário para a tela com a lista de carros
#     else:
#         new_car_form = CarModelForm()
#    return render(request, 'new_car.html', { 'new_car_form': new_car_form})


# class CarsView(View):
    
#     def get(self, request):
#         cars = Car.objects.all().order_by('-model') #o menos, faz um "order by desc"
#         search = request.GET.get('search')

#         if search:
#             cars = Car.objects.filter(model__icontains=search)

#         return render(
#             request, 
#             'cars.html',
#             {'cars': cars}
#         )

#class NewCarView(View):
    
    # def get(self, request):
    #     new_car_form = CarModelForm()
    #     return render(request, 'new_car.html', { 'new_car_form': new_car_form})
    
    # def post(self, request):
    #     new_car_form = CarModelForm(request.POST, request.FILES)
    #     if new_car_form.is_valid():
    #         new_car_form.save()
    #         return redirect('cars_list')
    #     return render(request, 'new_car.html', { 'new_car_form': new_car_form})