## script to load the aedat4 file and save into the images and *.txt files

from dv import AedatFile
import cv2
import os
import numpy as np
from PIL import Image
import pdb 


def extract_davis(aedat_file_path, filename_txt_path, croped_events_path, save_path_dvs, save_path_aps, dvs_img_interval):
    
    frame_no = 0
    frame_all = []
    frame_exposure_time = []
    frame_interval_time = []
    # use_mode = 'frame_exposure_time'  #### default mode 
    use_mode = 'frame_interval_time'
    with AedatFile(aedat_file_path) as f:
        # list all the names of streams in the file
        print(f.names)
        # extract timestamps of each frame 
        for frame in f['frames']:
            frame_all.append(frame.image)   
            frame_exposure_time.append([frame.timestamp_start_of_exposure, frame.timestamp_end_of_exposure])    ## [1607928583397102, 1607928583401102]
            frame_interval_time.append([frame.timestamp_start_of_frame,    frame.timestamp_end_of_frame])       ## [1607928583387944, 1607928583410285]

            # pdb.set_trace()
        
        if use_mode == 'frame_exposure_time':
            frame_timestamp = frame_exposure_time
        elif use_mode == 'frame_interval_time':
            frame_timestamp = frame_interval_time

        frame_num = len(frame_timestamp)
        # Access dimensions of the event stream
        height, width = f['events'].size       
        event_frame = 255 * np.ones((height, width, 3), dtype=np.uint8)
        # loop through the "events" stream
        # events = np.hstack([packet for packet in f['events'].numpy()])

        # # Access information of all events by type
        # timestamps, x, y, polarities = events['timestamp'], events['x'], events['y'], events['polarity']


        # pdb.set_trace() 
        # save event_img
        idx = np.round(np.linspace(0, len(frame_timestamp) - 1, int(frame_num/dvs_img_interval))).astype(int)   ## frame index [0, 1, 2, ... , 3847] 
        frame_timestamp = np.array(frame_timestamp)[idx]    ## (3848, 2) 
        
        # one reader #
        # for e in f['events']: 
        #     if e.timestamp >= frame_timestamp[frame_no][0]:
        #         event_frame[int(e.y),int(e.x), :] = [30, 30, 220] * int(e.polarity) +  [200, 30, 30] * int(not e.polarity)
        #         #event_window.append([e.timestamp, e.x, e.y, e.polarity])
        #     if e.timestamp > frame_timestamp[frame_no][1]:
        #         cv2.imwrite(os.path.join(save_path_dvs, 'frame{:04d}'.format(frame_no*dvs_img_interval)+'.bmp'), event_frame)
        #         frame_no = frame_no + 1
        #         event_frame = 255 * np.ones((height, width, 3), dtype=np.uint8)
        #         if frame_no > frame_num-1:
        #             break
        #         continue
        
        file = open(filename_txt_path, 'w')

        # another reader # speed up
        # events will be a named numpy array
        events = np.hstack([packet for packet in f['events'].numpy()])
        timestamps, x, y, polarities = events['timestamp'], events['x'], events['y'], events['polarity']

        # start_frame = 0                         
        # end_frame   = 50                           
        # frame_num   = end_frame - start_frame 

        # start_idx = np.where(events['timestamp'] >= frame_timestamp[start_frame][0])[0][0]
        # end_idx   = np.where(events['timestamp'] >= frame_timestamp[end_frame][1])[0][0]
        # cropped_event = events[start_idx:end_idx]
        # timestamps, x, y, polarities = cropped_event['timestamp'], cropped_event['x'], cropped_event['y'], cropped_event['polarity']

        event_file = open(croped_events_path, 'w')
        for ii in range(timestamps.shape[0]):
            event_file.write(('{}, {}, {}, {}'.format(timestamps[ii], x[ii], y[ii], polarities[ii]) + "\n"))   

        event_file.close()

        # pdb.set_trace() 



        # for frame_no in range(start_frame, end_frame):
        for frame_no in range(0, int(frame_num/dvs_img_interval)-1):
        	
            event_frame = 255 * np.ones((height, width, 3), dtype=np.uint8)
            start_idx = np.where(events['timestamp'] >= frame_timestamp[frame_no][0])[0][0]
            end_idx   = np.where(events['timestamp'] >= frame_timestamp[frame_no][1])[0][0]
            event = events[start_idx:end_idx]
            
            on_idx  = np.where(event['polarity'] == 1)      ## (array([    3,     4,     5, ..., 10633, 10635, 10636]),) 
            off_idx = np.where(event['polarity'] == 0)      ## (array([    0,     1,     2, ..., 10629, 10632, 10634]),)
            event_frame[event['y'][on_idx],  event['x'][on_idx], :]  = [30, 30, 220] * event['polarity'][on_idx][:, None]
            event_frame[event['y'][off_idx], event['x'][off_idx], :] = [200, 30, 30] * (event['polarity'][off_idx]+1)[:, None]
            
            cv2.imwrite(os.path.join(save_path_dvs, 'frame{:04d}'.format(frame_no*dvs_img_interval)+'.bmp'), event_frame)
            cv2.imshow('Event Image', event_frame)
            cv2.waitKey(1)
            print('The {} timestamp is {}'.format(frame_no, events['timestamp'][frame_no]))
            file.write('The {} frame, the timestamp is {}'.format(frame_no, events['timestamp'][frame_no]) + "\n")  # save the timestamp
            
            # pdb.set_trace() 
            
        file.close()

        # save aps_img
        # for frame_no in range(start_frame, end_frame):
        for frame_no in range(0, int(frame_num/dvs_img_interval)-1):
            this_frame = frame_all[frame_no]
            event_img = np.zeros((height, width))
            cv2.imwrite(os.path.join(save_path_aps, 'frame{:04d}'.format(frame_no)+'.bmp'), this_frame)
            cv2.imshow('APS Image', this_frame)
            cv2.waitKey(1)

        # pdb.set_trace()


def extract_rgb(rgb_file_path, save_path_rgb):
    cap = cv2.VideoCapture(rgb_file_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_num = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_no = 0
    while(True):
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imwrite(os.path.join(save_path_rgb, 'frame{:04d}'.format(frame_no)+'.bmp'), frame)
        frame_no = frame_no + 1



def main():
    aedat_path = '/home/wangxiao/Downloads'
    dvs_img_interval = 1
    for root, dirs, files in os.walk(aedat_path):
        for file in files:
            (filename, extension) = os.path.splitext(file)

            print("==>> filename: ", filename)

            if (extension == '.aedat4'):

                if filename+'_aps' in os.listdir(root) or filename+'_dvs' in os.listdir(root):
                    print("==>> Skip this video ... ")
                    continue 
                
                save_path_dvs = os.path.join(root, filename, filename+'_dvs')
                save_path_aps = os.path.join(root, filename, filename+'_aps')
                aedat_file_path = os.path.join(root, filename+'.aedat4')
                filename_txt_path = os.path.join(root, filename+'_timestamp.txt')
                croped_events_path = os.path.join(root, filename+'_events.txt')
                
                if not os.path.exists(save_path_dvs):
                    os.makedirs(save_path_dvs)
                if not os.path.exists(save_path_aps):
                    os.makedirs(save_path_aps)

                extract_davis(aedat_file_path, filename_txt_path, croped_events_path, save_path_dvs, save_path_aps, dvs_img_interval) 


if __name__ == '__main__':
    main()





