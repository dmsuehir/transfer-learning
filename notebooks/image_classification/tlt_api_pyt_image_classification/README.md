# Transfer Learning for PyTorch Image Classification using the Intel® Transfer Learning Tool API

This notebook demonstrates how to use the Intel Transfer Learning Tool API to do transfer learning for
image classification using PyTorch.

The notebook performs the following steps:
1. Import dependencies and setup parameters
1. Get the model
1. Get the dataset
1. Prepare the dataset
1. Predict using the original model
1. Transfer learning
1. Predict
1. Export

## Running the notebook

To run the notebook, follow the instructions to setup the [PyTorch notebook environment](/notebooks/setup.md).

To use Gaudi for training and inference, install required software for Intel Gaudi: 
1.  Temporarily uninstall torch
```
# Torch will later be re-installed below
pip uninstall torch
```
2.  Install the Gaudi Intel SW Stack
```
wget -nv https://vault.habana.ai/artifactory/gaudi-installer/1.15.0/habanalabs-installer.sh
chmod +x habanalabs-installer.sh
sudo apt-get update
```
```
# Note: This may not be required depending on what is already installed on your machine
./habanalabs-installer.sh install --type base
```
3.	Install the Gaudi Intel Pytorch environment
```
# Note: This step may not be required depending on what is already installed on your machine
./habanalabs-installer.sh install -t dependencies
```
```
./habanalabs-installer.sh install --type pytorch –venv
```

See [Habana Docs](https://docs.habana.ai/en/latest/Installation_Guide/SW_Verification.html) for detailed installation instructions

## References

Dataset citations
```
@ONLINE {tfflowers,
author = "The TensorFlow Team",
title = "Flowers",
month = "jan",
year = "2019",
url = "http://download.tensorflow.org/example_images/flower_photos.tgz" }

@ONLINE {CIFAR10,
author = "Alex Krizhevsky",
title = "CIFAR-10",
year = "2009",
url = "http://www.cs.toronto.edu/~kriz/cifar.html" }

@article{openimages,
  title={OpenImages: A public dataset for large-scale multi-label and multi-class image classification.},
  author={Krasin, Ivan and Duerig, Tom and Alldrin, Neil and Veit, Andreas and Abu-El-Haija, Sami
    and Belongie, Serge and Cai, David and Feng, Zheyun and Ferrari, Vittorio and Gomes, Victor
    and Gupta, Abhinav and Narayanan, Dhyanesh and Sun, Chen and Chechik, Gal and Murphy, Kevin},
  journal={Dataset available from https://github.com/openimages},
  year={2016}
}
```
Model citations
```
@misc{yalniz2019billionscale,
    title={Billion-scale semi-supervised learning for image classification},
    author={I. Zeki Yalniz and Hervé Jégou and Kan Chen and Manohar Paluri and Dhruv Mahajan},
    year={2019},
    eprint={1905.00546},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

