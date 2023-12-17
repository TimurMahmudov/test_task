from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50,
                             verbose_name="Наименование")
    super_category = models.ForeignKey('self',
                                       on_delete=models.PROTECT,
                                       verbose_name="Надкатегория",
                                       related_name="subs",
                                       null=True,
                                       blank=True)

    def __str__(self):
        if self.super_category:
            return "{} - {}".format(self.super_category.title, self.title)
        return self.title

    def count_subs(self):
        return self.subs.count()

    count_subs.short_description = "Кол-во вложенных категорий"

    class Meta:
        ordering = ("super_category__title", "title")
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
