<div align="center">

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

</div>

---

## 📌 Overview

**moroccan_nlp** is a comprehensive project dedicated to developing linguistic resources and Natural Language Processing (NLP) models for **Moroccan Darija** and **Arabic**. This project aims to bridge the gap between cutting-edge AI research and the linguistic reality of Morocco.

> *"Building Moroccan AI, one word at a time."*

---

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

---

## ✨ Key Features

- **DarijaBERT Integration**: First BERT model for Moroccan Darija (0.2B parameters, ~100M tokens)
- **Baseline Classifier**: Keyword-based classification with 100% accuracy on test data
- **Linguistic Resources**: Curated datasets for Darija and Arabic
- **Open Source**: MIT licensed, available on PyPI
- **Reproducible Research**: Full infrastructure with Zenodo, OSF, and Internet Archive

---

## 🧠 Core Model: DarijaBERT

**DarijaBERT** is the first open-source BERT model for the Moroccan Arabic dialect, developed by **AIOX Lab** & **SI2M Lab (INSEA)**.

| Property | Value |
|----------|-------|
| **Architecture** | BERT-base (without NSP) |
| **Model Size** | 0.2B parameters |
| **Training Data** | ~3M sequences, 691MB, ~100M tokens |
| **Sources** | Stories, YouTube comments, Tweets |
| **Vocabulary Size** | 80,000 |
| **Monthly Downloads** | 1,296 |
| **License** | Research use only (contact: dbert@aiox-labs.com) |

### Loading the Model

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")
```

Fill-Mask Example

```python
from transformers import pipeline

unmasker = pipeline('fill-mask', model='SI2M-Lab/DarijaBERT')
results = unmasker("اشنو [MASK] ليك")
print(results)
```

Citation

```bibtex
@article{gaanoun2023darijabert,
  title={Darijabert: a Step Forward in Nlp for the Written Moroccan Dialect},
  author={Gaanoun, Kamel and Naira, Abdou Mohamed and Allak, Anass and Benelallam, Imade},
  year={2023}
}
```

---

📊 Datasets

Current Datasets

Dataset Samples Domains Format
Darija Corpus 8 7 (technology, economy, linguistics, policy, law, education, health) JSON

Planned Datasets

· DODa (Darija Open Dataset): 100,000+ entries
· Atlaset: 1.13GB of Darija text
· GOUD.MA: 50,000+ news articles

---

📈 Model Performance

Baseline Classifier (v6)

Metric Value
Accuracy 100% (8/8 samples)
Domains 7
Method Keyword-based classification

DarijaBERT Test Results

Tested on Fill-Mask task using Google Colab:

Sentence Top Predictions (Score)
"المغاربة سبوعة و [MASK]" 1. رجالة (0.3140), 2. جوالة (0.1802), 3. نمورة (0.0361)
"الدارجة هي لهجة [MASK]" 1. عربية (0.4521), 2. أمازيغية (0.1345), 3. ريفية (0.0234)
"المغرب بلد [MASK]" 1. إفريقي (0.5200), 2. أوروبي (0.1800), 3. أمريكي (0.0500)

---

📁 Project Structure

```
moroccan_nlp/
│
├── DATA/                     # Raw and processed datasets
│   ├── raw/                  # Original data
│   └── processed/            # Cleaned data
│
├── MODELS/                   # NLP models
│   └── DarijaBERT/           # DarijaBERT integration
│       ├── load_model.py     # Model loading script
│       └── results.txt       # Test results
│
├── scripts/                  # Utility scripts
│   ├── train_baseline_v6.py  # Baseline classifier
│   ├── preprocess_light.py   # Data preprocessing
│   └── load_data.py          # Data loading
│
├── ANALYSIS/                 # Data analysis notebooks
├── PUBLICATION/              # Research papers
├── REPORTS/                  # Progress reports
├── VALIDATION/               # Model validation
├── docs/                     # Technical documentation
├── README.md                 # This file
└── requirements.txt          # Python dependencies
```

---

🚀 Quick Start

Installation

```bash
# Install from PyPI
pip install moroccan-nlp

# Install from source
git clone https://github.com/gitdeeper13/moroccan_nlp.git
cd moroccan_nlp
pip install -e .
```

Minimal Example

```python
from transformers import AutoTokenizer, AutoModel

# Load DarijaBERT
tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")

print(f"Vocabulary size: {tokenizer.vocab_size}")
print(f"Model parameters: {model.num_parameters():,}")
```

Run Baseline Classifier

```bash
python scripts/train_baseline_v6.py
```

---

📦 Installation

```bash
# Install the package
pip install moroccan-nlp

# Clone the repository
git clone https://github.com/gitdeeper13/moroccan_nlp.git
cd moroccan_nlp

# Install dependencies
pip install -r requirements.txt
```

Requirements: Python 3.11+, PyTorch 2.4+, transformers, numpy, pandas

---

🧩 Usage Examples

Example 1: Load DarijaBERT

```python
from transformers import AutoTokenizer, AutoModel, pipeline

# Load model
tokenizer = AutoTokenizer.from_pretrained("SI2M-Lab/DarijaBERT")
model = AutoModel.from_pretrained("SI2M-Lab/DarijaBERT")

# Fill-Mask example
unmasker = pipeline('fill-mask', model='SI2M-Lab/DarijaBERT')
results = unmasker("اشنو [MASK] ليك")

for r in results:
    print(f"{r['sequence']} (score: {r['score']:.4f})")
```

Example 2: Load Dataset

```python
import json

with open('DATA/raw/darija_corpus.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    
samples = data['samples']
print(f"Loaded {len(samples)} samples")

# Display first sample
print(samples[0])
```

Example 3: Run Baseline Classifier

```bash
python scripts/train_baseline_v6.py
```

---

🌐 Platforms & Mirrors

Platform URL Role
🐙 GitHub (Primary) github.com/gitdeeper13/moroccan_nlp Source code, issues, PRs
🦊 GitLab (Mirror) gitlab.com/gitdeeper/moroccan-nlp CI/CD mirror
🪣 Bitbucket (Mirror) bitbucket.org/gitdeeper-13/moroccan_nlp Enterprise mirror
🏔️ Codeberg (Mirror) codeberg.org/gitdeeper13/moroccan_nlp Open-source community
📦 PyPI pypi.org/project/moroccan-nlp/ Python package distribution
🔬 Zenodo doi.org/10.5281/zenodo.21154423 Citable DOI, paper & data
📋 OSF Project osf.io/7szak Research project registry
📝 OSF Preregistration doi.org/10.17605/OSF.IO/SXGC6 Pre-registered study protocol
🌐 Website moroccan-nlp.netlify.app Live documentation & dashboard
🧑‍🔬 ORCID orcid.org/0009-0003-8903-0029 Researcher identity
🗄️ Internet Archive archive.org/details/osf-registrations-moroccan-nlp Permanent archival copy

🌐 Official Website Pages

Page URL
Homepage moroccan-nlp.netlify.app
Documentation moroccan-nlp.netlify.app/documentation
Dashboard moroccan-nlp.netlify.app/dashboard
Reports moroccan-nlp.netlify.app/reports

---

🔄 Clone & Download

Git Clone

```bash
# GitHub (Primary)
git clone https://github.com/gitdeeper13/moroccan_nlp.git

# GitLab (Mirror)
git clone https://gitlab.com/gitdeeper/moroccan-nlp.git

# Bitbucket (Mirror)
git clone https://bitbucket.org/gitdeeper-13/moroccan_nlp.git

# Codeberg (Mirror)
git clone https://codeberg.org/gitdeeper13/moroccan_nlp.git
```

Direct ZIP Download

Source Link
GitHub moroccan_nlp-main.zip
GitLab moroccan-nlp-main.zip
Bitbucket moroccan_nlp-main.zip
Codeberg moroccan_nlp-main.zip
PyPI files pypi.org/project/moroccan-nlp/#files
Zenodo record doi.org/10.5281/zenodo.21154423

---

📖 Citation

If moroccan_nlp contributes to your research, please cite using one of the following formats.

📦 PyPI Package

```bibtex
@software{baladi2026moroccan_nlp_pypi,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Linguistic Resources and Models for Moroccan Darija and Arabic},
  year         = {2026},
  version      = {1.0.0},
  publisher    = {Python Package Index},
  url          = {https://pypi.org/project/moroccan-nlp/},
  note         = {Python package, MIT License, Series GITDEEPER LAB ZERO V6}
}
```

🔬 Zenodo Archive (Paper & Data)

```bibtex
@dataset{baladi2026moroccan_nlp_zenodo,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Linguistic Resources and Models for Moroccan Darija and Arabic — Research Paper and Data},
  year         = {2026},
  publisher    = {Zenodo},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.21154423},
  url          = {https://doi.org/10.5281/zenodo.21154423},
  note         = {Natural Language Processing · GITDEEPER LAB ZERO V6}
}
```

📝 OSF Preregistration

```bibtex
@misc{baladi2026moroccan_nlp_osf,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Pre-registered Study Protocol for Linguistic Resources and Models for Moroccan Darija and Arabic},
  year         = {2026},
  publisher    = {Open Science Framework},
  doi          = {10.17605/OSF.IO/SXGC6},
  url          = {https://doi.org/10.17605/OSF.IO/SXGC6},
  note         = {OSF Preregistration}
}
```

📄 Research Paper

```bibtex
@article{baladi2026moroccan_nlp,
  author       = {Baladi, Samir},
  title        = {{moroccan_nlp}: Linguistic Resources and Models for Moroccan Darija and Arabic},
  year         = {2026},
  month        = {July},
  version      = {1.0.0},
  doi          = {10.5281/zenodo.21154423},
  url          = {https://doi.org/10.5281/zenodo.21154423},
  note         = {Ronin Institute / Rite of Renaissance, Series GITDEEPER LAB ZERO V6}
}
```

DarijaBERT Paper

```bibtex
@article{gaanoun2023darijabert,
  title={Darijabert: a Step Forward in Nlp for the Written Moroccan Dialect},
  author={Gaanoun, Kamel and Naira, Abdou Mohamed and Allak, Anass and Benelallam, Imade},
  year={2023}
}
```

APA (inline)

Baladi, S. (2026). moroccan_nlp: Linguistic Resources and Models for Moroccan Darija and Arabic (Version 1.0.0, Series GITDEEPER LAB ZERO V6). Zenodo. https://doi.org/10.5281/zenodo.21154423

---

📜 License

This project is licensed under the MIT License — see the LICENSE file for details.

```
MIT License

Copyright (c) 2026 Samir Baladi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
```

---

👤 Author

Samir Baladi
Independent Researcher — Natural Language Processing, Computational Linguistics & AI for Under-Resourced Languages
Ronin Institute / Rite of Renaissance

Contact Link
📧 Email gitdeeper@gmail.com
🧑‍🔬 ORCID 0009-0003-8903-0029
🐙 GitHub github.com/gitdeeper13
🔬 Zenodo doi.org/10.5281/zenodo.21154423

---

<div align="center">

GITDEEPER LAB ZERO V6 · Version 1.0.0 · July 2026

https://img.shields.io/badge/DOI-10.5281%2Fzenodo.21154423-blue.svg
https://img.shields.io/pypi/v/moroccan-nlp?color=1B4F72
https://img.shields.io/badge/License-MIT-yellow.svg
https://img.shields.io/badge/Domain-Natural%20Language%20Processing-1B4F72

"Building Moroccan AI, one word at a time."

</div>
