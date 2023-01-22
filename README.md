# ai_house_fake_news_detection

# Setup Working Environment  

## Pre-requirements 

- conda 4.12.0 (later versions may also work) - [Installation](https://docs.anaconda.com/anaconda/install/index.html)
- VS Code - [Ubuntu Installation](https://code.visualstudio.com/docs/setup/linux)
- (Optional) CUDA Version: 11.4; Driver Version: 470.129.06 - [Installation](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)

## Setup environment 

If you have CUDA
```bash
conda env create -f environment_gpu.yaml
```
Otherwise
```bash
conda env create -f environment.yaml
```

# Start Jupyter

You may use any port 
```bash
jupyter lab --port 7766
```

# Content 

- [Workshop](https://github.com/VSydorskyy/ai_house_fake_news_detection/blob/main/workshop/AI_House_workshop.ipynb). Colab [link](https://colab.research.google.com/drive/16eFSJMhVYYBo1WhbhhkLBN6kWuXzTstf?usp=sharing)
- [Week 2 Session 1](https://github.com/VSydorskyy/ai_house_fake_news_detection/blob/week_2/Week_2_Linear_and_Recurrent_models/Session_1_Text_Data_Representations.ipynb)

# Data

- For Lecture 2.1 we will use Kaggle datasets. [Prepare in advance](#how-to-use-kaggle-datasets)
    - Fake and real news dataset API command: `kaggle datasets download -d clmentbisaillon/fake-and-real-news-dataset`
    - Toxic Comment Classification Challenge API command: `kaggle competitions download -c jigsaw-toxic-comment-classification-challenge`

## How to use Kaggle datasets

1. Create Kaggle account 
2. Proceed [with Installation & Authentication](https://www.kaggle.com/docs/api#getting-started-installation-&-authentication)
3. Download dataset with API command 
