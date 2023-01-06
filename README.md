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