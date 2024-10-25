
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, status
from .permissions import IsOwnerOrAdminReadOnly
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, PledgeDetailSerializer, ProjectDetailSerializer
from django.http import Http404



class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    #GET object permissions
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    #POST object permissions
    def post(self, request):
       serializer = ProjectSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save(owner=request.user)
           return Response(
               serializer.data,
               status=status.HTTP_201_CREATED
           )
       return Response(
           serializer.errors,
           status=status.HTTP_400_BAD_REQUEST
       )

class ProjectDetail(APIView):
    permission_classes = [
    permissions.IsAuthenticatedOrReadOnly,
    IsOwnerOrAdminReadOnly
    
]
    #define GET object permissions
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    #define GET request after permission is granted
    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)
    
    #define PUT request
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
    )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
    )
    
    #define DELETE request
    def delete(self, request, pk):
        project = self.get_object(pk)
        if project.owner == request.user:
            project.delete()
            return Response("User Deleted")
        return Response ("project not authorised to be deleted", status=status.HTTP_204_NO_CONTENT)
    
    

class PledgeList(APIView):

    #GET request to retrieve all pledge instances
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    #Post reques to create new plegde
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    #retrieve all instances of the pledge model from DB
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

    #custom handling of object creation
    def perform_create(self, serializer):
        serializer.save(supporter=self.request.user)
        
    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.IsAdminUser()] 
        return [permissions.IsAuthenticatedOrReadOnly()] 

class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
        IsOwnerOrAdminReadOnly
    ]

    #retrieve a specific model instance by its primary key 
    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
    
    #update an existing resource identified by its primary key
    def put(self, request, pk):
        project = self.get_object(pk)
        self.check_object_permissions(self.request, project)
        serializer = PledgeSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    #delete an existing resource identified by its primary key
    def delete(self, request, pk):
        pledge = self.get_object(pk)
        if pledge.supporter == request.user:
            pledge.delete()
            return Response("User Deleted")
        return Response ("project not authorised to be deleted", status=status.HTTP_204_NO_CONTENT)
    
    def get(self,request,pk): 
        pledge=self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)