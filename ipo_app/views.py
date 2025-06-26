from django.shortcuts import render, get_object_or_404
from rest_framework import generics, filters
from .models import IPO
from .serializers import IPOSerializer
from django_filters.rest_framework import DjangoFilterBackend

def ipo_list(request):
    query = request.GET.get("q")
    status = request.GET.get("status")
    ipos = IPO.objects.all()
    if status:
        ipos = ipos.filter(status__iexact=status)
    if query:
        ipos = ipos.filter(company_name__icontains=query)
    return render(request, 'home.html', {'ipos': ipos})

def ipo_detail(request, pk):
    ipo = get_object_or_404(IPO, pk=pk)
    return render(request, 'detail.html', {'ipo': ipo})
from rest_framework import generics
from .serializers import IPOSerializer

class IPOListAPI(generics.ListAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['company_name']
    filterset_fields = ['status']

class IPODetailAPI(generics.RetrieveAPIView):
    queryset = IPO.objects.all()
    serializer_class = IPOSerializer