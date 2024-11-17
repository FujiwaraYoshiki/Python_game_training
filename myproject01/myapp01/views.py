# myapp01/views.py
from django.shortcuts import render


def index(request):
    if request.method == "POST":
        # フォームから送られたデータを取得
        name = request.POST.get('name', '')
        message = f"Hello, {name}! Nice to meet you!"
    else:
        # デフォルトのメッセージ
        message = "Hello! Please enter your name."

    context = {
        'message': message
    }
    return render(request, 'myapp01/index.html', context)
