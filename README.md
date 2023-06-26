# event_representation

Event-based camera data representation. (In some papers, also called "**Event Stacking**")  
Some popular representation and (maybe) their demo codes.

**If you see other representation (paper or code),  please tell me or make a pull request to this repo. Many thanks**


# Current Presentation 

## event frame
**Event frame** is the simplest representation. Considering polarity, each pixel in image would only be `+1/0/-1`, which means a `positive/no/negative` event occurs here.  
<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/event_frame.jpg" width="480" height="360" alt="event frame"/><br/>
</div>
## event accumulate frame
**Event accumulate frame** is sometimes called **event intensity frame**, or **histogram of events[1]**. Each pixel would be a number that indicate the intensity. For a uint8 image, the range would be (0, 255), where 128 means no events (or the same number of positive/negative events), >128 means more positive events occurred here, and vice versa.  
<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/event_accumulate_frame.jpg" width="480" height="360" alt="event accumulate frame"/><br/>
</div>

## time-surface | surface of active events
**Time-surface** is also caled **surface of active events**, which include both `spatio` and `temporal` information. The value of each pixel should be $$image(x,y; t) = exp(-|t-T(x,y)| / \tau)$$, where $\tau$ is a tunable parameter that depends on the motion in the scene. `t` is the reference time, which could be 'local' or 'global'.  
Check [this paper](https://www.neuromorphic-vision.com/public/publications/1/publication.pdf) for more details.   
**Draw time-surface in 2d image**
<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/time_surface.jpg" width="480" alt="time_surface"/><br/>
</div>

**Draw time-surface as a 3d grid**  
To plot time surface in a 3d grid, check `plot_3d_grid.py` file.  
Attention that plot 3d grid needs much memory, so just try to plot a patch in full image.  
Also, since the global reference time is used for whole image, the local time-surface may be not "smooth". 
<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/3dts-sample.png" width="640" alt="time_surface"/><br/>
</div>

### adaptive time-surface 
There are lots of adaptive/modified time-surface. I just list some of them when I saw them in papers.  
1. Varying decay parameter.
For naive TS, the decay parameter $\tau$ is constant. While some use this $\tau = max(\tau_u - \frac{1}{n} \Sigma_{i=0}^{n}(t-t_{last,i}), \tau_l)$, which make TS decay faster in dense texture, while slower in low-texture scene. Reference: [14].

<div align=center>
<img src="https://github.com/LarryDong/event_representation/assets/14933902/1d2f5e70-4be1-49c9-a42d-f2eaec5e98b0" width="480" alt="adaptive time_surface"/><br/>
</div>
3. 

## spatiol-temporal voxel grid
**spatiol-temporal voxel grid**, sometimes called **Stacking Based on Time(SBT)**, **Stacking Based on Number(SBN)**.   
First proposed by Alex Zhu's [paper](https://openaccess.thecvf.com/content_eccv_2018_workshops/w36/html/Zhu_Unsupervised_Event-based_Optical_Flow_using_Motion_Compensation_ECCVW_2018_paper.html)[2].  
Widely used in learning-methods to "**stacking**", such as `E2VID`[3], reconstruction method[4] and HDR imaging[5].  
These methods all stack events into frames for networking processing, but may be slightly different. In Zhu's method (and E2VID's), timestamp information are reserved when drawing the gray-scale image, but **SBT/SBN** in [4] only accumulate polarity ignoring the timestamps, and in [5] positive and negative polarity stacking are separated and frames are doubled. How to stack depends mainly on the network architecture I guess.  
No reference codes now. Will be add if I find an elegant implementation.

## 3D graph representation
First proposed by Yin Bi in his ICCV19 and TIP20 papers[8,9]. Also appeared in Yongjian Deng's [6] [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Nam_Stereo_Depth_From_Events_Cameras_Concentrate_and_Focus_on_the_CVPR_2022_paper.html), and Simon Schaefer's paper[10] in CVPR2022.  
The key idea is to use a 3D graph to orgnize event stream for further processing (like classification).  
Steps: 1. Voxelize the event stream; 2. Select N important voxels (based on the number of events in each voxel) for denoise; 3. Calcuate the 2D histgram as the feature vector in each voxel; 4. The 3D coordinate, and the feature, construct a `Vertex` in a graph; 5. Data association and further processing can be dealed by graph (see paper for more details).
<div align=center>
<img src="https://user-images.githubusercontent.com/14933902/177023036-ad985aa3-7930-4eda-841d-b92437c1b6bc.png" width="720" alt="3D graph"/><br/>
</div>

## Multi-density series of stack

First proposed by Yeongwoo Nam in CVPR2022 [7] [Paper](https://openaccess.thecvf.com/content/CVPR2022/html/Nam_Stereo_Depth_From_Events_Cameras_Concentrate_and_Focus_on_the_CVPR_2022_paper.html)
Traditional SBT or SBN methods may cause events overwrite when the scene is dense, especially for autonomous driving. The proposed methods uses M stack and each reserve the half of duration of previous stack. Older events are not preserved since the information is less important the the new ones.  
The multiple stacks can be further processed by other network (such as 'generate' a sharp map described in [7]).
<div align=center>
<img src="https://user-images.githubusercontent.com/14933902/177671089-ce35b57d-2a5d-4b9a-9990-bf10f038c3f8.png" width="640" alt="3D graph"/><br/>
</div>

## Binary Event History Image (BEHI)
BEHI representation is first proposed in Wang's IROS2022 paper [11]. This representation draws all events (without polarity) in one frame during the whole histroy time $T$, Defined by: $$I_T(x,y) = (\sum_{i=1}^N[x_i=x, y_i=y, t_i \lt T]) \gt 0$$ 
<div align=center>
<img src="https://user-images.githubusercontent.com/14933902/201467925-eeb6b479-2bee-413b-bf76-69fbe95cd05d.png" width="640" alt="BEHI"/><br/>
</div>
This representation can be used to predict the future position of a moving object with less data (only 1 binary frame). The above image shows a BEHI when a ball is flying towards a robot camera. Please check the paper for more details (the collision position & time can be estimated by a network).

## Tencode
Tencode is first proposed in Huang's WACV2023 paper [12]. This method ecnodes both polarity and timestamp into a RGB image. The on/off polarity encode R and B channel, and timestamp encodes the G channel. Given a time duration $\Delta t$, the output frame is defined by: $$F(x,y)=(255, \frac{255(t_{max}-t)}{\Delta t}, 0), if \quad p=1$$ $$F(x,y)=(0, \frac{255(t_{max}-t)}{\Delta t}, 255), if \quad p=0$$
<div align=center>
<img src="https://user-images.githubusercontent.com/14933902/224537529-76323c9b-eda2-44f2-b44b-a473a09ac487.png" width="480" alt="Tencode"/><br/>
</div>

## Sparse but varying pixels
Proposed in Tobias Fische's ICRA2023 paper [13]. Used for place recognition. 
<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/SparseVaryingPixel.png" width="480" alt="Tencode"/><br/>
</div>


# TODO:
- C++ version may be added later.
- Some other presentations would be added later.


# Acknowledgement
Some codes are inspired by TU Berlin's Course: [https://github.com/tub-rip/events_viz](https://github.com/tub-rip/events_viz)



# Reference 
[1]. Liu et al., Adaptive Time-Slice Block-Matching Optical Flow Algorithm for Dynamic Vision Sensors, BMVC 2018  
[2]. Zihao Zhu, et al. Unsupervised Event-based Optical Flow using Motion Compensation, ECCVW 2018  
[3]. H. Rebecq, R. Ranftl, V. Koltun and D. Scaramuzza, "High Speed and High Dynamic Range Video with an Event Camera," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 43, no. 6, pp. 1964-1980, 1 June 2021, doi: 10.1109/TPAMI.2019.2963386.  
[4]. Mostafavi, M., Wang, L. & Yoon, KJ. Learning to Reconstruct HDR Images from Events, with Applications to Depth and Flow Prediction. Int J Comput Vis 129, 900–920 (2021).  
[5]. Yunhao Zou; Yinqiang Zheng; Tsuyoshi Takatani; Ying Fu: Learning To Reconstruct High Speed and High Dynamic Range Videos From Events.  
[6]. Yongjian Deng; Hao Chen; Hai Liu; Youfu Li: A Voxel Graph CNN for Object Classification With Event Cameras. CVPR2022.  
[7]. Yeongwoo Nam; Mohammad Mostafavi; Kuk-Jin Yoon; Jonghyun Choi: Stereo Depth From Events Cameras: Concentrate and Focus on the Future. CVPR022.  
[8]. Yin Bi, Aaron Chadha, Alhabib Abbas, Eirina Bourtsoulatze, and Yiannis Andreopoulos. Graph-based object classification for neuromorphic vision sensing. IEEE Int. Conf. Comput. Vis. (ICCV), 2019  
[9]. Yin Bi, Aaron Chadha, Alhabib Abbas, Eirina Bourtsoulatze, and Yiannis Andreopoulos. Graph-based spatio-temporal feature learning for neuromorphic vision sensing. IEEE Transactions on Image Processing, 29:9084–9098, 2020.  
[10]. Simon Schaefer; Daniel Gehrig; Davide Scaramuzza: AEGNN: Asynchronous Event-Based Graph Neural Networks. CVPR2022. [11]. Wang, Ziyun; Ojeda, Fernando Cladera; Bisulco, Anthony; Lee, Daewon; Taylor, Camillo J.; Daniilidis, Kostas et al. (2022): EV-Catcher: High-Speed Object Catching Using Low-Latency Event-Based Neural Networks. In IEEE Robot. Autom. Lett. 7 (4), pp. 8737–8744. DOI: 10.1109/LRA.2022.3188400. 
[12]. Ze Huang, Li Sun, Cheng Zhao, Song Li, and Songzhi Su. EventPoint: Self-Supervised Interest Point Detection and Description for Event-based Camera. WACV 2023.
[13]. and Michael Milford. How Many Events Do You Need. Event-based Visual Place Recognition Using Sparse But Varying Pixels. ICRA 2023.
[14]. Zhu S, Tang Z, Yang M, et al. Event Camera-based Visual Odometry for Dynamic Motion Tracking of a Legged Robot Using Adaptive Time Surface[J]. arXiv preprint arXiv:2305.08962, 2023.
