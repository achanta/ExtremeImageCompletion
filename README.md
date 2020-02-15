# Extreme Image Completion

```
@inproceedings{achanta_extreme_2017,
author={R. {Achanta} and N. {Arvanitopoulos} and S. {Süsstrunk}},
booktitle={IEEE International Conference on Acoustics, Speech, and Signal Processing (ICASSP)},
title={Extreme Image Completion},
year={2017},
}
```

It is challenging to complete an image whose 99% pixels are randomly missing. This repository contains code related to the two algorithms of Filtering by Adaptive Normalization (FAN) and Efficient Filtering by Adaptive Normalization (EFAN) that solve this problem efficiently. As opposed to existing techniques, EFAN has a computational complexity that is linear in the number of pixels of the full image and is real-time in practice. For comparable quality of reconstruction, our algorithms are thus almost 2 to 5 orders of magnitude faster than existing techniques.

The Python demo file provided can be used, for example, as:
```
python lena.png 0.01 lena_fan.png
```
The value 0.01 is the fraction of pixels retained from the original image to recreate the image.

An example of image completion of an image is shown below:

<p float="center">
  <img src="https://github.com/achanta/ExtremeImageCompletion/blob/master/images/lena.png" width="200" />
  <img src="https://github.com/achanta/ExtremeImageCompletion/blob/master/images/lena_001.png" width="200" /> 
  <img src="https://github.com/achanta/ExtremeImageCompletion/blob/master/images/lena_fan.png" width="200" /> 
</p>

Given a full input image (left), a sparse image containing only 1 percent pixels is created (middle) and then completed (right).


