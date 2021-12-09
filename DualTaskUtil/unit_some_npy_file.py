import numpy as np
import os

print(os.getcwd())
data_01 = np.load("./all_data/data_01_activations.npy")
data_02 = np.load("./all_data/data_02_activations.npy")
data_03 = np.load("./all_data/data_03_activations.npy")
data_04 = np.load("./all_data/data_04_activations.npy")

all_data = np.concatenate([data_01, data_02, data_03, data_04])
np.save("./all_data/all_activations_1st_try.npy", all_data)

print(all_data.shape)



# data_01_predict_0=np.load("./all_data/data_01_predict_0.npy")
# data_01_predict_1=np.load("./all_data/data_01_predict_1.npy")
#
# print(data_01_predict_0.shape)
#
# data_02_predict_0=np.load("./all_data/data_02_predict_0.npy")
# data_02_predict_1=np.load("./all_data/data_02_predict_1.npy")
#
# print(data_02_predict_1.shape)
#
# data_03_predict_0=np.load("./all_data/data_03_predict_0.npy")
# data_03_predict_1=np.load("./all_data/data_03_predict_1.npy")
#
# data_04_predict_0=np.load("./all_data/data_04_predict_0.npy")
# data_04_predict_1=np.load("./all_data/data_04_predict_1.npy")
#
# print(data_04_predict_1.shape)


# predict_0 = np.concatenate([data_01_predict_0, data_02_predict_0, data_03_predict_0, data_04_predict_0])
# predict_1 = np.concatenate([data_01_predict_1, data_02_predict_1, data_03_predict_1, data_04_predict_1])

# np.save("./all_data/predict_0.npy", predict_0)
# np.save("./all_data/predict_1.npy", predict_1)
# print(predict_0.shape)

print("######")
