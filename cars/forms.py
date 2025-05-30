from django import forms
from cars.models import Brand, Car


# class CarForm(forms.Form): #ele herda da classe forms
#     model = forms.CharField(max_length=200)
#     brand = forms.ModelChoiceField(Brand.objects.all()) #para buscar todas as marcas e trazer a lista delas em um dropdown list
#     factory_year = forms.IntegerField()
#     model_year = forms.IntegerField()
#     plate = forms.CharField(max_length=10)
#     value = forms.FloatField()
#     photo = forms.ImageField()

#     def save(self): #o self neste caso, está se referindo ao CarForm, poderia ser o CarForm no lugar
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         ) #com isso é um criado um novo registro(objeto) no bd
#         car.save() #save do objeto car, no bd
#         return car

#uma outra maneira de fazer o que foi feito no bloco acima
class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__' # significa que eu quero todos os campos da classe Car. 


    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1995')
        return factory_year