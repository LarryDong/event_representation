# event_representation

Event-based camera data representation.  
Some popular representation and their demo codes.

**If you see other representation (paper or code),  please tell me or make a pull request to this repo. Many thanks**


# Current Presentation 

### event frame
**Event frame** is the simplest representation. Considering polarity, each pixel in image would only be `+1/0/-1`, which means a `positive/no/negative` event occurs here.  
<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/event_frame.jpg" width="480" height="360" alt="event frame"/><br/>
</div>


### event accumulate frame
**Event accumulate frame** is sometimes called **event intensity frame**, or **histogram of events[1]**. Each pixel would be a number that indicate the intensity. For a uint8 image, the range would be (0, 255), where 128 means no events (or the same number of positive/negative events), >128 means more positive events occurred here, and vice versa.

<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/event_accumulate_frame.jpg" width="480" height="360" alt="event accumulate frame"/><br/>
</div>


### time-surface | surface of active events
**Time-surface** is also caled **surface of active events**, which include both `spatio` and `temporal` information. The value of each pixel should be $$image(x,y; t) = exp(-|t-T(x,y)| / \tau)$$, where $\tau$ is a tunable parameter that depends on the motion in the scene. `t` is the reference time, which could be 'local' or 'global'.  
Check [this paper](https://www.neuromorphic-vision.com/public/publications/1/publication.pdf) for more details. 

**Draw time-surface in 2d image**

<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/time_surface.jpg" width="480" height="360" alt="time_surface"/><br/>
</div>

**Draw time-surface as a 3d grid**

To plot time surface in a 3d grid, check `plot_3d_grid.py` file.  
Attention that plot 3d grid needs much memory, so just try to plot a patch in full image.  
Also, since the global reference time is used for whole image, the local time-surface may be not "smooth". 

<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/3dts-sample.png" width="9600" height="480" alt="time_surface"/><br/>
</div>


# TODO:
- C++ version may be added later.
- Some other presentations would be added later. Includes:  
**spatiol-temporal voxel grid**: proposed by Alex Zhu's [paper](https://openaccess.thecvf.com/content_eccv_2018_workshops/w36/html/Zhu_Unsupervised_Event-based_Optical_Flow_using_Motion_Compensation_ECCVW_2018_paper.html)[2] and used in many framework like `e2vid`




# Acknowledgement
Some codes are inspired by TU Berlin's Course: [https://github.com/tub-rip/events_viz](https://github.com/tub-rip/events_viz)


# Reference 
[1]. Liu et al., Adaptive Time-Slice Block-Matching Optical Flow Algorithm for Dynamic Vision Sensors, BMVC 2018  
[2]. Zihao Zhu, et al. Unsupervised Event-based Optical Flow using Motion Compensation, ECCVW 2018
