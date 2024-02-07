"""
apppppppppppppplication
"""
from django.contrib import admin
from django.urls import path

from base.views import products

urlpatterns = [
    path('products/', products),
    path('products/<int:id>', products)
]
