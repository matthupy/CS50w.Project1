from django.shortcuts import render, redirect
from random import randrange

import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, title):
    entry = util.get_entry(title)

    if (entry is not None):
        entry = markdown2.markdown(entry)

        context = {
            "entry":entry,
            "title":title,
        }
        return render(request, "encyclopedia/page.html", context)

def random(request):
    # Get a random page
    entries = util.list_entries()
    index = randrange(len(entries))
    title = entries[index]

    return redirect('page', title=title)

