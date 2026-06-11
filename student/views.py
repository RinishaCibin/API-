from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from student.serializers import AssignmentSerializer,TodoSerializer,TeacherSerializer
from student.models import Assignments,Todo,Teacher
from rest_framework import status
# from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.viewsets import ViewSet

students=[
    {"id":1,"name":"Amala","age":20,"batch":"Bsc CS"},
    {"id":2,"name":"Vimala","age":22,"batch":"BCA"},
    {"id":3,"name":"Kamala","age":19,"batch":"Bsc CS"},
    {"id":4,"name":"Amal","age":21,"batch":"BCA"}
]

# Create your views here.
@api_view(['GET'])
def firstRequest(request):
    return Response(data={"msg":"First request hit"})

@api_view(["POST"])
def postExample(request):
    print(request.data.get('username'))
    print(request.data.get('password'))
    return Response(data={"msg":"POST Request"})

@api_view(["PUT"])
def putExample(request):
    return Response(data={"msg":"First PUT Request"})


class StudentApiView(APIView):
    def get(self,request):
        return Response(data=students)
    def post(self,request):
        print(request.data)
        students.append(request.data)
        return Response(data=students)
    
class SpecificStudentView(APIView):
    def get(self,request,**kwargs):
        sid=kwargs.get('id')
        studnt=list(filter(lambda item:item['id']==sid,students)).pop()
        print(studnt)
        return Response(data=studnt)
    
    def put(self,request,**kwargs):
        print(kwargs.get('id'))
        print(request.data)
        global students
        sid=kwargs.get('id')
        students=list(filter(lambda item:item['id']!=sid,students))
        students.append(request.data)
        return Response(data=students)
    
    def delete(self,request,**kwargs):
        global students
        sid=kwargs.get('id')
        students=list(filter(lambda item:item['id']!=sid,students))
        return Response(data=students)
    
class AssignmentView(APIView):
    def post(self,request):
      print(request.data)
      dser=AssignmentSerializer(data=request.data)
      if dser.is_valid():
          title=dser.validated_data.get('title')
          desc=dser.validated_data.get('description')
          submission=dser.validated_data.get('submission_date')
          Assignments.objects.create(title=title,description=desc,submission_date=submission)
          return Response(data={"msg":"Success"},status=status.HTTP_201_CREATED)
      return Response(data={"msg":dser.errors},status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        data=Assignments.objects.all()
        ser=AssignmentSerializer(data,many=True)
        return Response(data=ser.data,status=status.HTTP_200_OK)
    
class SpecificAssignmentView(APIView):
    def get(self,request,**kwargs):
        aid=kwargs.get('pk')
        assignment=Assignments.objects.get(id=aid)
        ser=AssignmentSerializer(assignment)
        return Response(data=ser.data)
    def delete(self,request,**kwargs):
        aid=kwargs.get('pk')
        Assignments.objects.get(id=aid).delete()
        return Response(data={"msg":"Deleted!"})
    def put(self,request,**kwargs):
        aid=kwargs.get('pk')
        assignment=Assignments.objects.get(id=aid)
        dser=AssignmentSerializer(data=request.data)
        if dser.is_valid():
            title=dser.validated_data.get('title')
            desc=dser.validated_data.get('description')
            submission=dser.validated_data.get('submission_date')
            assignment.title=title
            assignment.description=desc
            assignment.submission_date=submission
            assignment.save()
            return Response(data={"msg":"Updated"},status=status.HTTP_200_OK)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    
# TOD CURD OPERATIONS #

# class TodoView(APIView):
#     def post(self,request):
#         print(request.data)
#         tser=TodoSerializer(data=request.data)
#         if tser.is_valid():
#             title=tser.validated_data.get('title')
#             descri=tser.validated_data.get('description')
#             subj=tser.validated_data.get('subject')
#             Todo.objects.create(title=title,description=descri,subject=subj)
#             return Response(data={"msg":"Success"},status=status.HTTP_201_CREATED)
#         return Response(data={"msg":tser.errors},status=status.HTTP_400_BAD_REQUEST)
    
#     def get(self,request):
#         data=Todo.objects.all()
#         todoseri=TodoSerializer(data,many=True)
#         return Response(data=todoseri.data,status=status.HTTP_200_OK)
    
# class SpecificTodoView(APIView):
#     def get(self,request,**kwargs):
#         todoid=kwargs.get('pk')
#         td=Todo.objects.get(id=todoid)
#         todoseri=TodoSerializer(td)
#         return Response(data=todoseri.data)
#     def delete(self,request,**kwargs):
#         todoid=kwargs.get('pk')
#         Todo.objects.get(id=todoid).delete()
#         return Response(data={"msg":"Deleted!"})
#     def put(self,request,**kwargs):
#         todoid=kwargs.get('pk')
#         td=Todo.objects.get(id=todoid)
#         tser=TodoSerializer(data=request.data)
#         if tser.is_valid():
#             title=tser.validated_data.get('title')
#             desc=tser.validated_data.get('description')
#             subj=tser.validated_data.get('subject')
#             td.title=title
#             td.description=desc
#             td.subject=subj
#             td.save()
#             return Response(data={"msg":"Updated"},status=status.HTTP_200_OK)
#         return Response(data=tser.errors,status=status.HTTP_400_BAD_REQUEST)

class TodoView(APIView):
    def get(self,request):
        todos=Todo.objects.all()
        ser=TodoSerializer(todos,many=True)
        return Response(data=ser.data)
    def post(self,request):
        dser=TodoSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class SpecificTodoView(APIView):
    def get(self,request,**kwargs):
        tid=kwargs.get('pk')
        todo=Todo.objects.get(id=tid)
        ser=TodoSerializer(todo)
        return Response(data=ser.data)
    def delete(self,request,**kwargs):
        todo=Todo.objects.get(id=kwargs.get('pk')).delete()
        return Response(data={"msg":"DELETED"})
    def put(self,request,**kwargs):
        todo=Todo.objects.get(id=kwargs.get('pk'))
        dser=TodoSerializer(todo,data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    
class TeacherView(APIView):
    def get(self,requrst):
        teach=Teacher.objects.all()
        tser=TeacherSerializer(teach,many=True)
        return Response(data=tser.data)
    
    def post(self,request):
        dser=TeacherSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class TeachersViewSet(ViewSet):
    def list(self,request):
        teach=Teacher.objects.all()
        tser=TeacherSerializer(teach,many=True)
        return Response(data=tser.data)
    def create(self,request):
        dser=TeacherSerializer(data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data,status=status.HTTP_201_CREATED)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk=None):
        teach=Teacher.objects.get(id=pk)
        dser=TeacherSerializer(teach,data=request.data)
        if dser.is_valid():
            dser.save()
            return Response(data=dser.data)
        return Response(data=dser.errors,status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self,request,pk=None):
        teach=Teacher.objects.get(id=pk)
        ser=TeacherSerializer(teach)
        return Response(data=ser.data)
    def destroy(self,request,pk=None):
        Teacher.objects.get(id=pk).delete()
        return Response(data={"msg":"Deleted"})





    
            

            


           





    

    


    
    
    
       
       



