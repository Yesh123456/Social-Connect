from django.views.generic import TemplateView

class TestPage(TemplateView):
	template_name='test.html'

class OutPage(TemplateView):
	template_name='out.html'

class Home_page(TemplateView):
	template_name = 'index.html'