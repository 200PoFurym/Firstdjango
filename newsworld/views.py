from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView

from news.form import RegisterForm, LoginForm
from newsworld.models import News, NewsCategory, CartModel, LikeModel


# Create your views here.
def home_page(request):
    news = News.objects.all()
    categories = NewsCategory.objects.all()
    if request.method == 'POST':
        get_news = request.POST.get('search_news')
        if get_news:
            exact_news = News.objects.filter(news_name__icontains=get_news)
            context = {'news': news, 'categories': categories, 'search_news': exact_news}
            return render(request, 'index.html', context=context)
    else:
        context = {'news': news, 'categories': categories}
        return render(request, template_name='index.html', context=context)


def single_news(request, id):
    news = News.objects.get(id=id)
    context = {'news': news}
    return render(request, 'single_news.html', context=context)


class MyFormView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'


class MyLoginFormView(CreateView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'


def logout_view(request):
    logout(request)
    return redirect('/')


def category_page(request, id):
    categories = NewsCategory.objects.get(id=id)
    news = News.objects.filter(category=categories)
    context = {'categories': categories, 'news': news}
    return render(request, 'category_news.html', context=context)


def add_product_to_cart(request, id):
    if request.method == 'POST':
        cheker = News.objects.get(id=id)
        # if cheker.count >= int(request.POST.get('count')):
        CartModel.objects.create(user_id=request.user.id,
                                     user_news=cheker).save()
                                     # user_product_quantity=int(request.POST.get('count'))).save()
        return redirect('/user_cart')
    else:
        return redirect('/')


def user_cart(request):
    cart = CartModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'Новый заказ'
        for i in cart:
            main_text += f'Новости: {i.user_news}\n' \
                         f'ID пользователя: {i.user_id}'

    else:
        return render(request, 'cart.html', {'cart': cart})

def add_like(request, id):
    if request.method == 'POST':
        cheker = News.objects.get(id=id)
        LikeModel.objects.create(user_id=request.user.id, user_news=cheker).save()
        return redirect('user_likes')
    else:
        return redirect('/')
def user_likes(request):
    like = LikeModel.objects.filter(user_id=request.user.id)
    if request.method == 'POST':
        main_text = 'Добавлено в избранное'
        for i in like:
            main_text += f'Новость: {i.user_news}\n' \
                         f'ID пользователя: {i.user_id}'
    else:
        return render(request, 'like.html', {'like': like})

