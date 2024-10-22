from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import permissions
from projects.permissions import IsSelfOrSuperUser
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.views.decorators.csrf import csrf_exempt

# class CustomUserList(APIView):

#     # only admin can see all users
#     def get_permissions(self):
#         if self.request.method == 'GET':
#             return [permissions.IsAdminUser()] 
#         return [permissions.AllowAny()] 
 
    
#     # retrieves a list of all users
#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = CustomUserSerializer(users, many=True)
#         return Response(serializer.data)

#     def post(self, request):
        
#         #creates a new user if the data is valid, and returns either the created user's data or validation errors
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data,
#                 status=status.HTTP_201_CREATED
#             )
#         return Response(
#             serializer.errors, 
#             status=status.HTTP_400_BAD_REQUEST
#         )

class CustomUserList(APIView):

    # Only admin can see all users
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()]
        return super().get_permissions()  # Call the superclass method for other methods

    # Retrieves a list of all users
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Creates a new user if the data is valid, and returns either the created user's data or validation errors
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class CustomUserDetail(APIView):
    
    permission_classes = [
        permissions.IsAuthenticated,
        IsSelfOrSuperUser
    ]
   
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404("User not found.")

    def get(self, request, pk):
        user = self.get_object(pk)  # Fetch the user object
        serializer = CustomUserSerializer(user)  # Initialize the serializer with the user
        return Response(serializer.data)  # Return the serialized data
    
    def put(self, request, pk):
        user = self.get_object(pk)  # Fetch the user object
        serializer = CustomUserSerializer(instance=user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save the updated user
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)  # Fetch the user object
        user.delete()  # Delete the user
        return Response(status=status.HTTP_204_NO_CONTENT)    
    

@csrf_exempt  # Disable CSRF for this view
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        # Return user details along with the token
        return Response({
            'token': token.key,
            'user_id': user.id,
            'email': user.email,
            'username': user.username  # Optional: include the username
        }, status=status.HTTP_200_OK)