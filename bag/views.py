from django.shortcuts import render
from django.shortcuts import render, redirect, reverse, get_object_or_404

# Create your views here.
def view_bag(request):
    return render(request,'bag/bag.html')