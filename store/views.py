from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Page

# Listado de páginas con búsqueda
class PageListView(ListView):
    model = Page
    template_name = "store/page_list.html"
    context_object_name = "pages"

    def get_queryset(self):
        qs = super().get_queryset()
        self.q = self.request.GET.get("q", "").strip()
        if self.q:
            qs = qs.filter(
                Q(title__icontains=self.q) |
                Q(subtitle__icontains=self.q) |
                Q(content__icontains=self.q)
            ).distinct()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = getattr(self, "q", "")
        if not context["pages"]:
            if context["q"]:
                context["no_pages"] = f"No se encontraron páginas que coincidan con '{context['q']}'."
            else:
                context["no_pages"] = "No hay páginas aún."
        return context

# Detalle de una página
class PageDetailView(DetailView):
    model = Page
    template_name = "store/page_detail.html"
    context_object_name = "page"

# Crear nueva página
class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    fields = ["title", "subtitle", "content", "image"]
    template_name = "store/page_form.html"
    success_url = reverse_lazy("store:page_list")

# Editar página existente
class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    fields = ["title", "subtitle", "content", "image"]
    template_name = "store/page_form.html"
    success_url = reverse_lazy("store:page_list")

# Eliminar página
class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = "store/page_confirm_delete.html"
    success_url = reverse_lazy("store:page_list")
