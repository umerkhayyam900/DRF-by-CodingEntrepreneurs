from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

# def api_home(request, *args, **kwargs):
#     body = request.body # byte string of json data
#     data = {}
#     try:
#         data = json.loads(body) # string of json data -> python dictionary
#     except:
#         pass
#     print(data)
#     print(request.headers)
#     data["params"] = dict(request.GET)
#     data["headers"] = dict(request.headers)
#     data["content_type"] = request.content_type
#     # print("body", body)
#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#    model_data = Product.objects.all().order_by("?").first()
#    print("model_data", model_data)
#    data = {}
#    if model_data:
#       data = model_to_dict(model_data, fields=["id", "title", "price"])

#    return JsonResponse(data) 

# DRF api view
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # data = serializer.save()
        # print(data)
        data = serializer.data
        return Response(data)
    # return Response({"invalid": "not good data"}, status= 400)