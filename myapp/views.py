from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm

import requests


def info_page(request):
    api_data = request.GET.get('api_data', 'default_value')
    info_message = request.GET.get('info_message', 'default_message')
    
    return render(request, 'info.html', {'api_data': api_data, 'info_message': info_message})


def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':    

        form = UserLoginForm(request.POST)
        if form.is_valid():
            # Preparar dados para enviar à API
            data = {
                'nome': form.cleaned_data['nome'],
                'senha': form.cleaned_data['senha']
            }

            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/login', json=data)
            # Lógica de tratamento da resposta da API#joga para view index

            api_data = api_response.json()

            if api_response.status_code == 200:
                # Se a resposta da API foi bem-sucedida (status code 200)
                # Exemplo: receber dados da API (JSON)
                
                sucess_message = api_data
                # Exemplo: passar os dados para a próxima página
                #return render(request, 'info.html', {'api_data': api_data,'info_message':sucess_message})

                
                success_message2 = 'Operação realizada com sucesso'
                
                # Redirecionar para uma URL com parâmetros
                url = reverse('info_page') + f'?api_data={api_data}&info_message={success_message2}'
                return HttpResponseRedirect(url)

            else:
                # Se a resposta da API não foi bem-sucedida
                # Exemplo: exibir mensagem de erro para o usuário
                error_message = api_data
                #return render(request, 'info.html', {'form': form, 'info_message': error_message})
                success_message2 = 'nao deu login'
                
                # Redirecionar para uma URL com parâmetros
                url = reverse('info_page') + f'?api_data={api_data}&info_message={success_message2}'
                return HttpResponseRedirect(url)
           
    else:
        form = UserLoginForm()
   
    return render(request, 'login.html', {'form': form})



def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            data = {
            'nome': form.cleaned_data['nome'],
            'senha': form.cleaned_data['senha'],
            'email': form.cleaned_data['email'],
            'cpf': form.cleaned_data['cpf']
            }
            # Enviar formulário para a API (exemplo)
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/register', json=data)
            # Lógica de tratamento da resposta da API#joga para view index

            api_data = api_response.json()

        if api_response.status_code == 200:
            # Se a resposta da API foi bem-sucedida (status code 200)
            # Exemplo: receber dados da API (JSON)

            sucess_message = api_data
            # Exemplo: passar os dados para a próxima página
            return render(request, 'index.html', {'api_data': api_data,'sucess_message':sucess_message})

        else:
            # Se a resposta da API não foi bem-sucedida
            # Exemplo: exibir mensagem de erro para o usuário
            error_message = api_data
            return render(request, 'index.html', {'form': form, 'error_message': error_message})
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_details(request):
    # Redirecionar para uma URL com parâmetros
    #url = reverse('user_details')
    #return HttpResponseRedirect(url)

   
    id = 1
    api_response = requests.get(f'https://api-python-tarde-37668b622097.herokuapp.com/usuarios/{id}')
    # Lógica de tratamento da resposta da API#joga para view index

    api_data = api_response.json()

    if api_response.status_code == 200:
        # Se a resposta da API foi bem-sucedida (status code 200)
        # Exemplo: receber dados da API (JSON)

        user_name = api_data.get('nome', 'Nome não disponível')

        # Exemplo: passar os dados para a próxima página
        return render(request, 'user_details.html', {'api_data': api_data,'user_name':user_name})
    else:
        info_message = api_data
        return render(request, 'info.html', { 'info_message': info_message})