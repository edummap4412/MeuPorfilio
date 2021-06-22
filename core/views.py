
#from django.views.generic import TemplateView
from .models import Servico, Equipe, Recursos
from django.views.generic import FormView
from .forms import ContatoForm
from django.urls import reverse_lazy
from django.contrib import messages
"""Aqui eu fiz uma for para serviços (entrontra-se la services.html)
Utiliando Servico.objcts.all() feito isso os icones e as descricoes estao corretas , de acordo com o Bando de dados.
Em seguida para deixar o site mais vivo eu use :Servico.objects.order_by('?').all() para ordenar os icones de forma aleatoria
toda vez que atualizar .
OBS : Lá no services.html  exclui os as colunas de cada serviço deixando somente uma para usa-la para 
"for"  ondde somente com ela eu posso listar os serviços
    E POSSIVEL FAZER NO CAMPO 'EQUIPE' 
--------CRIANDO FORMULARIOS--------
Depois que criei o formulario para envio de email no forms . preciso mudar a Herança dde IndexView
de TemplateView para FormView , porque a campo 'CONTATO" esta em Index tambem.   
    
    """


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['equipe'] = Equipe.objects.order_by('?').all()
        context['recursos'] = Recursos.objects.order_by('?').all()

        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o Email')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)



