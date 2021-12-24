import cv2



from deepface import DeepFace


def face_exp(photo):

    img = cv2.imread(photo)
    result = DeepFace.analyze(img, actions=['emotion'])
    return result["dominant_emotion"]



