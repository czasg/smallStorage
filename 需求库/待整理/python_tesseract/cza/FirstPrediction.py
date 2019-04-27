from imageai.Prediction import ImagePrediction

import os

execution_path = os.getcwd()

prediction = ImagePrediction()

prediction.setModelTypeAsResNet()

#prediction.setModelPath( execution_path + "esnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.setModelPath('resnet50_weights_tf_dim_ordering_tf_kernels.h5')

prediction.loadModel()

predictions, percentage_probabilities = prediction.predictImage("123.png", result_count=5)
#predictions, percentage_probabilities = prediction.predictImage("b123.png", result_count=5)
#predictions, percentage_probabilities = prediction.predictImage("g123.png", result_count=5)

print(predictions,'!!!!!!!!!!!!!!!!!!')
print(percentage_probabilities,'!!!!!!!!!!!!!!!!!!')
print(prediction)

for index in range(len(predictions)):
	print('##################')
	print(predictions[index], percentage_probabilities[index])