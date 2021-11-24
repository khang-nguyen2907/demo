import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.feature import local_binary_pattern
from sklearn.naive_bayes import MultinomialNB
from imutils import paths
from sklearn.metrics import accuracy_score
from skimage.feature import hog
import os


def feature_vector_extract(image, npoint, radius, method = 'default'):
    #chuyen thanh anh xam
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #local binary pattern de trich xuat feature
    lbp = local_binary_pattern(image= gray, P = npoint, R = radius, method= method)
    rows, columns = lbp.shape
    size = rows*columns
    # "lbp" tra ve 1 mang 2 chieu nen t reshape no lai thanh 1 vector de no thanh feature vector
    f_vec = lbp.reshape(size)

    return f_vec

def feature_descriptor(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resize = cv2.resize(src=img, dsize=(64, 128))
    fd, hog_image = hog(resize, orientations= 9, pixels_per_cell= (8, 8), cells_per_block= (2, 2), visualize= True)
    return fd
#load all training image return a dictionary with labels and data
def load_label_data(path):

    labels = list()
    train_labels = list()
    data = list()
    train_data = list()
    dim = (256, 256)
    for imagePath in paths.list_images(path):
        image = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)
        # resize = cv2.resize(image, dim, interpolation= cv2.INTER_AREA)
        # feature_vec = feature_vector_extract(resize, 8, 1)
        fd = feature_descriptor(image)
        labels.append(imagePath.split(os.path.sep)[-2])
        data.append(fd)
        train_labels = np.array(labels)
        train_data = np.array(data)




    return (train_data, train_labels)
path ='G:\LocalBinaryPattern\image_train' #day la duong link dan toi tap
# train = load_training_data(path)
# labels = train[0]
# data = train[1]
(train_data, train_label) = load_label_data(path)
# test = load_training_data('G:\CN4\MAI\LBP\MAI_Image')
(test_data, test_label) = load_label_data('G:\LocalBinaryPattern\image_test')
model = MultinomialNB()
model.fit(train_data, train_label)

pred = model.predict(test_data)
score = accuracy_score(test_label, pred)*100
print("accuracy = ", score)

# dim = (256, 256)
# for imagePath in paths.list_images('G:\CN4\MAI\LBP\d'):
#     vector = []
#     image = cv2.imread(imagePath, cv2.IMREAD_UNCHANGED)
#     resize = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
#
#     feature_vec =feature_vector_extract(resize, 8, 1)
#     vector.append(feature_vec)
#     pred = str(model.predict(np.array(vector))[0])
#     prob = model.predict_proba(np.array(vector))
#     # s = pred + "\n" +str(prob)
#
#     #in labels len hinh anh test
#     cv2.putText(resize, pred, (10,30), cv2.FONT_HERSHEY_SIMPLEX,0.5, (0, 0, 255), 1)
#     cv2.imshow("Image", resize)
#     print("Probability of this image in each class: ", prob)
#     cv2.waitKey(0)
