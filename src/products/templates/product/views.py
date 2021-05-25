from django.shortcuts import render
from django.views.generic import DetailView,ListView
from django.contrib.postgres.search import TrigramDistance
from django.db.models import Q
from products.models import category
from souq.models import Souq
from jumia.models import Jumia
from noon.models import Noon

from django.core.paginator import Paginator



# UPDATE jumia SET manufacture = LOWER(manufacture);

# from django.views.generic import TemplateView
# from chartjs.views.lines import BaseLineChartView


# class LineChartJSONView(BaseLineChartView):
#     def get_labels(self):
#         """Return 7 labels for the x-axis."""
#         return ["January", "February", "March", "April", "May", "June", "July"]

#     def get_providers(self):
#         """Return names of datasets."""
#         return ["Central", "Eastside", "Westside"]

#     def get_data(self):
#         """Return 3 datasets to plot."""

#         return [[75, 44, 92, 11, 44, 95, 35],
#                 [41, 92, 18, 3, 73, 87, 92],
#                 [87, 21, 94, 3, 90, 13, 65]]


# line_chart = TemplateView.as_view(template_name='souq/souq_detail.html')
# line_chart_json = LineChartJSONView.as_view()   


class SearchResultsView(ListView):
    model = Souq
    paginate_by = 10
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Souq.objects.filter(
            Q(title__icontains=query)
        )
        return object_list





def is_valid_queryparam(param):
    return param != '' and param is not None


def Product(request):
    qs = Souq.objects.all()
    count = Souq.objects.all().count()
    Categories = category.objects.all().order_by('sweetName')
    Recently_Viewed =Souq.objects.filter()[:50]
    manufacture = request.GET.get('manufacture')
    categorys = request.GET.get('category')
    paginator = Paginator(qs, 50) # Show 50 contacts per page.
    brands= Souq.objects.values('manufacture').distinct().order_by('manufacture')
    obj = Souq.objects.values('rate')
    # print('+++++++++++++++++++++++++++++++++++++=')
    # print(Recently_Viewed)
    if is_valid_queryparam (manufacture) and manufacture != 'Choose...':
        qs = qs.filter(manufacture__icontains=manufacture)
        count = qs.filter(manufacture__icontains=manufacture).count()
        paginator = Paginator(qs, 50) # Show 50 contacts per page.

    if is_valid_queryparam (categorys) and categorys != 'Choose...':
        qs = qs.filter(category__sweetName=categorys)
        count = qs.filter(category__sweetName=categorys).count()
        paginator = Paginator(qs, 50) # Show 50 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'product/jumia_list.html',{
        'page_obj' : page_obj ,
        'Categories' : Categories,
        'brands':brands,
        'count':count,
        'Recently_Viewed':Recently_Viewed,
        'object': obj,
        
         })




class itemDetails(DetailView):
    model = Souq
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        curTitle= self.object.title
        curManufacture=self.object.manufacture
        souq=Souq.objects.annotate(distance=TrigramDistance('title',curTitle),).filter(distance__lte=0.7,manufacture=curManufacture).order_by('distance')[:4]
        noon=Noon.objects.annotate(distance=TrigramDistance('title',curTitle),).filter(distance__lte=0.7,manufacture=curManufacture).order_by('distance')[:4]
        jumia=Jumia.objects.annotate(distance=TrigramDistance('title',curTitle),).filter(distance__lte=0.7,manufacture=curManufacture).order_by('distance')[:4]
        data['noon'] = noon
        data['jumia'] = jumia
        data['souqPlus'] = souq

        return data






