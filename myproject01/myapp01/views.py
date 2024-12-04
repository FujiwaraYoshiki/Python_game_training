# myapp01/views.py
from django.shortcuts import render
from .forms import NameForm


def index(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            # フォームが有効ならデータを取り出す
            name = form.cleaned_data['name']
            message = f"Hello, {name}! Nice to meet you!"
        else:
            message = "Invalid input. Please try again."
    else:
        form = NameForm()
        message = "Hello! Please enter your name."

    context = {
        'form': form,
        'message': message,
    }
    return render(request, 'myapp01/index.html', context)
