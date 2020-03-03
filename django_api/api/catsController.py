from rest_framework.decorators import api_view, schema
from rest_framework.response import Response
from ..model.cats import Cats


@api_view(["GET"])
@schema(Cats())
def get_cat(request):
    return Response({"ga": "to"})
