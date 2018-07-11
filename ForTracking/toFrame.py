#! encoding: UTF-8
"""
    Created on Oct 24, 2017
    
    @author: Lilac
"""
print(__doc__)
import os
import cv2

def toFrame():
    videos_src_path = '/home'
    videos_save_path = '/home'
    video_name="play.mp4"

    cap = cv2.VideoCapture(videos_src_path + video_name)
    k=1
    #print cv2.CAP_PROP_FRAME_COUNT
    frame_count = 0
    all_frames = []
    while (True):
        ret, frame = cap.read()
        if ret is False:
            break
        all_frames.append(frame)
        cv2.imwrite(videos_save_path+str(frame_count)+".jpg",frame)
        frame_count+=1
    print frame_count

def playvideo():
    videos_src_path = '/home'
    videos_save_path = '/home'
    video_name="play.mp4"
    cap = cv2.VideoCapture(videos_src_path + video_name)
    while (cap.isOpened()):
        ret, frame = cap.read()
        Color_set = cv2.cvtColor(frame, cv2.COLOR_RGBA2RGB)
        cv2.imshow("frame",Color_set)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    toFrame()
