from django.shortcuts import render
from rest_framework.views import APIView
from .models import Student
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin,UpdateModelMixin,RetrieveModelMixin,ListModelMixin,CreateModelMixin
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets

# Create your views here.
# Class based APIview
class StudentView(APIView):
    def get(self,request,pk=None,format=None):
        if pk is not None:
            stu=Student.objects.get(pk=pk)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
        
    def post(self,request,pk=None,format=None):
    #    stu=Student.objects.get(pk=pk)
       serializer=StudentSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({'message':'Created!'})
       
       return Response(serializer.errors)
    
    def put(self,request,pk=None,format=None):
        id=request.data.get('id',None)
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Completely Updated!")
        return Response(serializer.errors)
    
    def patch(self,request,pk=None,format=None):
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Partially Updated!")
        return Response(serializer.errors)
    
    def delete(self,request,pk=None,format=None):
        stu=Student.objects.get(pk=pk)
        stu.delete()
        return Response("Item Deleted")


# Function based APIview
@api_view(['GET','POST','PUT','PATCH','DELETE'])
def hello_world(self,request):
    if request.method=='GET':
        id=request.data.get('id')
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'Message':"Data stored successfully!"})
        return Response(serializer.errors)
    
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response("Fully Updated")
        return Response(serializer.errors)
    
    if request.method=='PATCH':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return  Response("Fully Updated")
        return Response(serializer.errors)
    
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response("Deleted!")


#Generic+ModelMixin APIView
class NOTPKStudentView(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class PKStudentView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

# Concrete Genric API view
class StudentList(ListAPIView):    #To Retrieve the all instance of model
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentCreate(CreateAPIView):  #Create a new instance in model
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieve(RetrieveAPIView):  #To Retrieve a single instance from model
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentUpdate(UpdateAPIView):    # Update the instance in model(partial+complete) 
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentDelete(DestroyAPIView):  # Delete a instance from model
     queryset=Student.objects.all()
     serializer_class=StudentSerializer

class StudentListCreate(ListCreateAPIView): # Retrieve the all instances and Create a new instance in model
     queryset=Student.objects.all()
     serializer_class=StudentSerializer

class StudentRetrieveDestroy(RetrieveDestroyAPIView): # Retrieve and destroy a instance in model
     queryset=Student.objects.all()
     serializer_class=StudentSerializer

class StudentRetrieveUpdate(RetrieveUpdateAPIView): # Retrieve and update a single instance from model
     queryset=Student.objects.all()
     serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView): # Retrieve,update and destroy a single instance from model.
     queryset=Student.objects.all()
     serializer_class=StudentSerializer


# Viewset API view
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(pk=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
    
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Created")
        return Response(serializer.errors)
    
    def update(self,request,pk=None):
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Completely Updated")
        return Response(serializer.errors)
    
    def partial_update(self,request,pk=None):
        stu=Student.objects.get(pk=pk)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Partially Updated")
        return Response(serializer.errors)
    
    def destroy(self,request,pk=None):
        stu=Student.objects.get(pk=pk)
        stu.delete()
        return Response("data deleted")
    
class StudentModelview(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    def list(self, request, *args, **kwargs):
        print(request.data)
        print(self.action)
        print(args)
        print(kwargs)
        return super().list(request, *args, **kwargs)
    def retrieve(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return super().retrieve(request, *args, **kwargs)
    # def create(self, request, *args, **kwargs):
    #     print(request.data)
    #     print(args)
    #     print(kwargs)
    #     x=request.data['surname']
    #     # print(x)
    #     # request.data._mutable=True
    #     request.data['name']=x
    #     # request.data['age']='50'
    #     # request.data['roll']=80
    #     print(self.action)
    #     return super().create(request, *args, **kwargs)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)