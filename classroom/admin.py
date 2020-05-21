from django.contrib import admin

# Register your models here.
from .models import Subjectcreate,Chaptercreate,Assignment,Studentsolution, Video, Assignmentmain,Chapterass, Asspdf, Studentsolution_ass, Video_ass,Video_seen
from .models import Quiz,Question,Answer,Dashboard,Quiz_ass,Question_ass,Answer_ass,Dashboard_ass
admin.site.register(Subjectcreate)
admin.site.register(Chaptercreate)
admin.site.register(Assignment)
admin.site.register(Studentsolution)
admin.site.register(Video)
admin.site.register(Assignmentmain)
admin.site.register(Chapterass)
admin.site.register(Asspdf)
admin.site.register(Studentsolution_ass)
admin.site.register(Video_ass)
admin.site.register(Video_seen)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Dashboard)
admin.site.register(Quiz_ass)
admin.site.register(Question_ass)
admin.site.register(Answer_ass)
admin.site.register(Dashboard_ass)

