from django.shortcuts import render
from django.views.generic import TemplateView
from site_app.models import FooterLink

import blog_app.views
from blog_app.models import PostModel


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_page'] = 'home'
        context['posts'] = PostModel.objects.all()
        context['recent_post'] = context['posts'][:len(context['posts'])-4:-1]
        return context

def site_footer(request):
    footer_links: FooterLink = FooterLink.objects.all()
    return render(request, "shared/includes/side_footer.html", {"footer_links":footer_links})