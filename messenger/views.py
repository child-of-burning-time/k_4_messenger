from django.shortcuts import render, redirect


def index(request):
    return redirect('messenger:dialogues')


def dialogues(request):
    return render(request, 'messenger/dialogues.html')