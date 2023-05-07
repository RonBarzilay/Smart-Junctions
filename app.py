import cv2
from imageai.Detection import VideoObjectDetection
from frame_data import *

# from moviepy.editor import *
# from moviepy.video.fx.resize import resize

"""
=========================================
            Global Variables
=========================================
"""
model_path = r"model/yolo.h5"
junction_name = "Highway"
video_input = fr"video input/{junction_name}.mp4"
video_output = fr"video output/{junction_name} output"
web_cam = cv2.VideoCapture(0)
data_collected = []

"""
=========================================
            Global Functions
=========================================
"""


def for_frame(frame_number, data, output_count):
    """
    This function will collect required data from each frame
    :param frame_number:
    :param data:
    :param output_count:
    :return:
    """
    frame_data = FrameData(data=data, frame_number=frame_number, count=output_count)
    print("FOR FRAME No. ", frame_data.get_frame_number())
    print("Output for each object : ", frame_data.get_data())
    print("Output count for unique objects : ", frame_data.get_uniq_objects_counter())
    print("------------END OF A FRAME --------------")
    data_collected.append(frame_data)


# Creating and initializing model to our detector
detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

# What we wish to detect
obj_to_detect = detector.CustomObjects(car=True, bus=True, motorcycle=True, truck=True)

video_path = detector.detectObjectsFromVideo(input_file_path=video_input,
                                             camera_input=web_cam,
                                             output_file_path=video_output,
                                             frames_per_second=1, minimum_percentage_probability=60,
                                             per_frame_function=for_frame, custom_objects=obj_to_detect)
print(video_path)
