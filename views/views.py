from django.views import View
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect,JsonResponse,HttpResponseBadRequest
class BaseView(View):
    template_name=None
    def get(self,request,*args,**kwargs):
        if hasattr(self,'prepare'):
            getattr(self,'prepare')(request,*args,**kwargs)
        if hasattr(self,'handle_cookie_request'):
            getattr(self,'handle_cookie_request')(request,*args,**kwargs)
        response=render(request,self.template_name,self.get_context(request))
        if hasattr(self,'handle_cookie_response'):
            getattr(self,'handle_cookie_response')(response,*args,**kwargs)
        return response

    def get_context(self, request):
        context={}
        context.update(self.get_extra_context(request))
        return context

    def get_extra_context(self, request):
        return {}

class BaseRedirectView(View):
    redirect_url=None
    def dispatch(self, request, *args, **kwargs):
        if hasattr(self,'handle'):
            getattr(self,'handle')(request,*args,**kwargs)
        return HttpResponseRedirect(self.redirect_url)
class OperateView(View):
    form_cls = None
    def post(self,request,*args,**kwargs):
        form = self.form_cls(request.POST.dict())

        if form.is_valid():
            handler=request.POST.get('type','')
            if hasattr(self,handler):
                return JsonResponse(getattr(self,handler)(request,**form.cleaned_data))
            else:
                return HttpResponseBadRequest("type does not give")
        else:
            return JsonResponse({'errorcode':-300,'errormsg':form.errors})