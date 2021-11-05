# event_representation

Event-based camera data representation.  
Some popular representation and their demo codes.



## Current Presentation 

**event frame** is the simplest representation. Considering polarity, each pixel in image would only be `+1/0/-1`, which means a `positive/no/negative` event occurs here.  

**event accumulate frame** is sometimes called **event intensity frame**. Each pixel would be a number that indicate the intensity. For a uint8 image, the range would be (0, 255), where 128 means no events (or the same number of positive/negative events), >128 means more positive events occurred here, and vice versa.

**time-surface** is also caled **surface of active events**, which include both `spatio` and `temporal` information. The value of each pixel should be 

$ image(x,y; t) = exp(-|t-T(x,y)| / \tau) $

where $\tau$ is a tunable parameter that depends on the motion in the scene. `t` is the reference time, which could be 'local' or 'global'

