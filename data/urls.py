"""crypto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path

    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from data import views

urlpatterns = [
    path('bi_dashboard/', views.bi_dashboard_view, name='bi_dashboard'),
    path('prediction/user/', views.predict_user_profit, name='prediction_user'),
    path('prediction/btc/', views.PredictBTCPrice.as_view(), name='prediction_btc'),
]
