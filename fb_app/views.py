from django.shortcuts import render
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

# Create your views here.
