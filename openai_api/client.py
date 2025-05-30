import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

client = openai.Client()

def get_car_ai_bio(model, brand, year):
    message = ''''
    Me mostre uma descrição de venda para o carro {} {} {} em apenas 250 caracteres. Fale coisas específicas desse modelo.
    Descreva especificações técnicas desse modelo de carro.
    '''
    message = message.format(brand, model, year)#isso substitui os valores do prompt, o primeiro {} vai ser substituido pelo model, o segundo pelo brand e o terceiro pelo year
    response = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': message
            }
        ],
        max_tokens=1000,
        model='gpt-3.5-turbo',
    )

    return response.choices[0].message.content #aqui, como o retorno do openai
    #é enviado um objeto JSON, isso escrito acima, quer dizer que quero pegar o primeiro item da lista 'choices' e o texto dele

     