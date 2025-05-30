from django.db import models

# aqui, criamos as tabelas do sistema

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    #Para alterar para que os itens tenham o seu nome com o model, antes ficava 'Car_object (1)', agora fica 'Volkswagen'
    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    #colocamos a brand como foreignkey para que ela não seja digitada e sim escolhida pelo o usuário
    #Brand - tabela / on_delete - neste caso com o protect, o usuário não vai conseguir excluir a marca se ela já estiver ligada a algum carro / 
    #related_name - é um nome que colocamos para a relação entre as duas tabelas
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    #colocando imagens, todas as imagens que forem adicionadas, ficarão salvas na pasta 'cars'
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    #Para alterar para que os itens tenham o seu nome com o model, antes ficava 'Car_object (1)', agora fica 'Marea 20v'
    def __str__(self):
        return self.model

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at'] #ordenando para que o mais recente fique em primeiro
    
    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}' #para alterar para que os itens tenham o seu nome com o model, antes ficava 'CarInventory_object (1)', agora fica '10 - 10000.0'
