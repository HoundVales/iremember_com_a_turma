import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def listar_posts(request):
    try:
        # URL da API Flask
        url = 'https://api-python-tarde-37668b622097.herokuapp.com/posts'  # ajuste o endereço e a porta conforme necessário

        # Enviar requisição GET para a API Flask
        response = requests.get(url)
        response.raise_for_status()  # Levanta uma exceção para códigos de status HTTP de erro

        # Verificar se a resposta contém dados
        posts = response.json()

        # Renderizar o template com os posts
        template = loader.get_template('listar_posts.html')
        context = {'posts': posts}
        return HttpResponse(template.render(context, request))

    except requests.RequestException as e:
        # Em caso de erro na requisição
        return HttpResponse(f"Erro ao buscar os posts: {e}", status=500)