import pandas as pd
import numpy as np
from os.path import splitext
import torch
from PIL import Image


def events_to_voxel_grid(events, num_bins, width, height):
    """
    Build a voxel grid with bilinear interpolation in the time domain from a set of events.

    :param events: a [N x 4] NumPy array containing one event per row in the form: [timestamp, x, y, polarity]
    :param num_bins: number of bins in the temporal axis of the voxel grid
    :param width, height: dimensions of the voxel grid
    """

    assert(events.shape[1] == 4)
    assert(num_bins > 0)
    assert(width > 0)
    assert(height > 0)

    voxel_grid = np.zeros((num_bins, height, width), np.float32).ravel()

    # normalize the event timestamps so that they lie between 0 and num_bins
    last_stamp = events[-1, 0]
    first_stamp = events[0, 0]
    deltaT = last_stamp - first_stamp

    if deltaT == 0:
        deltaT = 1.0

    events[:, 0] = (num_bins - 1) * (events[:, 0] - first_stamp) / deltaT
    ts = events[:, 0]
    xs = events[:, 1].astype(np.int)
    ys = events[:, 2].astype(np.int)
    pols = events[:, 3]
    pols[pols == 0] = -1  # polarity should be +1 / -1

    tis = ts.astype(np.int)
    dts = ts - tis
    vals_left = pols * (1.0 - dts)
    vals_right = pols * dts

    valid_indices = tis < num_bins
    np.add.at(voxel_grid, xs[valid_indices] + ys[valid_indices] * width
              + tis[valid_indices] * width * height, vals_left[valid_indices])

    valid_indices = (tis + 1) < num_bins
    np.add.at(voxel_grid, xs[valid_indices] + ys[valid_indices] * width
              + (tis[valid_indices] + 1) * width * height, vals_right[valid_indices])

    voxel_grid = np.reshape(voxel_grid, (num_bins, height, width))

    return voxel_grid


def read_dvs_event_fix_duration(path_to_event_file: str, duration_us: int, start_index: int):

    print('==>> Will use fixed duration event windows of size {:.2f} us'.format(duration_us))
    file_extension = splitext(path_to_event_file)[1]
    assert(file_extension in ['.txt'])
    event_file = open(path_to_event_file, 'r')
    event = event_file.readlines()

    # import pdb 
    # pdb.set_trace() 

    # ignore header + the first start_index lines
    # for i in range(start_index):
        

    # import pdb 
    # pdb.set_trace() 


    last_stamp = None
    duration_s = duration_us / 1000000.0
    event_list = []
    for line in event:
        t, x, y, pol = line.split(' ')
        t, x, y, pol = float(t), int(x), int(y), int(pol)
        event_list.append([t, x, y, pol])

        if last_stamp is None:
            last_stamp = t

        if t > last_stamp + duration_us:
            last_stamp = t
            event_window = np.array(event_list)

    
    return event_window




def save_event_to_img(path_to_event_file: str, event_window: list, width:int, height:int):

    frame = np.zeros((height, width)) #event_window[-1,0] - event_window[0,0] 
    for i in range(0*int(event_window.shape[0]/64), 64*int(event_window.shape[0]/64)): 
        frame[int(event_window[i][2]), int(event_window[i][1])] = 1 
    
    frame = frame.astype(np.float)*255
    img = Image.fromarray(frame)
    img = img.convert('1')
    img.save(path_to_event_file)




path_to_events = '/home/wangxiao/Documents/rgb_event_tracking_benchmark/v2e/output/airboard_1/v2e-dvs-events.txt'
save_event_path = '/home/wangxiao/Documents/rgb_event_tracking_benchmark/v2e/output/airboard_1/event_frames/' 

# read fixed event number
start_index = 0
num_bins = 5
width = 346
height = 260
N = 10000

event_tensor_iterator = pd.read_csv(path_to_events, delim_whitespace=True, header=None, names=['t', 'x', 'y', 'pol'],
                                        dtype={'t': np.float64, 'x': np.int16, 'y': np.int16, 'pol': np.int16},
                                        engine='c',
                                        skiprows=start_index, chunksize=N, nrows=None)


### (1) voxel  from  "High Speed and High Dynamic Range Video with an Event Camera"

# for event_tensor_pd in event_tensor_iterator:
#     event_tensor = events_to_voxel_grid(event_tensor_pd.values, num_bins=num_bins, width=width, height=height)
#     event_tensor = torch.from_numpy(event_tensor)

# read fixed event duration
duration_us = 100

print("==>> Loading txt file ... ")
event_window = read_dvs_event_fix_duration(path_to_events, duration_us, start_index)

# import pdb 
# pdb.set_trace()

print("==>> Begin to save file .... ")
save_event_to_img(save_event_path, event_window, width, height)  ### (2) event img 


