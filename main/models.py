from django.db import models

class Recipes(models.Model):
    pretitele = models.CharField('Тип блюда', max_length=50)
    title = models.CharField('Название блюда',max_length=50)
    timecook = models.CharField('время приготовления',max_length=50)
    recipe = models.TextField('рецепт')
    dishing = models.ImageField('картинка',upload_to='recipes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'