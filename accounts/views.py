from django.views import View
from .models import CustomUser
from django.shortcuts import render, redirect
from .forms import User_data_Form
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required

def user_data_input(request):
    """新規ユーザー情報の入力。"""
    # 一覧表示からの遷移や、確認画面から戻るリンクを押したときはここ。
    if request.method == 'GET':
        # セッションに入力途中のデータがあればそれを使う。
        form = User_data_Form(request.session.get('form_data'))
    else:
        form = User_data_Form(request.POST)
        if form.is_valid():
            # 入力後の送信ボタンでここ。セッションに入力データを格納する。
            request.session['form_data'] = request.POST
            return redirect('user_data_confirm')

    context = {
        'form': form
    }
    return render(request, 'user_data_input.html', context)

def user_data_confirm(request):
    """入力データの確認画面。"""
    # registerviewで入力したユーザー情報をセッションから取り出す。
    session_form_data = request.session.get('form_data')
    if session_form_data is None:
        # セッション切れや、セッションが空でURL直接入力したら入力画面にリダイレクト。
        return redirect('user_data_input')

    context = {
        'form': User_data_Form(session_form_data)
    }
    return render(request, 'user_data_confirm.html', context)


def user_data_create(request):
    """ユーザーを作成する。"""
    # user_data_inputで入力したユーザー情報をセッションから取り出す。
    # ユーザー作成後は、セッションを空にしたいのでpopメソッドで取り出す。
    session_form_data = request.session.pop('form_data', None)
    if session_form_data is None:
        # ここにはPOSTメソッドで、かつセッションに入力データがなかった場合だけ。
        # セッション切れや、不正なアクセス対策。
        return redirect('user_data_input')

    form = User_data_Form(session_form_data)
    if form.is_valid():
        form.save()
        return redirect('admin')

    # is_validに通過したデータだけセッションに格納しているので、ここ以降の処理は基本的には通らない。
    context = {
        'form': form
    }
    return render(request, 'user_data_input', context)


def loginview(request):
    if request.method == 'POST':
        email_data = request.POST['email_data']
        password_data = request.POST['password_data']
        user = authenticate(request,email=email_data,password=password_data)
        if user is not None:
            login(request,user)
            return redirect('userhome')
        else:
            return redirect('login')
    return render(request,'login.html')

@login_required
def userhomeview(request):
    object_userdata = CustomUser.objects.all()
    return render(request,'userhome.html',{'object_userdata':object_userdata})