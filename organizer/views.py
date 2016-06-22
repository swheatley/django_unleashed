from django.http.response import HttpResponse

from .models import Tag


def homepage(request):
    tag_list = Tag.objects.all()

    html_output = "<html>"

    html_output += "<head>"

    html_output += "<title>"

    html_output += "Don't Do This!</title>\n"

    html_output += "</head>"

    html_output += "<body>"



    for tag in tag_list:
        html_output += " <ul>"

        html_output += " <li>"

        html_output += tag.name.title()

        html_output += "</li>"

        html_output += " </ul>"

        html_output += "</body>"
        html_output += "</html>"

    return HttpResponse(html_output)
