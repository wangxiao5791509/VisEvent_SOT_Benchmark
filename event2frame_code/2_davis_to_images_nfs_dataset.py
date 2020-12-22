# Read .aedat4 file from DAVIS346 at the temporal window (t1-t2), generating frames.
# Jianing Li, Peking university, lijianing@pku.edu.cn, Oct. 15th, 2020.

import argparse
import os
import numpy as np
import math
from dv import AedatFile, LegacyAedatFile
import cv2
import xlrd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import aedat



# decoder = aedat.Decoder('/home/wangxiao/Documents/rgb_event_tracking_benchmark/v2e/output/airboard_1/v2e-dvs-events.aedat4')
# print(decoder.id_to_stream())

# for packet in decoder:
#     print(packet['stream_id'], end=': ')
#     if 'events' in packet:
#         print('{} polarity events'.format(len(packet['events'])))
#     elif 'frame' in packet:
#         print('{} x {} frame'.format(packet['frame']['width'], packet['frame']['height']))
#     elif 'imus' in packet:
#         print('{} IMU samples'.format(len(packet['imus'])))
#     elif 'triggers' in packet:
#         print('{} trigger events'.format(len(packet['triggers'])))



# import pdb 
# pdb.set_trace() 

        


parser = argparse.ArgumentParser(
    description='Read the .aedat file from DAVIS346.')

parser.add_argument('-n', '--neuromorphic_file', default = './tables/neuromorphic_data_newfile.xlsx', help='the .xlsx file path') 


def show_events(events, width=346, height=240):
    """
    plot events in three-dimensional space.

    Inputs:
    -------
        true events   - the true event signal.
        events   - events include true event signal and noise events.
        width    - the width of AER sensor.
        height   - the height of AER sensor.

    Outputs:
    ------
        figure     - a figure shows events in three-dimensional space.

    """
    ON_index = np.where(events['polarity'] == 1)
    OFF_index = np.where(events['polarity'] == 0)


    fig = plt.figure('{} * {}'.format(width, height))
    ax = fig.gca(projection='3d')

    ax.scatter(events['timestamp'][ON_index]-events['timestamp'][0], events['x'][ON_index], events['y'][ON_index], c='red', label='ON', s=3)  # events_ON[1][:]
    ax.scatter(events['timestamp'][OFF_index]-events['timestamp'][0], events['x'][OFF_index], events['y'][OFF_index], c='mediumblue', label='OFF', s=3)


    font1 = {'family': 'Times New Roman', 'size': 20}
    font1_x = {'family': 'Times New Roman', 'size': 19}
    font2 = {'size': 13}
    ax.set_xlabel('t(us)', font1_x)  # us
    ax.set_ylabel('x', font1)
    ax.set_zlabel('y', font1)
    #ax.set_xlim([0, max(new_events[1][:])])  # int(length/1000)
    #ax.set_ylim([1, width])
    #ax.set_zlim([1, height])
    # print(numpy.linspace(1, width, 5).astype(int))
    #ax.set_yticks(np.linspace(1, width, 5).astype(int))
    #ax.set_zticks(np.linspace(1, height, 5).astype(int))
    #ax.set_xticks(np.linspace(0, max(events['timestamp'][:]), 5))  # length
    #ax.xaxis.set_tick_params(labelsize=14)  # 12
    #ax.yaxis.set_tick_params(labelsize=14)  # 13
    #ax.zaxis.set_tick_params(labelsize=14)  # 13

    #ax.legend(loc='upper center', bbox_to_anchor=(0.77, 0.83), prop=font2)

    plt.show()


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
    if events.size:
        assert events['x'].max() < width, "out of bound events: x = {}, w = {}".format(events['x'].max(), width)
        assert events['y'].max() < height, "out of bound events: y = {}, h = {}".format(events['y'].max(), height)

        ON_index = np.where(events['polarity'] == 1)

        img[events['y'][ON_index], events['x'][ON_index], :] = [30, 30, 220] * events['polarity'][ON_index][:, None]  # red

        OFF_index = np.where(events['polarity'] == 0)
        img[events['y'][OFF_index], events['x'][OFF_index], :] = [200, 30, 30] * (events['polarity'][OFF_index] + 1)[:,None]  # blue
    return img


def events_to_event_images(input_filename, output_file, output_filename, aps_frames_NUM, interval=0.025):

    """
    Mapping asynchronous events into event images
    args :
        - input_file:.aedat file, saving dvs events.
        - output_file: the output filename saving timestamps.
        - event number: generating an event image needs event number.
    return:
        - event_image
        - timestamp file: .txt, saving the timestamps for event images.
    """
    


    
    with AedatFile(input_filename) as f:

        # import pdb 
        # pdb.set_trace() 
        
        events = np.hstack([event for event in f['events'].numpy()]) 

        start_timestamp = events[0][0] 

        # saving event images.
        for i in range(int(aps_frames_NUM)):
            start_index = np.searchsorted(events['timestamp'], int(start_timestamp)+i*interval*1e6) 
            # list B(event_timestamps) insert in list A(timestamp_indexes)
            end_index = np.searchsorted(events['timestamp'], int(start_timestamp)+(i+1)*interval*1e6)
            #end_index = start_index + 5000 # 15000 event numbers

            rec_events = events[start_index:end_index]



            # print('event number = {}'.format(end_index-start_index))

            #rec_events = events[start_index:start_index+20000]
            # show_events(rec_events, 346, 260)
    
            event_image = make_color_histo(rec_events)

            save_path = output_file +'/{}.png'.format(i+1)
            cv2.imwrite(save_path, event_image)

            print('The filename {}, the {} frame has been done!'.format(input_filename, i+1))
            output_filename.write(save_path + "\n")  # save the timestamp


def save_aps_images(input_filename, output_image_file):
    """
    Mapping asynchronous events into event images
    args :
        - input_file:.aedat file, saving davis data.
        - output_file: the output filename saving aps images.
    return:
        - aps_image
    """

    # import pdb 
    # pdb.set_trace() 
    

    with AedatFile(input_filename) as f:
        j=0
        for frame in f['frames']:
            save_image = frame.image
            save_image_path = output_image_file + '/{}.png'.format(j + 1)
            cv2.imwrite(save_image_path, save_image)
            j = j+1
            print('The {} has been done!'.format(save_image_path))




def _main(args):
    # input_file=os.path.expanduser(args.neuromorphic_file)
    # neuromorphic_file = xlrd.open_workbook(input_file)
    # neuromorphic_information = neuromorphic_file.sheet_by_name('neuromorphic_dataset')
    # sequence_names = neuromorphic_information.col_values(0)[1:]
    # temporal_lengths = neuromorphic_information.col_values(1)[1:]
    # start_timestamps = neuromorphic_information.col_values(4)[1:]

    interval = 0.01   # 100 FPS
    output_filename = open('./neuromorphic_frames.txt', 'w')

    # rawfile_path = "/home/wangxiao/Documents/rgb_event_tracking_project/data_processing/raw_dataset/" 

    rawfile_path = "/home/wangxiao/Documents/rgb_event_tracking_benchmark/v2e/output/"
    files = os.listdir(rawfile_path) 
    
    
    
    savepath = "/home/wangxiao/Documents/rgb_event_tracking_benchmark/v2e/output_event_image/"

    # for i in range(len(files)):
    for i in range(1):         

        sequence_names = files[i] 

        davis_file = rawfile_path + sequence_names + "/v2e-dvs-events.aedat4"
        output_path = savepath + sequence_names + "/EVENT_frames/"
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        output_aps_path = savepath + sequence_names + "/APS_frames/"
        if not os.path.exists(output_aps_path):
            os.makedirs(output_aps_path)

        # events_to_event_images(davis_file, output_path, output_filename, start_timestamps[i], temporal_lengths[i], interval=0.01)
        # save_aps_images(davis_file, output_aps_path)
        
        rgb_imgs = "/home/wangxiao/Documents/rgb_event_tracking_benchmark/v2e/NFS_rgb_dataset/" + sequence_names + "/240/" + sequence_names + "/"

        aps_frames_NUM = len(os.listdir(rgb_imgs))  
        events_to_event_images(davis_file, output_path, output_filename, aps_frames_NUM, interval=0.1) 

    output_filename.close()


if __name__ == '__main__':
    _main(parser.parse_args())






