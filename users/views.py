from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import api_view,permission_classes,action
from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer,UserRegisterSerializer
from .models import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # @action(methods=['post'],permission_classes=[AllowAny,],detail=False)
    # def register(self,request):
    #     serializer = UserRegisterSerializer(data = request.data)
    #     serializer.is_valid(raise_exception=True)
    #
    #     model_serializer = UserSerializer(data=serializer.data)
    #     model_serializer.is_valid(raise_exception=True)
    #     model_serializer.save()
    #     return Response(model_serializer.data)

class UserRegisterView(CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer
    permission_classes(AllowAny,)



def index(request):
    return render(request, 'auth.html')