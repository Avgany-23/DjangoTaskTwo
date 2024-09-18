from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import TemplateView
import json


class MainView(TemplateView):
    template_name = 'recipes/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        with open('recipes/recipes.json', 'r', encoding='utf-8') as f:
            result = json.load(f)
        dishes = [(i, dish) for i, dish in enumerate(sorted(list(result)), 1)]

        paginator = Paginator(dishes, 5)  # Количество элементов на страницу
        page = self.request.GET.get('page')
        try:
            dishes_page = paginator.page(page)
        except PageNotAnInteger:
            dishes_page = paginator.page(1)
        except EmptyPage:
            dishes_page = paginator.page(paginator.num_pages)
        context['dishes'] = dishes_page
        return context


class Recipe(TemplateView):
    template_name = 'recipes/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dish = kwargs.get('dish')
        count = self.request.GET.get('servings')
        with open('recipes/recipes.json', 'r', encoding='utf-8') as f:
            result = json.load(f)

        return {**context,
                'recipe': result.get(dish),
                'dish': kwargs['dish'],
                'count': count}
