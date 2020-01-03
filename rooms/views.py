from django.http import Http404
from django.urls import reverse
from math import ceil
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from . import models
from django.views.generic import ListView
from django.utils import timezone

# 함수형 뷰
# def all_rooms(request):
#     page = request.GET.get("page", 1)

#     # paginator사용하기
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.get_page(int(page))
#         return render(request, "rooms/home.html", {"page": rooms})
#     except EmptyPage:
#         return redirect("/")

# 클래스 뷰
class HomeView(ListView):
    """ HomeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "rooms"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        # return redirect(reverse("core:home"))
        raise Http404()

