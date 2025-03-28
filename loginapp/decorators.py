from django.shortcuts import render,redirect
def allifmaal_admin_supperuser(allif_param_func):
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        if usernme.is_superuser==True:
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func

def logged_in_user_can_add(allif_param_func):
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        usr_can_view=usernme.can_add
        if usr_can_view==True:
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func

def logged_in_user_can_view(allif_param_func):
    
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        usr_can_view=usernme.can_view
        if usr_can_view==True:
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func

def logged_in_user_can_edit(allif_param_func):
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        usr_can_view=usernme.can_edit
        if usr_can_view==True:
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func

def logged_in_user_can_delete(allif_param_func):
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        usr_can_view=usernme.can_delete
        if usr_can_view==True:
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func

def logged_in_user_is_admin(allif_param_func):
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        if usernme.user_category=="admin":
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func
def logged_in_user_is_owner_ceo(allif_param_func):
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        if usernme.user_category=="owner" or usernme.user_category=="ceo" or usernme.is_superuser==True:
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func
def logged_in_user_is_staff(allif_param_func):
    def allif_wrapper_func(request,*args,**kwargs):
        usernme=request.user
        if usernme.user_category=="staff":
            return allif_param_func(request,*args,**kwargs)
        else:
            return render(request,'loginapp/permissions/no_permission.html')
    return allif_wrapper_func
