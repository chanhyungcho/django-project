import pandas as pd
import tensorflow as tf
from keras import Sequential
from keras.layers import Dense
from keras.saving.save import load_model
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder


'''
Iris Species
Classify iris plants into three species in this classic dataset #답이 3종류고 분류기를 써야한다. = 이처럼 방향성을 잡고 시작해야.
'''


class IrisService(object):
    def __init__(self):
        model = load_model('../save/iris_model.h5')
        graph = tf.get_default_graph()
        target_names = datasets.load_iris().target_names


    def hook(self):
        self.service_model()

    def service_model(self):
        pass



iris_menu = ["Exit",  # 0
             "Hook",  # 1
             "spec"  # 2
             ]
iris_lambda = {
    "1": lambda x: x.hook(),
    # "2": lambda x: x.spec(),

}
if __name__ == '__main__':
    iris = IrisService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(iris_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                iris_lambda[menu](iris)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")