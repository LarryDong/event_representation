# event_representation

Event-based camera data representation.  
Some popular representation and their demo codes.



## Current Presentation 

### event frame
**Event frame** is the simplest representation. Considering polarity, each pixel in image would only be `+1/0/-1`, which means a `positive/no/negative` event occurs here.  
<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/event_frame.jpg" width="480" height="360" alt="event frame"/><br/>
</div>


### event accumulate frame
**Event accumulate frame** is sometimes called **event intensity frame**. Each pixel would be a number that indicate the intensity. For a uint8 image, the range would be (0, 255), where 128 means no events (or the same number of positive/negative events), >128 means more positive events occurred here, and vice versa.

<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/event_accumulate_frame.jpg" width="480" height="360" alt="event accumulate frame"/><br/>
</div>


### time-surface | surface of active events
**Time-surface** is also caled **surface of active events**, which include both `spatio` and `temporal` information. The value of each pixel should be 

$$image(x,y; t) = exp(-|t-T(x,y)| / \tau)$$

where $\tau$ is a tunable parameter that depends on the motion in the scene. `t` is the reference time, which could be 'local' or 'global'.

Check [this paper](https://www.neuromorphic-vision.com/public/publications/1/publication.pdf) for more details. 

<div align=center>
<img src="https://raw.githubusercontent.com/LarryDong/event_representation/main/figure/time_surface.jpg" width="480" height="360" alt="time_surface"/><br/>
</div>


## Acknowledgement
Some codes are inspired by TU Berlin's Course: [https://github.com/tub-rip/events_viz](https://github.com/tub-rip/events_viz)
