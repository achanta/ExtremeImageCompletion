'''
----------------------------------------------------------
EXTREME IMAGE COMPLETION

This is a demo file for the Filtering by Adaptive
Normalization (FAN) algorithm
----------------------------------------------------------
Copyright (C) 2020 Ecole Polytechnique Federale de Lausanne
File created by Radhakrishna Achanta

This file is meant to demonstrate the extreme imgage completion
algorithm called Filtering by Adaptive Normalization (FAN) presented
the paper:

"Extreme Image Completion", Radhakrishna Achanta, Nikolaos
Arvanitopoulos, Sabine Susstrunk. ICASSP 2017, New Orleans, USA.

-----------------------------
EXAMPLE USAGE:
python lena.png 0.01 lena_demo.png
-----------------------------
'''

import numpy as np
from math import sqrt
from PIL import Image
from numpy.fft import fft2,ifft2,ifftshift
# import argparse
from sys import argv
from timeit import default_timer as timer



def fftblur(img, sigma):
    h,w = img.shape

    X,Y= np.meshgrid(np.arange(w),np.arange(h));
    X,Y = X-w//2,Y-h//2
    Z = np.exp(-0.5*(X**2 + Y**2)/(sigma**2))
    Z = Z/Z.sum()

    out = ifftshift(ifft2( fft2(img)*fft2(Z) ))
    return out


def fan_func(sparse_img, mask, num_kept):

    N = np.prod(mask.shape)
    sigma = sqrt(N/(np.pi*num_kept))

    r = fftblur(sparse_img[0],sigma)
    g = fftblur(sparse_img[1],sigma)
    b = fftblur(sparse_img[2],sigma)
    i = fftblur(mask,sigma)

    r = np.abs(r/i)
    g = np.abs(g/i)
    b = np.abs(b/i)

    img = np.dstack((r,g,b)).astype(np.uint8)

    return img

def sparsify(img,num_kept):

    dims = img.shape
    c,h,w = dims[0],dims[1], dims[2]

    rand_inds = np.random.permutation(np.arange(h*w))

    xvals = rand_inds[:num_kept]%w
    yvals = rand_inds[:num_kept]//w

    mask = np.zeros((h,w))
    mask[yvals,xvals] = 1

    sparse_img = np.zeros(dims,dtype=np.uint8)
    sparse_img[:,yvals,xvals] = img[:,yvals,xvals]

    return sparse_img, mask


def main():
    
    inp_img_name = "lena.png"
    percentage = 0.01
    out_img_name = "lena_fan.png"

    if len(argv) < 2:
        print("Usage: python inp_img_name [percentage] [out_img_name]")
        return

    if len(argv) > 1: inp_img_name = argv[1]
    if len(argv) > 2: percentage = np.float32(argv[2])
    if len(argv) > 3: out_img_name = argv[3]


    img = Image.open(inp_img_name)
    img = np.asarray(img)

    dims = img.shape
    h,w,c = dims[0],dims[1],1

    if len(dims) == 3:
        c = dims[2]
        img = img.transpose(2,0,1)

    num_kept = int(np.ceil(percentage*w*h))

    sparse_img, mask = sparsify(img,num_kept)

    start = timer()
    #------------------------------------------
    outimg = fan_func(sparse_img,mask,num_kept)
    #------------------------------------------
    end = timer()

    print("Saved:", out_img_name)
    print("Time taken in seconds: ", end-start)
    
    Image.fromarray(outimg).save(out_img_name)

    # save sparse image if needed
    # Image.fromarray(sparse_img.transpose(1,2,0)).save("sparse.png")
    
    return



main()
