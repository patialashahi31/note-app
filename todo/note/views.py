from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Note
from rest_framework.response import Response
from .serializers import NoteSerializer

# Create your views here.

class NoteAPIView(GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    model = Note
    
    def get(self,request,pk=None):
        if pk:
            obj= self.model.objects.filter(pk=pk).first()
            ss = self.serializer_class(instance=obj)
            return Response(ss.data,status=200)
        ss = self.serializer_class(self.model.objects.all(),many=True)
        return Response(ss.data,status=200)
        

    def post(self,request):
        data = request.data
        s = self.serializer_class(data=data)
        if s.is_valid():
            s.save()
        return Response(status=201)

    def delete(self,request,pk):
        obj= self.model.objects.filter(pk=pk).first()
        obj.delete()
        return Response("Note deleted",status=200)

    def put(self,request,pk):
        obj= self.model.objects.filter(pk=pk).first()
        s = self.serializer_class(data=request.data,instance=obj,partial=True)
        if s.is_valid():
            s.save()
        return Response(s.data,status=200)


    

