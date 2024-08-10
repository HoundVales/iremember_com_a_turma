# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from myapp.forms.post_forms import PostForm
import requests

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            id = 1
            data = {
                'titulo': form.cleaned_data['titulo'],
                'conteudo': form.cleaned_data['conteudo'],
                'autor_id':id
            }
            api_response = requests.post('https://api-python-tarde-37668b622097.herokuapp.com/posts', json=data)
            api_data = api_response.json()
            if api_response.status_code == 201:
                success_message2 = 'Post criado com sucesso'
                url = reverse('info') + f'?api_data={api_data}&info_message={success_message2}'
                return HttpResponseRedirect(url)
            else:
                success_message2 = 'Erro ao criar o post'
                url = reverse('info') + f'?api_data={api_data}&info_message={success_message2}'
                return HttpResponseRedirect(url)
        else:
            return JsonResponse({"message": "Erro ao criar o post", "errors": form.errors}, status=400)
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})