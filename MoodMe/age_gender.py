#git clone https://github.com/misbah4064/age_and_gender_detection.git

#import gdown
#cd age_and_gender_detection


#Download pre-trained data and unzip

#gdown https://drive.google.com/uc?id=1_aDScOvBeBLCn_iv0oxSO8X1ySQpSbIS

#unzip modelNweight.zip



#required modules

import cv2 as cv

import  math

import time




"""
getFaceBox functions
1.) Read the image and face reduction
2.) Pre-process the image. blobFromImage translates the img requested into an image containing the properties of the original image used for model training.
3.) 
"""
def getFaceBox(net, frame, conf_threshold=0.7):
    
    frameOpencvDnn = frame.copy()

    frameHeight = frameOpencvDnn.shape[0]

    frameWidth = frameOpencvDnn.shape[1]

    blob = cv.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)


    net.setInput(blob)

    detections = net.forward()

    bboxes = []

    for i in range(detections.shape[2]):

        confidence = detections[0, 0, i, 2]

        if confidence > conf_threshold:

            x1 = int(detections[0, 0, i, 3] * frameWidth)

            y1 = int(detections[0, 0, i, 4] * frameHeight)

            x2 = int(detections[0, 0, i, 5] * frameWidth)

            y2 = int(detections[0, 0, i, 6] * frameHeight)

            bboxes.append([x1, y1, x2, y2])

            cv.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight/150)), 8)

    return frameOpencvDnn, bboxes


faceProto = "age_and_gender_detection/modelNweight/opencv_face_detector.pbtxt"

faceModel = "age_and_gender_detection/modelNweight/opencv_face_detector_uint8.pb"

ageProto = "age_and_gender_detection/modelNweight/age_deploy.prototxt"

ageModel = "age_and_gender_detection/modelNweight/age_net.caffemodel"

genderProto = "age_and_gender_detection/modelNweight/gender_deploy.prototxt"

genderModel = "age_and_gender_detection/modelNweight/gender_net.caffemodel"


MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)


ageList = ['(0-2', '(4-6)', '(8-12)', '(15-20)','(25-32)', '(38-43)', '(48-53)', '(60-100)']

genderList = ['Male', 'Female']


#Load network

ageNet = cv.dnn.readNet(ageModel, ageProto)

genderNet = cv.dnn.readNet(genderModel, genderProto)

faceNet = cv.dnn.readNet(faceModel, faceProto)

padding = 20


def age_and_gender_detection(frame):

    #Read frame
    t = time.time()

    frameFace, bboxes = getFaceBox(faceNet, frame)

    for bbox in bboxes:


        face = frame[max(0, bbox[1] - padding):min(bbox[3]+padding, frame.shape[0] - 1), 
                max(0, bbox[0] - padding):min(bbox[2] + padding, frame.shape[1] - 1)]


        blob = cv.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)

        genderNet.setInput(blob)

        genderPreds = genderNet.forward()

        gender = genderList[genderPreds[0].argmax()]

        ageNet.setInput(blob)

        agePreds = ageNet.forward()

        age = ageList[agePreds[0].argmax()]

    return age, gender


def read_img(photo):

    inp = cv.imread(photo)


    return age_and_gender_detection(inp)


