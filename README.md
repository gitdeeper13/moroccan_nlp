# moroccan_nlp

### Natural Language Processing: Linguistic Resources and Models for Moroccan Darija and Arabic

**DarijaBERT · Baseline Classifier · Linguistic Corpora · AI for Under-Resourced Languages**

---

[![PyPI version](https://img.shields.io/pypi/v/moroccan-nlp?color=1B4F72&label=PyPI&logo=pypi&logoColor=white)](https://pypi.org/project/moroccan-nlp)
[![PyPI downloads](https://img.shields.io/pypi/dm/moroccan-nlp?color=154360&label=Downloads&logo=pypi&logoColor=white)](https://pypi.org/project/moroccan-nlp/#files)
[![Python versions](https://img.shields.io/pypi/pyversions/moroccan-nlp?color=306998&logo=python&logoColor=white)](https://pypi.org/project/moroccan-nlp)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21154423-blue.svg)](https://doi.org/10.5281/zenodo.21154423)
[![OSF Preregistration](https://img.shields.io/badge/OSF-Preregistered-blue?logo=osf&logoColor=white)](https://doi.org/10.17605/OSF.IO/SXGC6)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0003--8903--0029-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0003-8903-0029)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Domain](https://img.shields.io/badge/Domain-Natural%20Language%20Processing-1B4F72)](https://doi.org/10.5281/zenodo.21154423)
[![Series](https://img.shields.io/badge/Series-GITDEEPER%20LAB%20ZERO%20V6-1A5276)](https://doi.org/10.5281/zenodo.21154423)
[![Version](https://img.shields.io/badge/Version-1.0.0-orange)](https://github.com/gitdeeper13/moroccan_nlp)

## 📌 Overview

**moroccan_nlp** is a comprehensive project dedicated to developing linguistic resources and Natural Language Processing (NLP) models for **Moroccan Darija** and **Arabic**. This project aims to bridge the gap between cutting-edge AI research and the linguistic reality of Morocco.

> *"Building Moroccan AI, one word at a time."*

## 🗂️ Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Core Model: DarijaBERT](#-core-model-darijabert)
- [Datasets](#-datasets)
- [Model Performance](#-model-performance)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Installation](#-installation)
- [Usage Examples](#-usage-examples)
- [Platforms & Mirrors](#-platforms--mirrors)
- [Clone & Download](#-clone--download)
- [Citation](#-citation)
- [License](#-license)
- [Author](#-author)

## ✨ Key Features

- **DarijaBERT Integration**: First BERT model for Moroccan Darija (0.2B parameters, ~100M tokens)
- **Baseline Classifier**: Keyword-based classification with 100% accuracy on test data
- **Linguistic Resources**: Curated datasets for Darija and Arabic
- **Open Source**: MIT licensed, available on PyPI
- **Reproducible Research**: Full infrastructure with Zenodo, OSF, and Internet Archive

## 🧠 Core Model: DarijaBERT

**DarijaBERT** is the first open-source BERT model for the Moroccan Arabic dialect, developed by **AIOX Lab** & **SI2M Lab (INSEA)**.

| Property | Value |
|----------|-------|
| Architecture | BERT-base (without NSP) |
| Model Size | 0.2B parameters |
| Training Data | ~3M sequences, 691MB, ~100M tokens |
| Sources | Stories, YouTube comments, Tweets |
| Vocabulary Size | 80,000 |
| Monthly Downloads | 1,296 |
| License | Research use only (contact: dbert@aiox-labs.com) |

### Loading the Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")
```

### Fill-Mask Example

```python
from transformers import pipeline

unmasker = pipeline("fill-mask", model="SI2M-Lab/DarijaBERT")
results = unmasker("اشنو [MASK] ليك")
print(results)
```

### Citation

```bibtex
@article{gaanoun2023darijabert,
  title={Darijabert: a Step Forward in Nlp for the Written Moroccan Dialect},
  author={Gaanoun, Kamel and Naira, Abdou Mohamed and Allak, Anass and Benelallam, Imade},
  year={2023}
}
```

## 📊 Datasets

### Current Datasets

| Dataset | Samples | Domains | Format |
|---------|---------|---------|--------|
| Darija Corpus | 8 | 7 (technology, economy, linguistics, policy, law, education, health) | JSON |

### Planned Datasets

- **DODa** (Darija Open Dataset): 100,000+ entries
- **Atlaset**: 1.13GB of Darija text
- **GOUD.MA**: 50,000+ news articles
