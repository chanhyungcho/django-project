from django.shortcuts import render



from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser




@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    user_info = request.data
    SepalLengthCm = user_info['SepalLengthCm']
    SepalWidthCm = user_info['SepalWidthCm']
    PetalLengthCm = user_info['PetalLengthCm']
    PetalWidthCm = user_info['PetalWidthCm']

    print(f'리액트에서 보낸 데이터: {user_info}')
    print(f'넘어온 꽃받침 길이: {SepalLengthCm}')
    print(f'넘어온 꽃받침 너비: {SepalWidthCm}')
    print(f'넘어온 꽃잎 길이: {PetalLengthCm}')
    print(f'넘어온 꽃잎 너비: {PetalWidthCm}')
    return JsonResponse({'꽃 입력 결과': '성공!'})
