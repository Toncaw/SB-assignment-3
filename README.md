# SB-assignment-3
For this asignment we were learning about and implement last 2 steps in IBB recognition pipeline

# My work
1. Extracted my training dataset of ears using yolov4 from my prefious asignment
2. Augment my training dataset 
3. Augment perfectly_detected_ears dataset

Aumentation:
  - Blured the images with kernel 5x5
  - Sharpen the images with hernel([[0, -1, 0],
                                   [-1, 5, -1],
                                    [0, -1, 0]])
  - Equalized the luminocity of the images (covert from rgb to yuv and equalized the y heistogram)
  - Rotated all of the above pictures from -35° to 35° with 5° step
    - so total there are 15x3 new pictures for every ear 
 
 5. Trained my own CNN with help of Keras on my own training dataset (augmented).
 6. Trained  CNN with help of Keras on perfectly_detected_ears dataset (augmented).

  Training:
    - I trained the weights on google colab.
    - After some testing i realised that about 35 epoches deep the ram gets filled up and whole thing chrashes. (due to vast number of training data)
    - So i decided to save weights after 30 epochs (~15 min of training).
    
7. I Calculated the ranks and drew the CMC curve for trained models

# Results

| Model | Rank-1 | Rank-5 |
| pix-2-pix | 6,41 % | |
| CNN trained on my own dataset | 8.8 % | 26.4 % |
| CNN trained on perfectly_detected_ears dataset | 24.4 % | 45.6 % |

CMC Curve for  CNN trained on my own dataset:
![cmc_svoji](https://user-images.githubusercontent.com/79637072/149776572-3567da69-5709-46f8-b830-837157c010b3.png)

CMC Curve for CNN trained on perfectly_detected_ears dataset:
![cmc_perfect](https://user-images.githubusercontent.com/79637072/149776632-a1fc846d-5ecf-4074-b9e7-15a883a9af94.png)
