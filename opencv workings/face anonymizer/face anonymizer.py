import cv2
import mediapipe as mp
import os

img1 = cv2.imread(os.path.join('.','data','facetest2.png'))
img = img1

H, W, _ = img.shape
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    out = face_detection.process(img_rgb)
    if out.detections is not None:
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            x1, y1, w, h = bbox.xmin, bbox.ymin, bbox.width, bbox.height

            x1 = int(x1 * W)
            y1 = int(y1 * H)
            w = int(w * W)
            h = int(h * H)

    
            # blur faces
        img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))
#visualising the blurred image:
cv2.imshow('original',img1)
cv2.imshow('anonymized frame',img
           )
cv2.waitKey(0)