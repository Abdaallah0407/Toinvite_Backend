from rest_framework import generics, permissions, serializers
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from knox.models import AuthToken
from src.accounts.serializers import UserSerilaizer, RegisterSerializer, LoginSerializer, ChangePasswordSerializer, UserDetailSerializer
from src.events.serializers import *
from src.accounts.models import User
from src.events.models import Events
from src.accounts.utils import ADMIN
from services.paginators import MyPagination
# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": UserSerilaizer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API


class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        return Response({
            "user": UserSerilaizer(user,
                                   context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Get User API


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    serializer_class = UserSerilaizer

    def get_object(self):
        return self.request.user

# Change Password Serializer


class ChangePasswordAPI(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ChangePasswordSerializer


class UserProfileView(RetrieveAPIView):
    serializer_class = UserDetailSerializer

    def get(self, request, *args, **kwargs):
        queryset = User.objects.filter(id=self.kwargs['user_id'])
        user = get_object_or_404(queryset)
        serializer = UserDetailSerializer(user, context={'request': request})
        return Response(serializer.data)



class UserOwnActiveAdsView(ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Events.objects.filter(
            admin=self.request.user, is_active=True, is_published=True)
        return queryset


class UserOwnInActiveAdsView(ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == ADMIN:
            queryset = Events.objects.filter(
                is_active=False)
        else:
            queryset = Events.objects.filter(
                admin=self.request.user, is_active=False, is_published=True)
        return queryset


class UserOwnUnPublishedAdsView(ListAPIView):
    serializer_class = AdUnpublishedSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = MyPagination

    def get_queryset(self):
        if self.request.user.role == ADMIN:
            queryset = Events.objects.filter(is_published=False)
        else:
            queryset = Events.objects.filter(
                admin=self.request.user, is_published=False)
        return queryset