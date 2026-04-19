# Deep Learning Projects

This repository contains multiple machine learning and deep learning projects, covering computer vision and recommendation systems.

---

## Projects

### 1. Movie Recommender System

* Content-based recommendation using NLP
* Text preprocessing, stemming, and feature engineering
* Vectorization using **CountVectorizer**
* Similarity computation using **cosine similarity**
* Deployed using **Streamlit Cloud**
* Large model/data handled via **Google Drive + gdown**

**Live Demo:**
https://deeplearning-xjsvngzjgpamjjajalwjd4.streamlit.app/

Folder: `Custom_Recommender_System/`

---

### 2. CIFAR Image Classification (CNN)

* Used:
  * Conv2D layers (RGB images)
  * Batch Normalization 
  * ReLU activation 
  * MaxPooling layers (reducing spatial dimensions)
  * Dropout (reduces overfitting)
  * Fully connected layers (multi-class classification)

* Data preprocessing:
  * Channel-wise normalization using CIFAR-10 (mean & std)
  * Handled **3-channel (RGB) images of size 32×32**
  
**Performance:**

* Test Accuracy: **77.6%**

Folder: `CIFAR_Project/`

---

### 3. MNIST Digit Classification (CNN)

* Implemented a **deep CNN architecture** using PyTorch
* Used:

  * Conv2D layers (feature extraction)
  * Batch Normalization (stable training)
  * Dropout (reduce overfitting)
  * Fully connected layers (classification)
    
* Data preprocessing:
  * Normalization using mean & std
  * Training with **GPU support : T4 GPU**

**Performance:**

* Test Accuracy: **99.2%**

Additional:

* Evaluated using **confusion matrix**
* Efficient training using **DataLoader batching**

Folder: `MNIST_Project/`

---

## Tech Stack

* Python
* PyTorch
* Pandas, NumPy
* Scikit-learn
* Streamlit

---

## Repository Structure

```text
Deep_Learning/
│
├── CIFAR_Project/
├── MNIST_Project/
├── Custom_Recommender_System/
│
├── README.md
└── .gitignore
```

---

## Future Improvements

* Improve model accuracy
* Hyper-tuning using optuna

---

## Author

Bhavik

