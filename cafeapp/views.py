from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from cafeapp.decorators import cafe_ownership_required
from cafeapp.forms import CafeCreationForm
from cafeapp.models import Cafe


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class CafeCreateView(CreateView):
    model = Cafe
    form_class = CafeCreationForm
    template_name = 'cafeapp/create.html'

    def form_valid(self, form):
        temp_cafe = form.save(commit=False)
        temp_cafe.owner = self.request.user
        temp_cafe.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('cafeapp:detail', kwargs={'pk': self.object.pk})


class CafeDetailView(DetailView):
    model = Cafe
    context_object_name = 'target_cafe'
    template_name = 'cafeapp/detail.html'

    # def get_context_data(self, **kwargs):
    #     comment_list = Comment.objects.filter(cafe=self.object.pk).order_by('-created_at')
    #     # if user.is_authenticated: #로그인 했는가?
    #     # join = Join.objects.filter(user=user, project=project)
    #     # object_list = Post.object(project=self.get_object())
    #     return super(CafeDetailView, self).get_context_data(comment_list=comment_list, **kwargs)


@method_decorator(cafe_ownership_required, 'get')
@method_decorator(cafe_ownership_required, 'post')
class CafeUpdateView(UpdateView):
    model = Cafe
    context_object_name = 'target_post'
    form_class = CafeCreationForm
    template_name = 'cafeapp/update.html'

    def get_success_url(self):
        return reverse('cafeapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(cafe_ownership_required, 'get')
@method_decorator(cafe_ownership_required, 'post')
class CafeDeleteView(DeleteView):
    model = Cafe
    context_object_name = 'target_post'
    success_url = reverse_lazy('cafeapp:list')
    template_name = 'cafeapp/delete.html'

class CafeListView(ListView):
    model = Cafe
    context_object_name = 'cafe_list'
    ordering = ['-id']
    template_name = 'cafeapp/list.html'
    # def get_queryset(self):
    #     temp_list = Cafe.objects.filter()
    #
    #     page = int(self.request.GET.get('page', 1))
    #     paginator = Paginator(temp_list, 2)
    #     queryset = paginator.get_page(page)
    #
    #     return queryset