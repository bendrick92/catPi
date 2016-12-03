import picamera
import time
import os
import glob
from datetime import datetime
import subprocess


class CameraManager():

    BASE_DIR = os.path.dirname(os.path.realpath(__file__))
    IMGS_DIR = os.path.join(BASE_DIR, 'imgs/')
    VIDS_DIR = os.path.join(BASE_DIR, 'vids/')

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.brightness = 55
        self.camera.contrast = 5
        self.camera.resolution = (1280, 720)
        self.camera.framerate = 30
        # Wait for the automatic gain control to settle
        time.sleep(2)
        # Now fix the values
        self.camera.shutter_speed = self.camera.exposure_speed
        self.camera.exposure_mode = 'off'
        g = self.camera.awb_gains
        self.camera.awb_mode = 'off'
        self.camera.awb_gains = g

        self.full_img_file_path = os.path.join(self.IMGS_DIR)
        if not os.path.exists(self.full_img_file_path):
            os.makedirs(self.full_img_file_path)
        self.full_vid_file_path = os.path.join(self.VIDS_DIR)
        if not os.path.exists(self.full_vid_file_path):
            os.makedirs(self.full_vid_file_path)

    def get_img_count(self):
        return len([f for f in os.listdir(self.full_img_file_path) if os.path.isfile(os.path.join(self.full_img_file_path, f))])

    def get_vid_count(self):
        return len([f for f in os.listdir(self.full_vid_file_path) if os.path.isfile(os.path.join(self.full_vid_file_path, f))])

    def get_oldest_img_file_name(self):
        all_img_files = glob.glob(self.full_img_file_path + '*.jpg')
        all_img_files.sort(key=os.path.getmtime)
        oldest_img_file_name = os.path.basename(all_img_files[0])
        return oldest_img_file_name

    def get_oldest_vid_file_name(self):
        all_vid_files = glob.glob(self.full_vid_file_path + '*.jpg')
        all_vid_files.sort(key=os.path.getmtime)
        oldest_vid_file_name = os.path.basename(all_vid_files[0])
        return oldest_vid_file_name

    def delete_img_file_by_name(self, img_file_name):
        if os.path.exists(self.full_img_file_path + img_file_name):
            os.remove(self.full_img_file_path + img_file_name)

    def delete_vid_file_by_name(self, vid_file_name):
        if os.path.exists(self.full_vid_file_path + vid_file_name):
            os.remove(self.full_vid_file_path + vid_file_name)

    def get_timestamp_string(self):
        return str(datetime.now().strftime('%Y%m%d_%H%M%S'))

    def take_picture(self):
        if self.get_img_count() > 30:
            self.delete_img_file_by_name(self.get_oldest_img_file_name())
        img_file_name = self.get_timestamp_string() + '.jpg'
        self.camera.capture(self.full_img_file_path + img_file_name)
        return img_file_name

    def take_video(self, length):
        if self.get_vid_count() > 10:
            self.delete_vid_file_by_name(self.get_oldest_vid_file_name())
        timestamp_string = self.get_timestamp_string()
        vid_file_name = timestamp_string + '.h264'
        self.camera.start_recording(self.full_vid_file_path + vid_file_name)
        time.sleep(length)
        self.camera.stop_recording()
        #try:
        #    converted_vid_file_name = self.full_vid_file_path + timestamp_string + '.mp4'
        #    print 'MP4Box -add ' + vid_file_name + ' ' + converted_vid_file_name
        #    subprocess.check_call(['MP4Box -add', vid_file_name, converted_vid_file_name])
        #except Exception as e:
        #    print e
        return vid_file_name

    def take_picture_series(self, series_count):
        counter = 1
        img_file_names = []
        while series_count >= counter:
            img_file_name = self.take_picture()
            img_file_names.append(img_file_name)
            counter += 1
            time.sleep(5)
        return img_file_names