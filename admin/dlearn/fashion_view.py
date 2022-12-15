from django.http import JsonResponse, QueryDict
from matplotlib import pyplot as plt
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
import tensorflow as tf

from admin.dlearn.fashion_service import FashionService


@api_view(['POST'])
@parser_classes([JSONParser])
def fashion(request):
    data = request.data
    test_num = tf.constant(int(data['testNum']))

    service = FashionService().service_model(test_num)
    print(f'예측한 답:{service}')

    resp = service
    return JsonResponse({'result':str(resp)})