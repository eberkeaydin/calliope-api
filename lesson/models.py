from django.db import models
from django.utils.translation import gettext_lazy as _

'''
Category
    -id
    -category_name

Lesson
    -id
    -lesson_title
    -category(fk)
    -difficulty
    -date_created

Content
    -id
    -youtube_url
    -content_text
    -lesson(fk)


'''

class Category(models.Model):
    
    category_name = models.CharField(max_length=255, default="Has no category", verbose_name=_("Category"))
    
    def __str__(self):
        return self.category_name
    
class Lesson(models.Model):
    
    class Meta:
        verbose_name = _("Lesson")
        verbose_name_plural = _("Lessons")
        ordering = ['id']
    
    SCALE = (
        (1, _('Beginner')),
        (2, _('Intermediate')),
        (3, _('Advance'))
    )
    
    lesson_title = models.CharField(max_length=255, blank=False, null=False, verbose_name=_("Lesson Title"))
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("Lesson Category"))
    
    difficulty = models.IntegerField(choices=SCALE, default=1, verbose_name=_("Difficulty"))
    
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.lesson_title
    
class Content(models.Model):
        
    class Meta:
        verbose_name = _("Content")
        verbose_name_plural = _("Contents")
        ordering = ['id']
            
        
    related_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name=_("Related Lesson"))
        
    video_url = models.URLField(max_length=512, verbose_name=_("Video URL"))
        
    content_header = models.CharField(max_length=255, verbose_name=_("Content Header"))
        
    content_text = models.TextField(verbose_name=_("Content Text"))

    def __str__(self):
        return self.content_header
    
    
    