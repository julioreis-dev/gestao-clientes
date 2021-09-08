from django.http import HttpResponse
from django.shortcuts import render
from clientes.models import Person


@login_required
def persons_list(request):
    persons = Person.objects.all()

    return render(
        request, 'person.html', {'persons': persons})


@login_required
def persons_new(request):
    if not request.user.has_perm('vendas.add_person'):
        return HttpResponse('Nao autorizado')
    elif not request.user.is_superuser:
        return HttpResponse('Nao e superusuario')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect('person_list')

    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):
    model = Person

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso', False)

        if not primeiro_acesso:
            context['message'] = 'Seja bem vindo ao seu primeiro acesso hoje'
            self.request.session['primeiro_acesso'] = True
        else:
            context['message'] = 'Voce ja acessou hoje'

        return context

class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        return Person.objects.select_related('doc').get(id=pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['vendas'] = Venda.objects.filter(
            pessoa_id=self.object.id)
        return context


class PersonCreate(LoginRequiredMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = '/vendas/person_list'


class PersonUpdate(LoginRequiredMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = ('vendas.deletar_clientes',)

    model = Person
    # success_url = reverse_lazy('person_list_cbv')

    def get_success_url(self):
        return reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maca', 'Limao', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')


def api(request):
    a = {'nome': 'Gregory', 'idade': 29, 'salario': 500}
    mensagem = {'mensagem': 'erro xyz'}
    lista = [1, 2, 3]

    produto = Produto.objects.last()

    b = model_to_dict(produto)

    l = []

    produtos = Produto.objects.all()

    for produto in produtos:
        l.append(model_to_dict(produto))

    return JsonResponse(l, status=200, safe=False)


class APICBV(View):
    def get(self, request):
        data = {'nome': 'Gregory'}

        produto = Produto.objects.last()
        b = model_to_dict(produto)

        l = []
        produtos = Produto.objects.all()

        for produto in produtos:
            l.append(model_to_dict(produto))

        return JsonResponse(l, safe=False)

    def post(self):
        pass
