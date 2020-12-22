# Read .hdf5 file for DAVIS346, and obtain events, frames, and frame timestamps.
# Jianing Li, Peking university, lijianing@pku.edu.cn, Sep. 2nd, 2020.

import argparse
import os
import h5py
import cv2
import numpy as np 

parser = argparse.ArgumentParser(
    description='Read the .hdf5 file for DAVIS346.')

parser.add_argument(
    '-i',
    '--input_dataset',
    #default = '../DVS_data_processing/0001_rotation_PCL_5000k_200r.hdf5',
    default = '/media/wangxiao/Elements/output_NfS_dataset_hdf5/airplane_landing/dvs_h5.h5',
    help='the .hdf5 file path for DAVIS346'
)


def make_color_histo(events, img=None, width=346, height=260):
    """
    simple display function that shows negative events as blue dots and positive as red one
    on a white background
    args :
        - events structured numpy array: timestamp, x, y, polarity.
        - img (numpy array, height x width x 3) optional array to paint event on.
        - width int.
        - height int.
    return:
        - img numpy array, height x width x 3).
    """
    if img is None:
        img = 255 * np.ones((height, width, 3), dtype=np.uint8)
    else:
        # if an array was already allocated just paint it grey
        img[...] = 255


    # import pdb 
    # pdb.set_trace() 

    if events.size:
        # assert events['x'].max() < width, "out of bound events: x = {}, w = {}".format(events['x'].max(), width)
        # assert events['y'].max() < height, "out of bound events: y = {}, h = {}".format(events['y'].max(), height)

        ON_index = np.where(events[:, 3] == 1)

        img[events[:, 2][ON_index], events[:, 1][ON_index], :] = [30, 30, 220] * events[:, 3][ON_index][:, None]  # red

        OFF_index = np.where(events[:, 3] == 0)
        img[events[:, 2][OFF_index], events[:, 1][OFF_index], :] = [200, 30, 30] * (events[:, 3][OFF_index] + 1)[:,None]  # blue
    
    return img








def _main(args):
    input_pathxxx = os.path.expanduser(args.input_dataset) # input .hdf5 file

    NfS_data_Path = "/media/wangxiao/Elements/output_NfS_dataset_hdf5/" 
    NfS_files = os.listdir(NfS_data_Path)


    #### videoidx: 17 

    for vid in range(18, len(NfS_files)): 
        videoName = NfS_files[vid] 
        
        input_path = "/media/wangxiao/Elements/output_NfS_dataset_hdf5/" + videoName + "/dvs_h5.h5"
        output_file = "/media/wangxiao/Elements/output_NfS_dataset_hdf5/" + videoName + "/event_IMGs/"

        os.mkdir(output_file)

        # f = h5py.File(input_path, "r")  

        with h5py.File(input_path) as f:

            # import pdb 
            # pdb.set_trace() 

            # List all groups
            print("Keys: %s" % f.keys())
            a_group_key = list(f.keys())[0]

            vidPath = "/home/wangxiao/Documents/rgb_event_tracking_benchmark/v2e/NFS_rgb_dataset/" + videoName + "/240/" + videoName + "/"
            vidIMGs = os.listdir(vidPath) 


            

            events = f['event'][:]                  # get events
            aps_frames_NUM = len(vidIMGs)           # get frames
            id_frame_timestamps = np.loadtxt("/media/wangxiao/Elements/output_NfS_dataset_hdf5/" + videoName + "/dvs-video-frame_times.txt")
            frame_timestamps = id_frame_timestamps[:, 1]

            xxx = events.shape[0] / aps_frames_NUM 


        start_timestamp = frame_timestamps[0] 
        interval = 0.1 
        start_index = 0

        # saving event images.
        for i in range(int(aps_frames_NUM)):

            # start_index = np.searchsorted(frame_timestamps, int(start_timestamp)+i*interval*1e6) 
            # list B(event_timestamps) insert in list A(timestamp_indexes)
            # end_index = np.searchsorted(frame_timestamps, int(start_timestamp)+(i+1)*interval*1e6)



            end_index = start_index + int(xxx)  # 15000 event numbers

            # import pdb 
            # pdb.set_trace() 

            rec_events = events[start_index:end_index, :]

            # print('event number = {}'.format(end_index-start_index))

            #rec_events = events[start_index:start_index+20000]
            #show_events(rec_events, 346, 260)

            event_image = make_color_histo(rec_events)

            save_path = output_file +'{}.png'.format(i+1)
            cv2.imwrite(save_path, event_image)

            print("==>> save IMG done: ", save_path) 

            start_index = end_index 


if __name__ == '__main__':
    _main(parser.parse_args())




