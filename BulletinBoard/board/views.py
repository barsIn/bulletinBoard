from django.shortcuts import render, redirect
from django.core.mail import send_mail
import os
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, request
from .models import Advertisement, Response, User
from django.views.generic.base import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .forms import AdvCreateForm, RespCreateForm
from django.contrib.auth.decorators import login_required


class AdvertisementView(View):
    def get(self, request):
        adv = Advertisement.objects.all()

        return render(request, 'board/advertisement.html', {'adv_list': adv})


class AdvertisementDetailView(DetailView):
    model = Advertisement
    template_name = 'board/adv_detail.html'
    context_object_name = 'adv'


class AdvCreate(LoginRequiredMixin, CreateView):
    template_name = 'board/adv_create.html'
    form_class = RespCreateForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.user = self.request.user
        fields.save()

        return super().form_valid(form)


# class RespCreate(LoginRequiredMixin, CreateView):
#     template_name = 'board/adv_create.html'
#     form_class = AdvCreateForm
#     success_url = reverse_lazy('index')
#
#     def form_valid(self, form):
#         fields = form.save(commit=False)
#         fields.author = self.request.user
#         fields.save()
#
#         return super().form_valid(form)


def respCreate(request, pk):

    if request.method == 'POST':
        form = RespCreateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['tekst']
            advertisement = Advertisement.objects.get(pk=pk)
            Response.objects.create(tekst=text, advertisement=advertisement, user=request.user)

        return redirect('adv_detail', pk)
    else:
        form = RespCreateForm()
    return render(request, 'board/createresp.html', {'form': form})



class AdvSearch(View):
    pass

class AdvUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'board/adv_update.html'
    form_class = AdvCreateForm
    model = Advertisement
    context_object_name = 'adv'
    # success_url = reverse_lazy('adv_detail')
    permission_required = ('Advertisement.change_post')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advertisement.objects.get(pk=id)



class AdvDeleteView(LoginRequiredMixin, DeleteView):
    model = Advertisement
    template_name = 'board/adv_delete.html'
    queryset = Advertisement.objects.all()
    success_url = ''
    context_object_name = 'adv'



class UserDetailView(DetailView):
    model = User
    template_name = 'board/user_detail.html'
    context_object_name = 'user'

@login_required()
def confirm_resp(request, id):
     resp = Response.objects.get(id=id)
     resp.is_confirm = True
     resp.save()
     author = resp.user
     adv = resp.advertisement.heading
     id = request.user.id

     send_mail(
         'Подтвержден ваш отклик на объявление',
         f'Подтвержден ваш отклик на объявление {adv}',
         f"{os.getenv('MY_MAIL')}",
         [f'{author.email}'],
         fail_silently=False,
     )
     return redirect(f'/user/{id}')

@login_required()
def delete_resp(request, id):
     resp = Response.objects.get(id=id)
     resp.delete()

     id = request.user.id


     return redirect(f'/user/{id}')



