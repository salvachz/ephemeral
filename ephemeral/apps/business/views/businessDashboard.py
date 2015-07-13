from apps.generic.views import EphemeralTemplateView
from django.http import HttpResponseRedirect
from datetime import datetime
from apps.business.models import Carrinho,Compra, Visita
import simplejson

class BusinessDashboardView(EphemeralTemplateView):
    template_name = "business/businessDashboard.html"

    def get(self, request, **kwargs):
        kwargs['car_to_go'] = self.__cart_by_day()
        kwargs['buy_to_go'] = self.__buy_by_day()
        kwargs['visit_to_go'] = self.__visit_by_day()
        return EphemeralTemplateView.get(self, request,**kwargs)

    def __cart_by_day(self):
        car_to_go = {}
        carrinhos = Carrinho.objects.all()
        for carrinho in carrinhos:
            if carrinho.data_str not in car_to_go:
                car_to_go[carrinho.data_str] = 1
            else:
                car_to_go[carrinho.data_str] = car_to_go[carrinho.data_str] + 1
        car_to_go2 = {}
        for data_str in car_to_go:
            ndata = datetime.strptime(data_str, "%d/%m/%Y")
            car_to_go2[ndata] = car_to_go[data_str]
        return car_to_go2

    def __buy_by_day(self):
        buy_to_go = {}
        compras = Compra.objects.all()
        for compra in compras:
            if compra.data_str not in buy_to_go:
                buy_to_go[compra.data_str] = 1
            else:
                buy_to_go[compra.data_str] = buy_to_go[compra.data_str] + 1
        buy_to_go2 = {}
        for data_str in buy_to_go:
            ndata = datetime.strptime(data_str, "%d/%m/%Y")
            buy_to_go2[ndata] = buy_to_go[data_str]
        return buy_to_go2

    def __visit_by_day(self):
        visit_to_go = {}
        visits = Visita.objects.all()
        for visit in visits:
            if visit.data_str not in visit_to_go:
                visit_to_go[visit.data_str] = 1
            else:
                visit_to_go[visit.data_str] = visit_to_go[visit.data_str] + 1
        visit_to_go2 = {}
        for data_str in visit_to_go:
            ndata = datetime.strptime(data_str, "%d/%m/%Y")
            visit_to_go2[ndata] = visit_to_go[data_str]
        return visit_to_go2
