# VisEvent_SOT_Benchmark
The First Large-scale Benchmark Dataset for Reliable Object Tracking by fusing RGB and Event Cameras. 

**VisEvent: Reliable Object Tracking via Collaboration of Frame and Event Flows**, Xiao Wang, Jianing Li, Lin Zhu, Zhipeng Zhang, Zhe Chen, Xin Li, Yaowei Wang, Yonghong Tian, Feng Wu **[[Paper](https://arxiv.org/pdf/2108.05015.pdf)] [[Project](https://sites.google.com/view/viseventtrack/)] [[DemoVideo](https://www.youtube.com/watch?v=U4uUjci9Gjc)]** 


## Abstract 
Different from visible cameras which record intensity images frame by frame, the biologically inspired event camera produces a stream of asynchronous and sparse events with much lower latency. In practice, the visible cameras can better perceive texture details and slow motion, while event cameras can be free from motion blurs and have a larger dynamic range which enables them to work well under fast motion and low illumination. Therefore, the two sensors can cooperate with each other to achieve more reliable object tracking. In this work, we propose a large-scale Visible-Event benchmark (termed VisEvent) due to the lack of a realistic and scaled dataset for this task. Our dataset consists of 820 video pairs captured under low illumination, high speed, and background clutter scenarios, and it is divided into a training and a testing subset, each of which contains 500 and 320 videos, respectively. Based on VisEvent, we transform the event flows into event images and construct more than 30 baseline methods by extending current single-modality trackers into dual-modality versions. More importantly, we further build a simple but effective tracking algorithm by proposing a cross-modality transformer, to achieve more effective feature fusion between visible and event data. Extensive experiments on the proposed VisEvent dataset, and two simulated datasets (i.e., OTB-DVS and VOT-DVS), validated the effectiveness of our model. 


## Dataset Samples 
![visevent-example](https://github.com/wangxiao5791509/RGB_Event_Tracking_Benchmark/blob/main/videosamples.png)
The source code of baseline trackers by fusing dual-modalities can be found at: [[DualModality_SOT_Python3](https://github.com/wangxiao5791509/DualModality_SOT_Python3)]. 



## How to Download VisEvent Dataset? 
Currently, the dataset can be obtained from: 

[[**BaiduYun**]()] [[**GoogleDrive**]()] [[**OneDrive**]()] 


## Evaluation ToolKit 
Only matlab version is available. 

**1. Download this github:**
    
    git clone https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark

**2. Download the tracking results of our benchmark:**
[[**GoogleDrive (181.5MB)**](https://drive.google.com/file/d/1slfxEOtmSAQFRv_OmDeeoiiK1F-DqhEz/view?usp=sharing)]

    unzip tracking_results_VisEvent_SOT_benchmark.zip, and put it into the folder "tracking_results". 

**3. Unzip the "annos.zip" in the folder "annos"**

**4. Open your matlab, and run the script "Evaluate_VisEvent_SOT_benchmark.m"**

**5. Wait and check the final evaluated figures:**

![visevent-example](https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/res_fig/VisEvent_benchmark_results.png)








## More Related Materials 
* [**Github-1**] https://github.com/wangxiao5791509/SNN_CV_Applications_Resources 
* [**Github-2**] https://github.com/uzh-rpg/event-based_vision_resources 
* **神经形态视觉传感器的研究进展及应用综述**，计算机学报，李家宁, 田永鸿 [[Paper](https://drive.google.com/file/d/1d7igUbIrEWxmUI7xq75P6h_I4H7uI3FA/view?usp=sharing)] 
* **Event-based Vision: A Survey**, Guillermo Gallego, et al., IEEE T-PAMI 2020, [[Paper](https://arxiv.org/abs/1904.08405)]
* [**FE108 dataset**] **Object Tracking by Jointly Exploiting Frame and Event Domain**, Jiqing Zhang, et al., ICCV 2021, [[Project](https://zhangjiqing.com/dataset/)] [[DemoVideo](https://www.youtube.com/watch?v=EeMRO8XVv04&ab_channel=JiqingZhang)] 











## Citation: 
If you find this work useful for your research, please cite the following papers: 

~~~
@article{wang2021viseventbenchmark,
  title={VisEvent: Reliable Object Tracking via Collaboration of Frame and Event Flows},
  author={Xiao Wang, Jianing Li, Lin Zhu, Zhipeng Zhang, Zhe Chen, Xin Li, Yaowei Wang, Yonghong Tian, Feng Wu},
  journal={arXiv:2108.05015},
  year={2021}
}
~~~

If you have any questions about this work, please submit an issue or contact me via wangxiaocvpr@foxmail.com. Thanks for your attention! 


















