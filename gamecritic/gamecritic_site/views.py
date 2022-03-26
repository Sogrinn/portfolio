from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegisterForm, LoginForm, GameForm, ReviewForm
from .models import Game, Review


def index(request):
    return render(request, 'index.html')


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form': form})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            print(form.errors)
        return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()
        return render(request, "form.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("index")


def game_list(request):
    games = Game.objects.all()
    return render(request, 'game_list1.html', {'games': games})


def game_review_list(request, game_id):
    reviews = Review.objects.filter(game=game_id)
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game_review_list.html', {'reviews': reviews, 'game': game})


@login_required
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            game = Game.objects.create(**form.cleaned_data)
            return redirect('game_review_list', game.id)
    else:
        form = GameForm()
        return render(request, 'form.html', {'form': form})


@login_required
def edit_game(request, game_id):
    if request.method == 'POST':
        form = Game(request.POST)
        if form.is_valid():
            game = get_object_or_404(Game, pk=game_id)
            game = form.cleaned_data
            game.save()
            return redirect('game_review_list', game.id)
    else:
        form = GameForm()
        return render(request, 'form.html', {'form': form})


@login_required
def add_review(request, game_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            game = get_object_or_404(Game, pk=game_id)
            Review.objects.create(game=game, user=user, **form.cleaned_data)
            return redirect('game_review_list', game.id)
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    if review.user == user:
        review.delete()
        return redirect('game_review_list', review.game.id)
    return HttpResponse('You can delete only your reviews!')


@login_required
def edit_review(request, review_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            review = get_object_or_404(Review, pk=review_id)
            if review.user == user:
                review.text = form.cleaned_data["text"]
                review.rating = form.cleaned_data["rating"]
                review.save()
                return redirect('game_review_list', review.game.id)
            return HttpResponse('You can edit only your reviews!')
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})