# Adaptive Transaction Fee Prediction for Bitcoin Mempool Optimization

This repository contains the implementation and experimental framework for the research project:

**Adaptive Transaction Fee Prediction for Bitcoin Mempool Optimization Using Multi-Feature Analysis and Retrieval-Augmented Generation (RAG)**

The project proposes a data-driven, explainable, and real-time approach to optimizing Bitcoin transaction prioritization under dynamic network congestion.

---

## 📌 Problem Statement

Bitcoin’s mempool stores unconfirmed transactions competing for limited block space.  
Traditional fee estimation techniques—primarily fee-per-byte heuristics and static statistical models—fail to capture:

- Non-linear fee dynamics  
- Transaction age fairness  
- Parent–child (CPFP) dependencies  
- Real-time network congestion patterns  

As a result, users often face fee overpayment, delayed confirmations, and inefficient block utilization.

---

## 🚀 Proposed Solution

This project introduces an **adaptive transaction fee prediction and prioritization framework** that integrates:

- **Multi-feature analysis**  
  - Fee rate  
  - Transaction age  
  - Ancestor dependencies (CPFP-aware)  

- **Non-linear transformations**  
  - Logarithmic scaling  
  - Feature normalization  

- **Sigmoid-based priority scoring**  
  - Stable ranking  
  - Interpretable prioritization  

- **Retrieval-Augmented Generation (RAG)**  
  - Context-aware explanations  
  - Transparent decision reasoning  

The system dynamically adapts to real-time mempool conditions while preserving fairness and miner incentives.

---

## 🧠 System Architecture

The framework consists of the following layers:

### 1. Data Collection
- Real-time Bitcoin mempool data ingestion via public APIs.

### 2. Feature Engineering
- Fee per byte with ancestor aggregation  
- Transaction age  
- Ancestor fee rate (CPFP awareness)

### 3. Scoring & Prediction
- Log-scaled features  
- Min–max normalization  
- Weighted linear scoring  
- Sigmoid-based priority mapping

### 4. RAG Explainability Layer
- Retrieves relevant transaction contexts  
- Generates human-readable explanations for prioritization decisions

### 5. Optimized Data Structures
- Hash Maps for O(1) transaction lookup  
- Priority Queues / Heaps for O(log n) ranking  
- Binary Search Trees for dynamic updates  

---

## 📊 Key Results

- **97% prediction accuracy** on live Bitcoin mempool data  
- **26% improvement** in inclusion of older transactions  
- **18% reduction** in fee volatility compared to heuristic models  
- **< 0.5 seconds** per update under real-time conditions  

These results demonstrate improved **fairness, efficiency, and transparency**.

---

## 🔍 Key Contributions

- Introduced **ancestor-aware, fairness-driven** transaction scoring  
- Integrated **RAG for explainable blockchain decision-making**  
- Designed a **scalable, real-time mempool optimization pipeline**  
- Bridged **machine learning, blockchain economics, and data structures**

---

## 📚 Research Reference

This repository accompanies the research paper:

**Adaptive Transaction Fee Prediction for Bitcoin Mempool Optimization Using Multi-Feature Analysis and Retrieval-Augmented Generation**

Department of Artificial Intelligence  
Vishwakarma University, Pune, India

---

## ⚖️ License

This project is released under the **MIT License**.  
You are free to use, modify, and distribute the code with attribution.

---

## 👤 Author

**Pravesh Jain**  
Artificial Intelligence & Data Science  
Vishwakarma University, Pune
