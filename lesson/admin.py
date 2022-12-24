from django.contrib import admin
from .models import Category, Lesson, Content

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'category_name',
    ]
    
@admin.register(Lesson)

class LessonAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'lesson_title',
        'category',
        'difficulty',
        'date_created',
        'is_active'
    ]
    
@admin.register(Content)

class LessonAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'related_lesson',
        'video_url',
        'content_header',
        'content_text'
    ]