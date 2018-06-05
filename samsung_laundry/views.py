from django.shortcuts import get_object_or_404,render
import datetime
from .models import S_IF,AC_IF,Item,Deal_IF
from django.views import generic
import logging
logger = logging.getLogger(__name__)
class search(generic.ListView):
    template_name = 'samsung_laundry/search.html'
    context_object_name = "ac_if"
    def get_queryset(self):
        return AC_IF.objects.all()

def search_id(request):
    start_date1 = datetime.date(2018, 4, 26)
    end_date1 = datetime.date(2018, 5, 31)
    try:
        selected_deal=request.POST['searchid']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
    except(KeyError,Deal_IF.DoesNotExist):
        return render(request,'samsung_laundry/search.html',{
            'ac_if':AC_IF.objects.all(),
            'no_data':'거래 내역이 없습니다.',
        })
    else:
        return render(request,'samsung_laundry/search.html',{
            'ac_if':AC_IF.objects.all(),
            'deal_IF':Deal_IF.objects.filter(AC_ID=selected_deal).filter(DEAL_DATE__range=(start_date,end_date)),
        })
    # return HttpResponseRedirect(reverse('samsung_laundry:search'))

def main(request):
    return render(request,'samsung_laundry/main.html')
