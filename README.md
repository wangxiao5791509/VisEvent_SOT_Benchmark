<div align="center">

<img src="https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/figures/visevent_art.jpg" width="600">
  
**The First Large-scale Benchmark Dataset for Reliable Object Tracking by fusing RGB and Event Cameras**

------

<p align="center">
  • <a href="https://sites.google.com/view/viseventtrack/">Project</a> •
  <a href="https://arxiv.org/abs/2108.05015">arXiv</a> • 
  <a href="https://github.com/wangxiao5791509/RGB-DVS-SOT-Baselines">Baselines</a> •
  <a href="https://youtu.be/U4uUjci9Gjc">DemoVideo</a> • 
  <a href="https://youtu.be/vGwHI2d2AX0">Tutorial</a> •
</p>

</div>

> **VisEvent: Reliable Object Tracking via Collaboration of Frame and Event Flows[J]** arXiv preprint arXiv:2108.05015, 2021, Xiao Wang, Jianing Li, Lin Zhu, Zhipeng Zhang, Zhe Chen, Xin Li, Yaowei Wang, Yonghong Tian, Feng Wu 




## News: 

* :fire: [2024.03.12] A New Long-term RGB-Event based Visual Object Tracking Benchmark Dataset (termed **FELT**) is available at
  [[Paper](https://arxiv.org/pdf/2403.05839.pdf)] 
  [[Code](https://github.com/Event-AHU/FELT_SOT_Benchmark)] 
  [[DemoVideo](https://youtu.be/6zxiBHTqOhE?si=6ARRGFdBLSxyp3G8)]  

* :fire: [2023.09.27] A High Definition (HD) Event based Visual Object Tracking Benchmark Dataset (termed **EventVOT**) is available at
[[arXiv](https://arxiv.org/abs/2309.14611)] [[Github](https://github.com/Event-AHU/EventVOT_Benchmark)] 

* :fire: [2023.09.20] VisEvent is accepted by IEEE Transactions on Cybernetics [[IEEE](https://ieeexplore.ieee.org/abstract/document/10284004)]

* :fire: [2022.11.27] Due to some aedat4 files are missing, you can use part of this dataset according to this list: [[aedat4HARDVS_list](https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/aedat4HARDVS_list.txt)]  

* :fire: [2022.11.23] A new Color Frame + Event Stream based Tracking dataset **COESOT** is available at 
[[arXiv](https://arxiv.org/abs/2211.11010)] [[GitHub](https://github.com/Event-AHU/COESOT)]

* :fire: [2022.10.19] Event camera (DVS, Spike) based Papers Published on Top International Conference [[
Event_Camera_in_Top_Conference](https://github.com/Event-AHU/Event_Camera_in_Top_Conference)]

* [2022.07.14] Update the VOT2019-RGB-Event dataset used in our paper [BaiduYun]. 

* [2022.02.10] Update paper list for event camera based tracking [[Event_Tracking_Paper_List](https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/Event_Tracking_Paper_List.md)]. 

* [2021.10.13] Update the links for onedrive. 



## Introduction 
Different from visible cameras which record intensity images frame by frame, the biologically inspired event camera produces a stream of asynchronous and sparse events with much lower latency. In practice, the visible cameras can better perceive texture details and slow motion, while event cameras can be free from motion blurs and have a larger dynamic range which enables them to work well under fast motion and low illumination. Therefore, the two sensors can cooperate with each other to achieve more reliable object tracking. In this work, we propose a large-scale Visible-Event benchmark (termed VisEvent) due to the lack of a realistic and scaled dataset for this task. Our dataset consists of 820 video pairs captured under low illumination, high speed, and background clutter scenarios, and it is divided into a training and a testing subset, each of which contains 500 and 320 videos, respectively. Based on VisEvent, we transform the event flows into event images and construct more than 30 baseline methods by extending current single-modality trackers into dual-modality versions. More importantly, we further build a simple but effective tracking algorithm by proposing a cross-modality transformer, to achieve more effective feature fusion between visible and event data. Extensive experiments on the proposed VisEvent dataset, and two simulated datasets (i.e., OTB-DVS and VOT-DVS), validated the effectiveness of our model. 


## Demo Video
A demo video for the VisEvent can be found by cliking the image below: 
<p align="center">
  <a href="https://youtu.be/U4uUjci9Gjc">
    <img src="https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/figures/visevent_demoIMG.jpg" alt="VisEvent_DemoVideo" width="700"/>
  </a>
</p>

<p align="center">
  <a href="https://youtu.be/U4uUjci9Gjc">
    <img src="https://github.com/wangxiao5791509/RGB_Event_Tracking_Benchmark/blob/main/videosamples.png" alt="VisEvent_examples" width="700"/>
  </a>
</p>




## Video Tutorial
The tutorial for this paper can be found by cliking the image below: 
<p align="center">
  <a href="https://youtu.be/vGwHI2d2AX0">
    <img src="https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/figures/visevent_tutorial.jpg" alt="VisEvent_DemoVideo" width="700"/>
  </a>
</p>




## How to Download VisEvent Dataset? 

* **BaiduYun (about 216 GB):** 
```
Link：https://pan.baidu.com/s/1VhdORXT4OvG8TUESfDZHfw
Password：AHUE 
```

* **DropBox**:
```
https://www.dropbox.com/scl/fo/r406wsgll56fy0hhhwu62/AFo3cjXjSI4Dzjn5nlnXNW0?rlkey=ecgyd26j1ycfl1jbm4pwc3vbn&st=rzf95buf&dl=0
```


## Links for **VOT2019-RGB-Event dataset** (36.3 GB) used in our paper 

* **BaiduYun:**
```
Link：https://pan.baidu.com/s/1cS79d1dJFD8mF0AwuGG5Og   Password: AHUT 
```

* **Googledrive:**  Click [[here](https://drive.google.com/drive/folders/19kSDi1VcDWJ9Tpr1fw34LK50Nm4zR2u8?usp=sharing)]



## Baseline Methods
The source code of baseline trackers by fusing dual-modalities can be found at: [[RGB-DVS-SOT-Baselines](https://github.com/wangxiao5791509/RGB-DVS-SOT-Baselines)].

<p align="center">
  <a href="https://github.com/wangxiao5791509/RGB-DVS-SOT-Baselines">
    <img src="https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/figures/visevent_baselines.png" alt="VisEvent_Baselines" width="700"/>
  </a>
</p>


## How to load the aedat4 file? 
We provide a python script ([**read_aedat4.py**](https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/scripts/read_aedat4.py)) to load the aedat4 file. You can download one aedat4 file to feel the data style: [[dvSave-2021_12_21_16_32_19.aedat4](https://drive.google.com/file/d/1cMCVocWA3bfnIX1WlKqMNACWiYvFZ1rC/view?usp=share_link)]


Here is an example: 

1). Install the required toolkit [[**dv-gui**](https://inivation.gitlab.io/dv/dv-docs/docs/getting-started.html)]. Please use different scripts for various Ubuntu OS: 

**Ubuntu 20.04**:

    sudo add-apt-repository ppa:inivation-ppa/inivation
    sudo apt-get update
    sudo apt-get install dv-gui

**Ubuntu 18.04**: 

    sudo add-apt-repository ppa:ubuntu-toolchain-r/test
    sudo add-apt-repository ppa:inivation-ppa/inivation-bionic
    sudo apt-get update
    sudo apt-get install dv-gui

**Ubuntu 16.04**: 

    sudo add-apt-repository ppa:ubuntu-toolchain-r/test 
    sudo add-apt-repository ppa:lkoppel/opencv 
    sudo add-apt-repository ppa:janisozaur/cmake-update 
    sudo add-apt-repository ppa:inivation-ppa/inivation-xenial 
    sudo apt-get update 
    sudo apt-get install dv-gui

Other softwares:

    pip install dv
    pip install opencv-python numpy pillow -i https://pypi.tuna.tsinghua.edu.cn/simple 

[ref] [https://gitlab.com/inivation/dv/dv-python](https://gitlab.com/inivation/dv/dv-python)

2). Open your terminal and run the script: 

    python read_aedat4.py










## Evaluation ToolKit 
Only matlab version is available. 

**1. Download this github:**
    
    git clone https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark

**2. Download the tracking results of our benchmark:**
[[**GoogleDrive (185MB)**](https://drive.google.com/file/d/1fILCNMrwt2PiITPWIQFZpk1PJvg_JAjX/view?usp=sharing)]

    unzip tracking_results_VisEvent_SOT_benchmark.zip, and put it into the folder "tracking_results". 

    unzip the "annos.zip" in the folder "annos"

**3. Open your matlab, and run the script "Evaluate_VisEvent_SOT_benchmark.m". Wait and check the final evaluated figures**

<img src="res_fig/VisEvent_benchmark_results.png" width="650"> 






## More Related Materials 
* [**Github-1**] https://github.com/wangxiao5791509/SNN_CV_Applications_Resources 
* [**Github-2**] https://github.com/uzh-rpg/event-based_vision_resources 
* [**Github-3**] https://github.com/wangxiao5791509/Single_Object_Tracking_Paper_List
* [**Survey**] **神经形态视觉传感器的研究进展及应用综述**，计算机学报，李家宁, 田永鸿 [[Paper](https://drive.google.com/file/d/1d7igUbIrEWxmUI7xq75P6h_I4H7uI3FA/view?usp=sharing)] 
* [**Survey**] **Event-based Vision: A Survey**, Guillermo Gallego, et al., IEEE T-PAMI 2020, [[Paper](https://arxiv.org/abs/1904.08405)]
* [**Survey**] **Deep Learning for Event-based Vision: A Comprehensive Survey and Benchmarks**, Xu Zheng, Yexin Liu, Yunfan Lu, Tongyan Hua, Tianbo Pan, Weiming Zhang, Dacheng Tao, Lin Wang, [[Paper](https://arxiv.org/abs/2302.08890)] 

* [**FE108 dataset**] **Object Tracking by Jointly Exploiting Frame and Event Domain**, Jiqing Zhang, et al., ICCV 2021, 
[[Project](https://zhangjiqing.com/dataset/)] [[added 33 videos, FE240 dataset, Baidu Cloud: password 68x3](https://pan.baidu.com/s/1gpAdfQ5Eb_GhhCDJlK3j2w)]
[[DemoVideo](https://www.youtube.com/watch?v=EeMRO8XVv04&ab_channel=JiqingZhang)] 
[[Github](https://github.com/Jee-King/ICCV2021_Event_Frame_Tracking)] 
[[Dataset](https://zhangjiqing.com/dataset/contact.html)] 
[[Paper](https://arxiv.org/pdf/2109.09052.pdf)]
[[Baiduyun](链接：https://pan.baidu.com/s/1GFfCULGbSiv7FWCKgkb8_g 提取码：AHUT)]
* [**SpikingJelly**] (SpikingJelly is an open-source deep learning framework for Spiking Neural Network (SNN) based on PyTorch) [[OpenI from PCL](https://git.openi.org.cn/OpenI/spikingjelly)] [[GitHub](https://github.com/fangwei123456/spikingjelly)] [[Documents](https://spikingjelly.readthedocs.io/zh_CN/latest/)]
* [**Event-Toolkit**] https://github.com/TimoStoff/event_utils (Various representations can be obtained with (a) the raw events, (b) the voxel grid, (c) the event image, (d) the timestamp image.)
* [**aedat 2.0.1**] AEDAT is a fast AEDAT 4 python reader, with a Rust underlying implementation. Run **pip install aedat** to install it. 
[[pypi.org](https://pypi.org/project/aedat/)] [[Github](https://github.com/neuromorphicsystems/aedat)]



<img src="res_fig/event_representations.png" width="650"> 





## License
This project is under the MIT license. See [[license](https://github.com/wangxiao5791509/VisEvent_SOT_Benchmark/blob/main/License)] for details. 


## :page_with_curl: BibTex: 
If you find this work useful for your research, please cite the following papers: 

```bibtex
@article{wang2021viseventbenchmark,
  title={VisEvent: Reliable Object Tracking via Collaboration of Frame and Event Flows},
  author={Xiao Wang, Jianing Li, Lin Zhu, Zhipeng Zhang, Zhe Chen, Xin Li, Yaowei Wang, Yonghong Tian, Feng Wu},
  journal={arXiv:2108.05015},
  year={2021}
}
```

If you have any questions about this work, please submit an issue or contact me via **Email**: wangxiaocvpr@foxmail.com, xiaowang@ahu.edu.cn, or **Wechat**: wangxiao5791509. Thanks for your attention! 


















