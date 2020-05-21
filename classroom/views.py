from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView, DetailView,DeleteView,View
from .models import Chaptercreate,Subjectcreate,Assignment,Video, Assignmentmain,Chapterass, Asspdf, Studentsolution_ass,Video_ass,Video_seen,Quiz,Question,Answer,Dashboard,Quiz_ass,Question_ass,Answer_ass,Dashboard_ass
from datetime import datetime
from .forms import AssignmentForm, AssignmentsolutionForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin 
# Create your views here.

@login_required
def Lessons(request):
     subjects=Subjectcreate.objects.all()
     
     item = get_object_or_404(Subjectcreate, pk=1)
     chapter=Chaptercreate.objects.filter(subject=item).count()
     assignment=Assignment.objects.filter(subject=item).count()
     videos=Video.objects.filter(subject=item).count()
     quizzes=Quiz.objects.filter(subject=item).count()

     print(chapter)
         
     return render(request,'classroom/subjects.html',{
        'subjects' :subjects,
        'chapter':chapter,
        'assignment':assignment,
        'videos': videos,
        'quizzes':quizzes
     })

@login_required
def subject(request,pk):
   item = get_object_or_404(Subjectcreate, pk=pk)
   print(item)
   subject=Chaptercreate.objects.filter(subject=item)
   assignment=Assignment.objects.filter(subject=item)
   videos=Video.objects.filter(subject=item)
   quizzes=Quiz.objects.filter(subject=item)

   print(assignment)
   context={
           'item':item,
           'subject': subject,
           'assignment':assignment,
           'videos': videos,
           'quizzes':quizzes
           }
   return render(request,'classroom/subjectcreate_detail.html',context)

@login_required
def solution_assignment(request,pk):
    assignment = get_object_or_404(Assignment, pk=pk)
    if request.method=='POST':
        form=AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user= request.user
            form.instance.ass= assignment
            form.save()
            return redirect('detail', assignment.subject.pk )
    else:
        form = AssignmentForm()
    return render(request,'classroom/upload_Assignment.html',{
        'form':form
        })

@login_required
def showvideo(request):

    videofile= Video.objects.all()

    
    print(videofile)
    
    context= {'videofile': videofile,
              
              }
        
    return render(request, 'classroom/videos.html', context)

class Videodetail(LoginRequiredMixin,DetailView):
    model=Video
    template_name='classroom/videos.html'


@login_required
def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    questions =Question.objects.filter(quiz__id=pk)
    answers = Answer.objects.filter(question__quiz__id=pk)
    student = request.user
    
    return render(request, 'classroom/take_quiz_form.html', {
        'quiz': quiz,
        'questions': questions,
        'answers':answers
        
    })

@login_required
def result(request,pk):
    answers = Answer.objects.filter(question__quiz__id=pk)
    quiz = get_object_or_404(Quiz, pk=pk)
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        print(datas)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:

            try:
               
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        #for q in qid:
         #   ans.append((Questions.objects.get(id = q)).answer)

        for answer in answers:
            
            if answer.is_correct:

                ans.append(answer.text)
        print(ans)       
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1

        print(score)
        eff = (score/total)*100
        student = request.user
        Dashboard.objects.create(student=student, quiz=quiz, score=score, total=total)

   
    return render(request,
        'classroom/result.html',
        {'score':score,
        'eff':eff,
        'total':total,

        })

@login_required
def Assignments(request):
     subjects=Assignmentmain.objects.all()

     time=datetime.now()
     print(time)
     

         
     return render(request,'classroom/Assignment_main.html',{
        'subjects' :subjects,
        'time':time

     })

@login_required
def pdf(request,pk):
   item = get_object_or_404(Assignmentmain, pk=pk)
   ass = get_object_or_404(Asspdf, pk=pk)
   print(item)
   subject=Chapterass.objects.filter(subject=item)
   assignment=Asspdf.objects.filter(subject=item)
   assignment_sol=Studentsolution_ass.objects.filter(subject=item,  user=request.user)
   videos=Video_ass.objects.filter(subject=item)
   quizzes=Quiz_ass.objects.filter(subject=item)
   count_sol=Studentsolution_ass.objects.filter(subject=item,  user=request.user, is_completed=True).count()
   count_ass=Asspdf.objects.filter(subject=item).count()
   count_quiz=Quiz_ass.objects.filter(subject=item).count()
   count_dashboard=Dashboard_ass.objects.filter(subject=item,  student=request.user, is_completed=True).count()
   percent=((count_sol+count_dashboard)/(count_ass+count_quiz))*100
   print(count_quiz)
   print(count_ass)
   print(count_dashboard)
  # assignment_sol=Studentsolution_ass.objects.filter(ass__id=pk, user=request.user)
   print(assignment_sol)
   print(assignment)
   if percent == 100:
       
           obj_instance = Assignmentmain.objects.get(subject=item)
           obj_instance.user=request.user
           obj_instance.is_completed=True
           obj_instance.save(update_fields=['user','is_completed'])


       

   context={
           'item':item,
           'subject': subject,
           'assignment':assignment,
           'assignment_sol':assignment_sol,
           'count_sol':count_sol,
           'count_ass':count_ass,
           'percent':percent,
           'videos': videos,
           'quizzes':quizzes
           
           }


   return render(request,'classroom/assignment_detail.html',context)

@login_required
def solution_assignment_student(request,pk):
 
 assignment = get_object_or_404(Asspdf, pk=pk)
 if request.method=='POST':
     form=AssignmentsolutionForm(request.POST, request.FILES)
     if form.is_valid():
         form.instance.subject= assignment.subject
         form.instance.user= request.user
         form.instance.ass= assignment
         form.instance.is_completed=True
         form.save()
         return redirect('detail_ass', assignment.subject.pk )
 else:
     form = AssignmentsolutionForm()
 return render(request,'classroom/upload_solution_Assignment.html',{
     'form':form
     })

class Video_assdetail(LoginRequiredMixin,DetailView):
    model=Video_ass
    template_name='classroom/video_ass.html'

@login_required
def Videocomplete(request,pk):
    user = request.user
    video = get_object_or_404(Video_ass, pk=pk)
    Video_seen.objects.create(video=video, user=user, is_completed=True)
    return redirect(request,'assignment')


@login_required
def take_quiz_ass(request, pk):
    quiz = get_object_or_404(Quiz_ass, pk=pk)
    questions =Question_ass.objects.filter(quiz__id=pk)
    answers = Answer_ass.objects.filter(question__quiz__id=pk)
    student = request.user
    
    
    return render(request, 'classroom/take_quiz_ass_form.html', {
        'quiz': quiz,
        'questions': questions,
        'answers':answers
        
    })

@login_required
def result_quiz_ass(request,pk):
    answers = Answer_ass.objects.filter(question__quiz__id=pk)
    quiz = get_object_or_404(Quiz_ass, pk=pk)
   
    print("result page")
    if request.method == 'POST':
        data = request.POST
        datas = dict(data)
        print(datas)
        qid = []
        qans = []
        ans = []
        score = 0
        for key in datas:

            try:
               
                qid.append(int(key))
                qans.append(datas[key][0])
            except:
                print("Csrf")
        #for q in qid:
         #   ans.append((Questions.objects.get(id = q)).answer)

        for answer in answers:
            
            if answer.is_correct:

                ans.append(answer.text)
        print(ans)       
        total = len(ans)
        for i in range(total):
            if ans[i] == qans[i]:
                score += 1

        print(score)
        eff = (score/total)*100
        student = request.user
        is_completed=True
        Dashboard_ass.objects.create(subject=quiz.subject,student=student, quiz=quiz, score=score, total=total, is_completed=is_completed)

   
    return render(request,
        'classroom/result_quiz_ass.html',
        {'score':score,
        'eff':eff,
        'total':total,

        })
