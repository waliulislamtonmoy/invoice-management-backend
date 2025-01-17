from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializer import CategorySerializer
from rest_framework import permissions

class CategoryListView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    def get(self,request):
        category=Category.objects.filter(user_id=request.user.id)
        serializer=CategorySerializer(category,many=True)
        return Response({
            "status":"success",
            "message":"category found",
            'data':serializer.data
        },status=status.HTTP_200_OK)
        
class CategoryCreateView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request):
        data=request.data
        data["user"]=request.user.id
        serializer=CategorySerializer(
            data=data,
            context={"request":request}
            )
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":"success",
            'data':serializer.data
            },status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CategoryUpdateView(APIView):
    permission_classes=(permissions.IsAuthenticated,)
    def post(self,request):
        cat_id=request.data.get("id")
        try:
            category=Category.objects.get(id=cat_id,user_id=request.user.id)
            serializer=CategorySerializer(category,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            
        except Category.DoesNotExist:
            return Response({"error":"category not found"},status=status.HTTP_404_NOT_FOUND)
        
class CategoryDeleteView(APIView):
    permission_classes=(permissions.IsAuthenticated)
    def delete(self,request,pk):
        try: 
           category=Category.objects.get(id=pk,user_id=request.user.id) 
           category.delete()
           return Response(status=status.HTTP_204_NO_CONTENT)
        except:
             return Response({"error":"Category Not Found"},status=status.HTTP_204_NO_CONTENT)
    
        
    
    
       
            
        
        
        
    

        
        
    
        
    