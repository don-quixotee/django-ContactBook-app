from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


from contacts.models import Contact
from contacts.froms import ContactForm


# Create your views here.


def listView(request):
    contact = Contact.objects.all
    context = {'contact':contact,}
    return render(request, 'contacts/index.html', context)


def createContactView(request, id=None):

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
            firstname = form.cleaned_data.get('first_name')
            messages.success(request, 'contact  name : {} has been created successfully !'.format(firstname))
            return redirect('/')
        

    
    context = {'form':form}
    return render(request, 'contacts/contact_form.html', context)


def update_contact(request, id):
    contact = Contact.objects.get(id=id)
    form = ContactForm(instance=contact)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('first_name')
            messages.success(request, 'contact name :{} has beed update successfully !'.format(firstname))
            return redirect('/')
        else:
            messages.warning(request, "Please enter valid inputs !")
            return render(request, 'contacts/contact_update.html', context={'form':form})


    return render(request, 'contacts/contact_update.html', context={'form':form})

def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id )
    if request.method == 'POST':
        contact.delete()
        messages.success(request, "contact Deleted !")
        return redirect('/')
    return render(request, 'contacts/delete.html', context={'contact':contact})

