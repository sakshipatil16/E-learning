from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Subjectcreate(models.Model):
    subject = models.CharField(max_length=100)

    def __str__(self):
        return str(self.subject)

class Chaptercreate(models.Model):
    subject = models.ForeignKey(Subjectcreate, on_delete=models.CASCADE, related_name='sub')
    chapter = models.CharField(max_length=100)

    def __str__(self):
        return str(self.chapter)

class Assignment(models.Model):
    subject=models.ForeignKey(Subjectcreate, on_delete=models.CASCADE,related_name='subj')
    item=models.ForeignKey(Chaptercreate, on_delete=models.CASCADE,related_name='assignment')
    pdf= models.FileField(upload_to='assignments/')
    topic = models.CharField(max_length=100)
    description=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return str(self.item.chapter)

class Studentsolution(models.Model):
    ass=models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='sol_assignment')
    pdf= models.FileField(upload_to='assignments/solution')
    created_date = models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)

class Video(models.Model):
    subject=models.ForeignKey(Subjectcreate, on_delete=models.CASCADE,related_name='video')
    item=models.ForeignKey(Chaptercreate, on_delete=models.CASCADE,related_name='chap')
    topic= models.CharField(max_length=255)
    videofile= models.FileField(upload_to='videos/', null=True)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.topic + ": " + str(self.videofile)



class Quiz(models.Model):
    subject= models.ForeignKey(Subjectcreate, on_delete=models.CASCADE,related_name='sub_q')
    item=models.ForeignKey(Chaptercreate, on_delete=models.CASCADE,related_name='chap_q')
    topic = models.CharField(max_length=255)
    def __str__(self):
        return self.topic

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text=models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text
class Answer(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text= models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Dashboard(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='+')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField() 
    def __str__(self):
        return str(self.student)

        


class Assignmentmain(models.Model):
    subject = models.CharField(max_length=100)
    end_date=models.DateTimeField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return str(self.subject)
 
class Chapterass(models.Model):
    subject = models.ForeignKey(Assignmentmain, on_delete=models.CASCADE, related_name='su')
    chapter = models.CharField(max_length=100)

    def __str__(self):
        return str(self.chapter)


class Asspdf(models.Model):
    subject=models.ForeignKey(Assignmentmain, on_delete=models.CASCADE,related_name='sub_ass')
    item=models.ForeignKey(Chapterass, on_delete=models.CASCADE,related_name='ass')
    pdf= models.FileField(upload_to='due_assignments/')
    topic = models.CharField(max_length=100)
    description=models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return str(self.item.chapter)

class Studentsolution_ass(models.Model):
    subject=models.ForeignKey(Assignmentmain, on_delete=models.CASCADE,related_name='sub_a')
    ass=models.ForeignKey(Asspdf, on_delete=models.CASCADE, related_name='sol_ass')
    pdf= models.FileField(upload_to='due_assignments/solution')
    created_date = models.DateTimeField(default=timezone.now)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)

class Video_ass(models.Model):
    subject=models.ForeignKey(Assignmentmain, on_delete=models.CASCADE,related_name='sub_vid')
    item=models.ForeignKey(Chapterass, on_delete=models.CASCADE,related_name='chapt')
    topic= models.CharField(max_length=255)
    videofile= models.FileField(upload_to='ass_videos/', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.topic + ": " + str(self.videofile)

class Video_seen(models.Model):
    video=models.ForeignKey(Video_ass, on_delete=models.CASCADE,related_name='vid_seen')
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)



class Quiz_ass(models.Model):
    subject= models.ForeignKey(Assignmentmain, on_delete=models.CASCADE,related_name='sub_q_ass')
    item=models.ForeignKey(Chapterass, on_delete=models.CASCADE,related_name='chap_q_ass')
    topic = models.CharField(max_length=255)
    time= models.PositiveIntegerField(null=True,blank=True)
    def __str__(self):
        return self.topic

class Question_ass(models.Model):
    quiz = models.ForeignKey(Quiz_ass, on_delete=models.CASCADE, related_name='questions_ass')
    text=models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text
class Answer_ass(models.Model):
    
    question = models.ForeignKey(Question_ass, on_delete=models.CASCADE, related_name='answers_ass')
    text= models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Dashboard_ass(models.Model):
    subject=models.ForeignKey(Assignmentmain, on_delete=models.CASCADE,related_name='sub_assign')
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz_ass, on_delete=models.CASCADE, related_name='q')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    total = models.FloatField() 
    is_completed=models.BooleanField(default=False)
    def __str__(self):
        return str(self.student)

       