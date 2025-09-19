from django.shortcuts import render
from app.models import student 
from app.serializers import studentserializer
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# --------------------------------function based api--------------------------------

# @api_view(["GET","POST"])
# def stu_list(req):
#      if req.method=="GET":
#         snippets = student.objects.all()
#         serializer = studentserializer(snippets, many=True)
#         return Response(serializer.data)
#      elif req.method=="POST":
#         serializer = studentserializer(data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     
# @api_view(["GET","PUT","PATCH","DELETE"])
# def stu_detail(req,pk):
#     if req.method=="GET":
#         snippets = student.objects.all()
#         serializer = studentserializer(snippets, many=True)
#         return Response(serializer.data)
#     elif req.method=="PUT":
#         snippet = student.objects.get(id=pk)

#         serializer = studentserializer(snippet, data=req.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif req.method=="PATCH":
#         snippet = student.objects.get(id=pk)
        
#         serializer = studentserializer(snippet, data=req.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif req.method=="DELETE":
#         snippet = student.objects.get(id=pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



    
    


# Create your views here.


# ------------------------------------- basic class based api ----------------------------------------------

# from app.models import student
# from app.serializers import studentserializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# class List(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = student.objects.all()
#         serializer =  studentserializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = studentserializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class Detail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return student.objects.get(pk=pk)
#         except student.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = studentserializer(snippet)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = studentserializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# -----------------------------------------------------------------------------------------

# from app.models import student
# from app.serializers import studentserializer
# from rest_framework import mixins
# from rest_framework import generics

# class List(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentserializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

# class Detail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentserializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# --------------------------------genric -------------------------------------
from app.models import student
from app.serializers import studentserializer
# from rest_framework import generics


# class List(generics.ListCreateAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentserializer


# class Detail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = student.objects.all()
#     serializer_class = studentserializer


# --------------------------------routers---------------------------------
from rest_framework import viewsets

class studentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = student.objects.all()
    serializer_class = studentserializer