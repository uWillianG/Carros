from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory
from openai_api.client import get_car_ai_bio

def car_inventory_update():
    cars_count = Car.objects.all().count() #contando quantos carros tem na tabela
    cars_value = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value'] #pega apenas o valor associado à chave 'total_value', ou seja, o total somado dos valores dos carros.
    CarInventory.objects.create(
        cars_count=cars_count,
        cars_value=cars_value
    )

@receiver(post_save, sender=Car) #o post_save é chamado depois que o carro é salvo, serve tanto para criar quanto para atualizar
#o sender é a tabela que queremos monitorar, nesse caso a tabela Car
def car_post_save(sender, instance, **kwargs): 
    car_inventory_update()

    #se eu quero controlar apenas a criação, eu coloco o created
    # if created:
    #     car_inventory_update()

@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()


@receiver(pre_save, sender=Car) #estou declarando que esse sinal vai ser chamado antes de salvar um carro
def car_pre_save(sender, instance, **kwargs): #parametros obrigatorios, apenas o kwargs é opcional, mas coloca-lo é uma boa prática
    if not instance.bio:
        ai_bio = get_car_ai_bio(
            instance.model,instance.brand, instance.model_year
        )
        instance.bio = ai_bio

# @receiver(pre_delete, sender=Car)
# def car_pre_delete(sender, instance, **kwargs): 
#     print('### PRE DELETE ###')
#     print(instance.model, instance.brand)
