# Dr. Itauma Itauma — Academic Website

[![Website](https://img.shields.io/badge/Website-amightyo.github.io-blue)](https://amightyo.github.io/)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0000--8835--5292-green)](https://orcid.org/0009-0000-8835-5292)
[![Google Scholar](https://img.shields.io/badge/Google-Scholar-blue)](https://scholar.google.com/citations?user=v0-zAJkAAAAJ&hl=en)
[![GitHub](https://img.shields.io/badge/GitHub-amightyo-black)](https://github.com/amightyo)

This repository contains the source code for the academic website of **Dr. Itauma Itauma**, Associate Professor of Data Science and Analytics at Harrisburg University of Science and Technology.

🌐 **Live website:** https://amightyo.github.io/

---

## About

I am a data scientist, professor, researcher, and academic leader whose work connects **artificial intelligence, data science, education and learning analytics, health and wellness analytics, and advanced quantitative methods**.

My research emphasizes the use of rigorous analytical methods to address meaningful human, educational, organizational, and health-related problems.

The website serves as a living academic portfolio documenting my:

- Research
- Publications
- Research projects
- Teaching
- Doctoral mentorship
- Scholarly presentations and service
- Curriculum vitae
- INSIGHT Lab initiative

---

## Research Areas

My research program is organized around four interconnected streams:

### 1. AI, Data Science & Education

Research examining artificial intelligence, predictive AI, generative AI, human–AI collaboration, AI literacy, and learning analytics.

### 2. Health & Wellness Analytics

Research applying data science and advanced statistical methods to sleep, physical activity, metabolic health, psychological wellness, and health informatics.

### 3. Advanced Quantitative Methods

Application and development of rigorous analytical approaches including:

- Structural Equation Modeling
- Bayesian Statistics
- Machine Learning
- Predictive Modeling
- Meta-Analysis
- Multilevel Modeling

### 4. Science of Research & Emerging AI

Research focused on:

- Bibliometrics
- Open Science
- Reproducible Research
- Retrieval-Augmented Generation (RAG)
- Agentic AI
- Emerging research methodologies

---

## INSIGHT Lab

The website also serves as the developing home of the **INSIGHT Lab**:

**Interdisciplinary Network for Science, Intelligence, Growth, Health & Technology**

> *Turning data into insight. Turning insight into impact.*

The INSIGHT Lab is an emerging interdisciplinary research initiative focused on connecting artificial intelligence, data science, education, health analytics, advanced quantitative methods, and reproducible research.

The lab is intended to support interdisciplinary collaboration, doctoral research development, student mentorship, and the translation of rigorous analytical research into meaningful impact.

---

## Website Technology

This website is built using:

- [Quarto](https://quarto.org/)
- Git
- GitHub
- GitHub Actions
- GitHub Pages
- Python

The site was migrated from an earlier Jekyll-based website to provide a more modern, reproducible, and maintainable academic web presence.

---

## Automated Deployment

The website uses **GitHub Actions** for continuous deployment.

The workflow is:

```text
Local changes
      ↓
Quarto preview
      ↓
Commit to master
      ↓
Push to GitHub
      ↓
GitHub Actions
      ↓
Quarto render
      ↓
GitHub Pages artifact
      ↓
Automatic deployment
      ↓
amightyo.github.io
```
Changes pushed to the master branch automatically trigger a fresh Quarto build and deployment to GitHub Pages.

---

## ORCID Publication Synchronization

Publication metadata is synchronized with my public ORCID record using a custom Python workflow.

```text
ORCID
   ↓
Python synchronization script
   ↓
Structured publication data
   ↓
Generated Quarto content
   ↓
GitHub
   ↓
Automatic website deployment
```
The synchronization workflow periodically checks my ORCID record and updates publication information when changes are detected.

ORCID:

https://orcid.org/0009-0000-8835-5292

The relevant components include:
```text
scripts/
└── update_publications.py

data/
└── orcid_publications.json

generated/
└── orcid-publications.qmd

.github/
└── workflows/
    ├── publish.yml
    └── update-publications.yml
```
ORCID API credentials are managed securely through GitHub Actions repository secrets and are not stored in the repository.

---

## Repository Structure

The repository includes the major website sections and supporting infrastructure:

```text
amightyo.github.io/
│
├── .github/
│   └── workflows/
│       ├── publish.yml
│       └── update-publications.yml
│
├── data/
│   └── orcid_publications.json
│
├── generated/
│   └── orcid-publications.qmd
│
├── images/
│
├── includes/
│   ├── person-schema.html
│   └── google-verification.html
│
├── scripts/
│   └── update_publications.py
│
├── index.qmd
├── about.qmd
├── research.qmd
├── lab.qmd
├── teaching.qmd
├── publications.qmd
├── projects.qmd
├── mentorship.qmd
├── cv.qmd
├── _quarto.yml
├── styles.css
└── README.md
```

Additional project pages may be added as the research portfolio develops.

---

## Local Development

To work with the website locally, clone the repository:
```text
git clone https://github.com/amightyo/amightyo.github.io.git
cd amightyo.github.io
```
Open the repository in VS Code:

```text
code .
```
Preview the site:
```text
quarto preview
```
Render the complete website:
```text
quarto render
```

---

## Publishing Updates

After reviewing changes locally:
```text
git status
git add -A
git commit -m "Describe the website update"
git push origin master
```
No manual GitHub Pages publishing step is required.

A push to **master** automatically triggers the GitHub Actions deployment workflow.

---

## Reproducible Research Philosophy

The technical architecture of this website reflects the same principles emphasized in my research and mentorship:

Transparency · Reproducibility · Open Science · Responsible Analytics

Where appropriate, research projects are supported through tools and platforms such as:

- Git and GitHub  
- Quarto  
- Python  
- R  
- OSF  
- ORCID  
- Reproducible analytical workflows  

---

## Scholarly Profiles

* **Website:** https://amightyo.github.io/
* **Google Scholar:** https://scholar.google.com/citations?user=v0-zAJkAAAAJ&hl=en
* **ORCID:** https://orcid.org/0009-0000-8835-5292
* **LinkedIn:** https://www.linkedin.com/in/amightyo/
* **GitHub:** https://github.com/amightyo
* **ResearchGate:** https://www.researchgate.net/profile/Itauma-Itauma
* **Harrisburg University:** https://www.harrisburgu.edu/

---

## Current Development

The website will continue to evolve alongside my research, teaching, doctoral mentorship, scholarly collaborations, and the development of the INSIGHT Lab.

Future additions may include:

* INSIGHT Lab members and collaborators
* Student research projects
* Additional research project pages
* Research datasets and code
* Open science resources
* Teaching resources
* Presentations and workshops
* Research software and reproducible workflows

---

## License and Use

Website content, research materials, code, and other resources may have different reuse conditions depending on the specific project or publication.

Please consult individual repositories, publications, or project documentation for applicable licensing and citation information.

---

© 2026 Itauma Itauma





