from app.forms import TransactionForm
from django.shortcuts import redirect, render, get_object_or_404
from app.models import *
from django.http import JsonResponse



def index_view(request):
    filters = {
        "name__icontains": request.GET.get("name"),
        "date": request.GET.get("date"),
        "status__name__icontains": request.GET.get("status"),
        "type__name__icontains": request.GET.get("type"),
        "category__name__icontains": request.GET.get("category"),
        "subcategory__name__icontains": request.GET.get("subcategory"),
    }
    filters = {k: v for k, v in filters.items() if v}
    transactions = Transaction.objects.filter(**filters)

    context = {
        "transactions": transactions,
        "statuses": Status.objects.all(),
        "types": TransactionType.objects.all(),
        "categories": Category.objects.all(),
        "subcategories": SubCategory.objects.all(),
    }

    return render(request, "app/index.html", context)


def transaction_create_view(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("app:index")
    else:
        form = TransactionForm()
    return render(
        request, "app/transaction_form.html", {"form": form, "title": "Создание записи"}
    )


def manage_dictionaries_view(request):
    model_map = {
        "Статусы": Status,
        "Типы": TransactionType,
        "Категории": Category,
        "Подкатегории": SubCategory,
    }

    if request.method == "POST":
        model_name = request.POST.get("model")
        name = request.POST.get("name")

        if model_name == "Категории":
            type_id = request.POST.get("type_id")
            if name and type_id:
                Category.objects.create(name=name, type_id=type_id)

        elif model_name == "Подкатегории":
            category_id = request.POST.get("category_id")
            if name and category_id:
                SubCategory.objects.create(name=name, category_id=category_id)

        elif model_name in model_map and name:
            model_map[model_name].objects.create(name=name)

        return redirect("app:manage_dictionaries")

    dictionaries = {
        "Статусы": Status.objects.all(),
        "Типы": TransactionType.objects.all(),
        "Категории": Category.objects.all(),
        "Подкатегории": SubCategory.objects.all(),
    }
    categories = Category.objects.all()
    types = TransactionType.objects.all()

    return render(
        request,
        "app/manage_dictionaries.html",
        {
            "dictionaries": dictionaries,
            "categories": categories,
            "types": types,
        },
    )


def transaction_edit_view(request, uuid):
    instance = Transaction.objects.get(uuid=uuid)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect("app:index")
    else:
        form = TransactionForm(instance=instance)
    return render(
        request,
        "app/transaction_form.html",
        {"form": form, "title": "Редактирование записи"},
    )


def transaction_delete_view(request, uuid):
    transaction = get_object_or_404(Transaction, uuid=uuid)
    transaction.delete()
    return redirect("app:index")

def get_categories_by_type(request):
    type_id = request.GET.get("type")
    categories = Category.objects.filter(type_id=type_id)
    data = [{"id": c.id, "name": c.name} for c in categories]
    return JsonResponse(data, safe=False)

def get_subcategories_by_category(request):
    category_id = request.GET.get("category")
    subcategories = SubCategory.objects.filter(category_id=category_id)
    data = [{"id": s.id, "name": s.name} for s in subcategories]
    return JsonResponse(data, safe=False)

from django.shortcuts import get_object_or_404

def edit_dictionary_item(request, model, pk):
    model_map = {
        "Статусы": Status,
        "Типы": TransactionType,
        "Категории": Category,
        "Подкатегории": SubCategory,
    }

    ModelClass = model_map.get(model)
    instance = get_object_or_404(ModelClass, pk=pk)

    types = TransactionType.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        new_name = request.POST.get('name')
        related_id = request.POST.get('related_id')

        if new_name:
            instance.name = new_name

            if model == "Категории" and related_id:
                instance.type_id = related_id
            elif model == "Подкатегории" and related_id:
                instance.category_id = related_id

            instance.save()
            return redirect('app:manage_dictionaries')

    return render(request, "app/edit_item.html", {
        "item": instance,
        "model": model,
        "types": types,
        "categories": categories,
    })



def delete_dictionary_item(request, model, pk):
    model_map = {
        "Статусы": Status,
        "Типы": TransactionType,
        "Категории": Category,
        "Подкатегории": SubCategory,
    }

    ModelClass = model_map.get(model)
    instance = get_object_or_404(ModelClass, pk=pk)
    instance.delete()
    return redirect('app:manage_dictionaries')
