# Read .aedat4 file from DAVIS346 at the temporal window (t1-t2), obtaining events, frames for hdf5.
# Jianing Li, Peking university, lijianing@pku.edu.cn, Sep. 1st, 2020.

import argparse
import os
import numpy as np
from dv import AedatFile
import xlrd
import h5py

parser = argparse.ArgumentParser(
    description='Read the .aedat file from DAVIS346.')

parser.add_argument(
    '-n',
    '--neuromorphic_file',
    default = './tables/neuromorphic_data_file.xlsx',
    help='the .xlsx file path'
    )


def get_events_frames(input_file, start_time, end_time):
    """
    getting event, frames, frame timestamps from DAVIS346 streams during the temporal window (start-end).
    args :
        - input_file: .aedat4 file.
        - start_time, end_time: the temporal window.
    return:
        - aer_events: timestamp, x, y, polarity.
        - frames: color APS in DAVIS346.
        - frame_timestamps: the timestamps in frames
    """
    with AedatFile(input_file) as f:
        # get events
        all_events = np.hstack([event for event in f['events'].numpy()])
        timestamps = all_events['timestamp']
        index_1 = int(np.searchsorted(np.array(timestamps), start_time))
        index_2 = int(np.searchsorted(np.array(timestamps), end_time))
        events = all_events[index_1:index_2]
        events['timestamp'] = events['timestamp'] -start_time
        new_events = np.copy(events)
        aer_events = [(new_event[0], new_event[1], new_event[2], new_event[3]) for new_event in new_events]
        aer_type = {'names': ('timestamp', 'x', 'y', 'polarity'), 'formats': ('i8', 'i2', 'i2', 'i1')}
        aer_events = np.array(aer_events, dtype=aer_type)

        # get images
        frames = []
        frame_timestamps = []
        for frame in f['frames']:
            if frame.timestamp > start_time and frame.timestamp < end_time:
                frames.append(frame.image)
                frame_timestamps.append(frame.timestamp-start_time)

        return aer_events, frames, frame_timestamps


def davis_to_hdf5(output_hdf5_file, aer_events, frames, frame_timestamps):
    """
    Generating .hdf5 file for DAVIS346 camera.
    args :
        - output_hdf5_file: the output hdf5 file.
        - events: events in DAVIS346.
        - frames: images in DAVIS346.
        - frame_timestamps: the timestamp for each image.
    return:
        the .hdf5 file.
    """
    with h5py.File(output_hdf5_file, 'w') as f:
        f.create_dataset('events', data = aer_events) # save events
        f.create_dataset('frames', data= frames) # save frames
        f.create_dataset('frame_timestamps', data=frame_timestamps) # save frame timestamp
        f.close()
    print('The {} file has been generated!'.format(output_hdf5_file))


def _main(args):
    input_file=os.path.expanduser(args.neuromorphic_file)
    neuromorphic_file = xlrd.open_workbook(input_file)
    neuromorphic_information = neuromorphic_file.sheet_by_name('neuromorphic_dataset')
    sequence_names = neuromorphic_information.col_values(0)[1:]
    temporal_lengths = neuromorphic_information.col_values(1)[1:]
    start_timestamps = neuromorphic_information.col_values(4)[1:]

    #for i in range(141, 142):
    for i in range(1):
        #for i in range(len(sequence_names)):
        davis_file = '../DVS_data/{}.aedat4'.format(sequence_names[i])
        output_filename = './DVS_data_processing/{}.hdf5'.format(sequence_names[i])
        start_timestamp = int(start_timestamps[i])
        end_timestamp = int(start_timestamp) + int(temporal_lengths[i]*1e6)
        aer_events, frames, frame_timestamps = get_events_frames(davis_file, start_timestamp, end_timestamp)
        davis_to_hdf5(output_filename, aer_events, frames, frame_timestamps)

if __name__ == '__main__':
    _main(parser.parse_args())


