from django.contrib import admin

from .models import Article, Tag, TagArticle
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class TagArticleInlineInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main = False
        for form in self.forms:
            data = form.cleaned_data
            if not is_main and 'is_main' in data.keys() and data['is_main']:
                is_main = True
            elif is_main and 'is_main' in data.keys() and data['is_main']:
                raise ValidationError('Должен быть только один основной раздел')
        if not is_main:
            raise ValidationError('Выбирете 1 основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class TagArticleInline(admin.TabularInline):
    model = TagArticle
    formset = TagArticleInlineInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        TagArticleInline
        ]
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

