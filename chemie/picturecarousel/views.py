from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import Pictureform, TagForm
from .models import Contribution


@login_required
def submit_picture(request):
    form = Pictureform(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save()
        form.save_m2m()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Bildet har blitt sendt inn!",
            extra_tags="Bildet ble sendt",
        )
        return redirect(reverse("carousel:submit"))
    context = {"form": form}

    return render(request, "picturecarousel/submit_picture.html", context)


def view_carousel(request):
    pictures = Contribution.objects.get_all_shuffled()
    context = {"pictures": pictures}
    return render(request, "picturecarousel/carousel.html", context)


@permission_required("picturecarousel.change_contribution")
def approve_pictures(request):
    awaiting_approval = (
        Contribution.objects.filter(approved=False)
        .prefetch_related("author")
        .order_by("-date")
    )

    paginator = Paginator(awaiting_approval, 10)
    page_number = request.GET.get("page", 1)

    try:
        picture_page = paginator.page(page_number)
    except PageNotAnInteger:
        picture_page = paginator.page(1)
    except EmptyPage:
        picture_page = paginator.page(paginator.num_pages)

    context = {"picture_page": picture_page}
    return render(request, "picturecarousel/approve.html", context)


@permission_required("picturecarousel.change_contribution")
def approve_deny(request, picture_id, deny=False):
    if request.method == "POST":
        picture = get_object_or_404(Contribution, id=picture_id)
        if not deny:
            picture.approve()
            picture.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Bildet er godkjent",
                extra_tags="Yay!",
            )
        else:
            picture.delete()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Bildet ble slettet",
                extra_tags="Slettet!",
            )
        return HttpResponseRedirect(reverse("carousel:overview"))
    return HttpResponseRedirect(reverse("carousel:overview"))


@login_required
def view_pictures(request):
    pictures = (
        Contribution.objects.filter(approved=True)
        .prefetch_related("author")
        .order_by("-date")
    )

    paginator = Paginator(pictures, 10)
    page_number = request.GET.get("page", 1)

    try:
        picture_page = paginator.page(page_number)
    except PageNotAnInteger:
        picture_page = paginator.page(1)
    except EmptyPage:
        picture_page = paginator.page(paginator.num_pages)

    context = {"picture_page": picture_page}
    return render(request, "picturecarousel/view_active.html", context)


@permission_required("picturecarousel.change_contribution")
def tag_users(request, id):
    pic = Contribution.objects.get(id=id)
    form = TagForm(request.POST or None, instance=pic)

    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            form.save_m2m()

            # Redirect user to the page he came from
            # (either carousel:overview or carousel:view_pictures)
            came_from = request.GET.get("from", None)
            if came_from:
                return redirect(came_from)
            else:
                return redirect(reverse("carousel:overview"))
    context = {"pic": pic, "form": form}
    return render(request, "picturecarousel/tag_users.html", context)
