import cv2
import numpy as np
import time
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--video', help='Path to the video to be projected',
                    default='Ronaldo.mp4')            
args = parser.parse_args()

video_path=args.video
videostream = cv2.VideoCapture(1)   
video = cv2.VideoCapture(video_path)
dictionary = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
parameters =  cv2.aruco.DetectorParameters_create()

def find_and_warp(frame, source, cornerIds, dictionary, parameters):
    (imgH, imgW) = frame.shape[:2]
    (srcH, srcW) = source.shape[:2]
    markerCorners, markerIds, rejectedCandidates = cv2.aruco.detectMarkers(frame, dictionary, parameters=parameters)
    if len(markerCorners)!= 4:
        markerIds = np.array([]) 
    else: 
        markerIds.flatten()
    refPts = []
    for i in cornerIds:
        # grab the index of the corner with the current ID
        j = np.squeeze(np.where(markerIds == i))
        
        # if we receive an empty list instead of an integer index,
        # then we could not find the marker with the current ID
        if j.size == 0:
            continue
        else:
            j = j[0]   
        # otherwise, append the corner (x, y)-coordinates to our list
        # of reference points
        
        markerCorners = np.array(markerCorners)
        #print(markerCorners)
        corner = np.squeeze(markerCorners[j])
        refPts.append(corner)
    if len(refPts) != 4:
            return None
    (refPtTL, refPtTR, refPtBR, refPtBL) = np.array(refPts)
    dstMat = [refPtTL[0], refPtTR[1], refPtBR[2], refPtBL[3]]
    dstMat = np.array(dstMat)
    # define the transform matrix for the *source* image in top-left,
    # top-right, bottom-right, and bottom-left order
    srcMat = np.array([[0, 0], [srcW, 0], [srcW, srcH], [0, srcH]])
    # compute the homography matrix and then warp the source image to
    # the destination based on the homography
    (H, _) = cv2.findHomography(srcMat, dstMat)
    warped = cv2.warpPerspective(source, H, (imgW, imgH))
    mask = np.zeros((imgH, imgW), dtype="uint8")
    cv2.fillConvexPoly(mask, dstMat.astype("int32"), (255, 255, 255),
        cv2.LINE_AA)
    maskScaled = mask.copy() / 255.0
    maskScaled = np.dstack([maskScaled] * 3)
    warpedMultiplied = cv2.multiply(warped.astype("float"),
        maskScaled)
    imageMultiplied = cv2.multiply(frame.astype(float),
        1.0 - maskScaled)
    output = cv2.add(warpedMultiplied, imageMultiplied)
    output = output.astype("uint8")
    return output

while True:

    # Acquire frame and expand frame dimensions to have shape: [1, None, None, 3]
    # i.e. a single-column array, where each item in the column has the pixel RGB value
    ret, frame = videostream.read()
    ret, source = video.read()
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    frame_expanded = np.expand_dims(frame_rgb, axis=0)
    scale_percent = (1000/frame.shape[0])*100
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
    width2 = int(source.shape[1] * scale_percent / 100)
    height2 = int(source.shape[0] * scale_percent / 100)
    dim = (width2, height2)
    source = cv2.resize(source, dim, interpolation = cv2.INTER_AREA)
    
    
    # verify *at least* one ArUco marker was detected
    warped = find_and_warp(
        frame, source,
        cornerIds=(1, 2, 4, 3),
        dictionary=dictionary,
        parameters=parameters,
        )
    if warped is not None:
        # set the frame to the output augment reality frame and then
        # grab the next video file frame from our queue
        frame = warped
    cv2.imshow('Augmented Reality', frame)
    if cv2.waitKey(1) == ord('q'):
        break
        

cv2.destroyAllWindows()
print("Done")
