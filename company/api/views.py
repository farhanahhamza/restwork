from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from.models import employees,managers,Employee
from rest_framework.views import APIView
from .serializers import empSerializers,ManagerModelSer

# Create your views here.

# #function based view
# @api_view(['GET'])
# def employeelist(request):
#     return Response(data=employees)

#class based view
class EmployeeView(APIView):
    def get(self,request,*args,**kwargs):
        emp=employees
        if 'dept' in request.query_params:
            dp=request.query_params.get('dept')
            emp=[i for i in emp if i['dept']==dp]
        if 'limit' in request.query_params:
            lm=request.query_params.get('limit')
            emp=emp[0:int(lm)]
        return Response(data=employees)
    def post(self,request):
        data=request.data
        employees.append(data)
        return Response(data=employees)
    
class EmployeeSpecific(APIView):
    def get(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        res=[i for i in employees if i["id"]==eid].pop()
        return Response(data=res)
    def delete(self,request,*args,**kwargs):
        eid=kwargs.get("id")
        res=[i for i in employees if i["id"]==eid].pop()
        employees.remove(res)
        return Response(data=employees)
    def put(self,request,args,*kwargs):
        eid=kwargs.get("id")
        res=[i for i in employees if i["id"]==eid].pop()
        data=request.data
        res.update(data)
        return Response(data=employees)


class EmpView(APIView):
    def post(self,request):
         ser=empSerializers(data=request.data)
         if ser.is_valid():
           nm=ser.validated_data.get('name')
           dp=ser.validated_data.get('dept')
           qua=ser.validated_data.get('qualiffic')
           Employee.objects.create(name=nm,dept=dp,qualiffic=qua)
         return Response({"mesg":"Created"})
    def get(self,request):
        emp=Employee.objects.all()
        dser=empSerializers(emp,many=True)
        return Response(data=dser.data)
    
class EmpspecificView(APIView):
    def get(self,request,args,*kwrgs):
        eid=kwrgs.get("id")
        emp=Employee.objects.get(id=eid)
        des=empSerializers(emp)
        return Response(data=des.data)
    def delete(self,request,**kwrgs):
        eid=kwrgs.get("id")
        Employee.objects.filter(id=eid).delete()
        # emp.delete()
        return Response({"msg":"Deleted"})
    def put(self,request,**kwrgs):
        eid=kwrgs.get("id")
        emp=Employee.objects.get(id=eid)
        ser=empSerializers(data=request.data)
        if ser.is_valid():
            nm=ser.validated_data.get('name')
            dp=ser.validated_data.get('dept')
            qua=ser.validated_data.get('qualific')
            emp.name=nm
            emp.dept=dp
            emp.qualiffic=qua
            emp.save()
            return Response({"msg":"Updated"})
        return Response({"msg":ser.errors})

from rest_framework import status

class ManagerView(APIView):
    def post(self,request):
        ser=ManagerModelSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        return Response({"msg":"Failed"})
    def get(self,request):
        man=managers.objects.all()
        if 'exp_gt' in request.query_params:
            exp=request.query_params.get('exp_gt')
            man=man.filter(experience_gt=exp)
        if 'limit' in request.query_params:
            lm=request.query_params.get('limit')
        dser=ManagerModelSer(man,many=True)
        return Response(data=dser.data)

class SpecificManagerView(APIView):
    def get(self,request,*kwargs):
        try:
            mid=kwargs.get("id")
            man=managers.objects.get(id=mid)
            dser=ManagerModelSer(man)
            return Response(data=dser.data)
        except:
            return Response({"msg":"invalid ID"},status=status.HTTP_406_NOT_ACCEPTABLE)
    def delete(self,request,*kwargs):
        mid=kwargs.get("id")
        man=managers.objects.get(id=mid)
        man.delete()
        return Response({"msg":"Deleted"})
    def put(self,request,*kwargs):
        mid=kwargs.get("id")
        man=managers.objects.get(id=mid)
        ser=ManagerModelSer(data=request.data,instance=man)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"updated"})
        return Response({"msg":"Failed!!"})
    
from rest_framework.viewsets import Viewset,ModelViewSet
    
class ManagerViewSet(Viewset):
    def retrieve(self,rtequest,*args,**kwargs):
        mid=kwargs.get('pk')
        man=managers.objects.get(id=mid)
        dser=ManagerModelSer(man)
        return Response(data=dser.data)
    def list(self,request,*args,**kwargs):
        man=managers.objects.all()
        dser=ManagerModelSer(man,many=True)
        return Response(data=dser.data)
    def create(self,request):
        ser=ManagerModelSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Created"},status=status.HTTP_201_CREATED)
        return Response({"msg":"Failed"},status=status.HTTP_404_NOT_FOUND)
    def update(self,request,*args,**kwargs):
        mid=kwargs.get('pk')
        man=managers.objects.get(id=mid)
        ser=ManagerModelSer(data=request.data,instance=man)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"Updated"})
        return Response({"msg":"Failed"})
    def destroy(self,request,**kwrags):
        mid=kwrags.get('pk')
        man=managers.objects.get(id=mid)
        man.delete()
        return Response({"msg":"Deleted"})
    
class ManagerMViewSet(ModelViewSet):
    serializer_class=ManagerModelSer
    queryset=managers.objects.all()