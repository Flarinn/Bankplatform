from inspect import trace

from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponse
from django.views.generic import CreateView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
from .serializers import AccountSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect
from .forms import ApplicationForm, ApplicationPrincipalCompanyForm, ApplicationBeneficiarCompanyForm, AgentAccountForm, \
    AgentAccountProfileForm, PersonApplicationInfoForm, ApplicationInfoForm

menu = []



@api_view(['POST', 'GET'])
def create_ben_companies(request):
    error = ''
    if request.method == 'POST':
        form2 = ApplicationBeneficiarCompanyForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('create')
        else:
            if error.find('Principal company with this Name already exists'):
                return redirect('create')
            else:
                error = form2.errors
    return render(request, 'account/createbencompany.html',
                  {'menu': menu, 'title': 'Добавление компании Бенефициара', 'form2': ApplicationBeneficiarCompanyForm,
                   'error': error})


@api_view(['POST', 'GET'])
def create_princ_companies(request):
    error = ''
    if request.method == 'POST':
        form2 = ApplicationPrincipalCompanyForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('createbencompany')
        else:
            if error.find('Principal company with this Name already exists'):
                return redirect('createbencompany')
            else:
                error = form2.errors
    return render(request, 'account/createprincompany.html',
                  {'menu': menu, 'title': 'Добавление компании Принципала', 'form2': ApplicationPrincipalCompanyForm,
                   'error': error})


@api_view(['POST', 'GET'])
# @permission_classes([IsAuthenticatedOrReadOnly])
def create(request):
    error = ''
    percent = ''
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.Status='Подробное заполнение заявки агентом'
            form.save()
            form.WorkerId.set(request.user.id)
            print(request.user.id)
            print(form)
            #return redirect('applicationlist')
        else:
            print('neeet')
            form = ApplicationInfoForm()
            error = form.errors
            error1 = form.non_field_errors()
            print(error)
            print(error1)
    return render(request, 'account/create.html',
                  {'menu': menu, 'title': 'Создание заявки', 'form': ApplicationForm(), 'error': error})


@api_view(['POST', 'GET'])
def user_login(request):
    error = ''
    if request.method == 'POST':
        form = AgentAccountForm(request.POST)
        print('fufel')
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            print(cd)
            if user is not None:
                if user.is_active:
                    AgentAccountForm(request, user)
                    return HttpResponse('Authenticated successfully')
                    return redirect('create')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
        else:
            print(error)
            form = AgentAccountForm()
    return render(request, 'account/login.html',
                  {'menu': menu, 'title': 'Логин', 'form': AgentAccountForm(), 'error': error})

def logout_user(request):
    logout(request)
    return redirect('agentlogin')



def sign_in(request):
    error = ''
    if request.method == 'GET':
        form = AgentAccountForm()
        return render(request, 'account/login.html', {'form': form,'error': error})
    elif request.method == 'POST':
        form = AgentAccountForm(request.POST)
        print('eweeeee')
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print('kekw')
            if user:
                login(request, user)
                if user.profile.role== 'AGENT':
                    return redirect('profile', username)
                if user.profile.role == 'BANK':
                    return redirect('profile', username)
                if user.profile.role == 'PLATFORM':
                    return redirect('profile', username)
        else:
            error=form.errors
        # form is not valid or user is not authenticated
        messages.error(request, f'Invalid username or password')
        print(error)
        return render(request, 'account/login.html', {'menu': menu, 'title': 'Логин', 'form': form,'error': error})


def application_list(request):
    if request.method == "POST":
        pass
    return render(request, 'account/application.html', {'menu': menu, 'title': 'Профиль'})

def application_info(request,application_id):
    error=''
    application = Application.objects.get(pk=application_id)
    ben_company = BeneficiarCompany.objects.get(pk=application.BeneficiarCompany)
    princ_company = PrincipalCompany.objects.get(pk=application.PrincipalCompany)
    if request.method == 'GET':
        form= ApplicationInfoForm(instance=application)
        form_ben = ApplicationBeneficiarCompanyForm(instance=ben_company)
        form_princ = ApplicationPrincipalCompanyForm(instance=princ_company)
        form1 = PersonApplicationInfoForm()
        form2 = PersonApplicationInfoForm()
        return render(request, 'account/detail.html', {'menu': menu,'form_princ': form_princ, 'title': 'Профиль', 'form':form, 'form1':form1,'form2':form2, 'form_ben': form_ben,'application':application})
    if request.method == 'POST':
        form = ApplicationForm(request.POST, instance=application)
        form1 = PersonApplicationInfoForm(request.POST)
        form_princ = ApplicationPrincipalCompanyForm(instance=princ_company)
        form_ben = ApplicationBeneficiarCompanyForm(request.POST, instance=ben_company)
        print('eeeee')
        if form.is_valid():
            print('rrrrrr')
        else:
            print(form.errors)
        if form1.is_valid():
            print('dadada')
        if form_ben.is_valid():
            print('kekeke')
        if form.is_valid() and form1.is_valid() and form_ben.is_valid() and form_princ.is_valid():
            print('dadad')
            form = form.save(commit=False)
            if 'Отправить заявку агент' in request.POST:
                form.Status='На проверке у сотрудника платформы'
            if 'Отправить заявку платформа' in request.POST:
                form.Status='На рассмотрении у банка'
            if 'Отправить на доработку' in request.POST:
                form.Status='На заполнении у агента'
            if 'Отказать в выдаче' in request.POST:
                form.Status='Отказано'
            if 'Отправить предложение клиенту' in request.POST:
                form.Status='На согласовании у агента'
            form1 = form1.save(commit=False)
            form1.Rank = 'Владелец'
            form1.save()
            #form2.save(
            form_ben=form_ben.save(commit=False)
            form_ben.Name = form.BeneficiarCompany
            form_princ = form_princ.save(commit=False)
            form_princ.Name = form.PrincipalCompany
            form_ben.Vlad=form1.id
            form_ben.save()
            form_princ.save()
            # form.AgentWorkerId = request.user
            form.save()
            return redirect('home')
        else:
            form = ApplicationInfoForm(instance=application)
            error=form1.errors
            error =form1.non_field_errors()
            print(error)
            error=form.non_field_errors()
            print(error)
            error=form_ben.non_field_errors()
            print(error)
    return render(request, 'account/detail.html', {'menu': menu, 'title': 'Профиль', 'application': application,'form_princ': form_princ,'form':form,'form_ben': form_ben, 'form1':form1, 'error':error})


def profile(request, username):
    if request.method == 'POST':
        pass

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = AgentAccountForm(user)
        form1 = AgentAccountProfileForm(user)
        return render(request, 'account/profile.html',
                      context={'menu': menu, 'title': 'Профиль', 'form': form, 'form1': form1})

    return redirect("login")


def person_info(request,company):
    if request.method == 'GET':
        form = PersonApplicationInfoForm()
        return render(request, 'account/person.html', {'menu': menu, 'title': 'Профиль', 'form':form})
    if request.method == 'POST':
        form = PersonApplicationInfoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'account/person.html', {'menu': menu, 'title': 'Профиль', 'form':form})


def userpage(request):
    user_form = AgentAccountForm(instance=request.user)
    profile_form = AgentAccountProfileForm(instance=request.user.profile)
    return render(request=request, template_name="account/profile.html",
                  context={"user": request.user, "user_form": user_form, "profile_form": profile_form})


def custom_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    form = AgentAccountForm()

    return render(
        request=request,
        template_name="account/login.html",
        context={'form': form}
    )


class SignUpView(LoginView):
    model = User
    form_class = AgentAccountForm
    template_name = 'account/login.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        print('zaregan')
        # return redirect('students:quiz_list')


def percentCalc(Sum, Month):
    # Банковская логика вычисления процентов
    percentban = 0.03
    percentPlat = 0.01
    percent = percentban + percentPlat
    return percent


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def agent_account_list(request, format=None):
    # get all the ag_accounts
    # serialize them
    # return them
    if request.method == 'GET':
        ag_accounts = Profile.objects.all()
        serializer = AccountSerializer(ag_accounts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def agent_detail(request, id, format=None):  # Передаем id чтобы по нему посмотреть AgAccount
    try:
        ag_account = Profile.objects.get(pk=id)
    except Profile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = AccountSerializer(ag_account)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AccountSerializer(ag_account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        pass
    elif request.method == 'DELETE':
        ag_account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'POST':
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = AgentAccountForm(instance=request.user, data=request.POST)
        profile_form = AgentAccountProfileForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = AgentAccountForm(instance=request.user)
        profile_form = AgentAccountProfileForm(instance=request.user.profile)
        return render(request,
                      'account/profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

def anonymous_required(redirect_url):
    """
    Decorator for views that allow only unauthenticated users to access view.
    Usage:
    @anonymous_required(redirect_url='company_info')
    def homepage(request):
        return render(request, 'homepage.html')
    """
    def _wrapped(view_func, *args, **kwargs):
        def check_anonymous(request, *args, **kwargs):
            view = view_func(request, *args, **kwargs)
            if request.user.is_authenticated():
                return redirect(redirect_url)
            return view
        return check_anonymous
    return _wrapped

def index(request):  # главная страница
    return render(request, 'account/index.html', {'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'account/about.html', {'menu': menu, 'title': 'О компании'})

@permission_classes([IsAuthenticatedOrReadOnly])
def agent(request):
    if request.method == 'POST':
        print('post /agent')
    return render(request, 'account/agent.html', {'menu': menu, 'title': 'О компании'})
