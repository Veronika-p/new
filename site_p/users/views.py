from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from students.models import Articles, Tasks, Answer, Statistic

def test(request):
    return redirect('main/test.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Ваш аккаунт создан: можно войти на сайт.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        all_keys = request.POST.keys()
        numeric_keys = [key for key in all_keys if key.isdigit()]
        filtered_data = {key: request.POST.getlist(key) for key in numeric_keys}
        keys_view = filtered_data.keys()
        count = 0
        count_pr = 0
        for key in keys_view:

            if Tasks.objects.filter(id=int(key)).exists():
                ans = Answer()
                ans.user = get_object_or_404(Articles, id=request.session['user'])
                ans.answer = filtered_data[key][0]
                ans.task = get_object_or_404(Tasks, id=key)
                ans.save()
                if Tasks.objects.filter(otvet_tasks=filtered_data[key][0]).exists():
                    count_pr += 1
            count+=1
        s = Statistic()
        s.user = get_object_or_404(Articles, id=request.session['user'])
        s.bal = count_pr
        s.count_question = count
        s.save()
        return redirect('/profile')
    else:
        tests_user = []
        try:
            user_cur = get_object_or_404(Articles, id=request.session['user'])
            for t in user_cur.tests.all():
                try:
                    get_object_or_404(Answer, task=t)
                except:
                    tests_user.append({'number_tasks': t.number_tasks, 'image_tasks': t.image_tasks, 'id': t.id})
        except Http404:
            pass
            #return redirect('/')

        return render(request, 'users/profile.html', context={'tests_user': tests_user, 'count': len(tests_user)})


