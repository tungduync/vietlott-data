# 🎰 Vietlott Data Collection & Analysis

> 📊 **Automated data collection and analysis for Vietnam's official lottery games**

This project automatically collects and analyzes data from [Vietlott](https://vietlott.vn) - Vietnam's official lottery operator. It provides comprehensive statistics, frequency analysis, and experimental prediction models for educational purposes.

## 🎯 Supported Lottery Products

| Product | Official Results | Description |
|---------|------|-------------|
| **Power 6/55** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/655) | Choose 6 numbers from 1-55 |
| **Power 6/45** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/645) | Choose 6 numbers from 1-45 |
| **Keno** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/winning-number-keno) | Fast-pace number game |
| **Max 3D** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3d) | 3-digit lottery game |
| **Max 3D Pro** | [🔗 Results](https://vietlott.vn/vi/trung-thuong/ket-qua-trung-thuong/max-3dpro) | Enhanced 3D lottery |


## 📋 Table of Contents

- [🎯 Supported Lottery Products](#-supported-lottery-products)
- [📊 Data Statistics](#-data-statistics)
- [🔮 Prediction Models](#-prediction-models)
- [📈 Power 6/55 Analysis](#-power-655-analysis)
  - [📅 Recent Results](#-recent-results)
  - [🎲 Number Frequency (All Time)](#-number-frequency-all-time)
  - [📊 Frequency Analysis by Period](#-frequency-analysis-by-period)
- [⚙️ How It Works](#️-how-it-works)
- [🚀 Installation & Usage](#-installation--usage)
- [📄 License](#-license)


## 📊 Data Statistics

| Product   |   Total Draws | Start Date   | End Date   |   Total Records | First ID   | Latest ID   |
|:----------|--------------:|:-------------|:-----------|----------------:|:-----------|:------------|
| Power 655 |          1200 | 2017-08-01   | 2025-06-07 |            1200 | 00001      | 01200       |
| Power 645 |          1167 | 2017-10-25   | 2025-06-08 |            1167 | 00198      | 01364       |
| Keno      |           908 | 2022-12-04   | 2025-06-02 |          129077 | #0110271   | #0239906    |
| 3D        |           933 | 2019-04-22   | 2025-06-09 |             933 | 00001      | 00935       |
| 3D Pro    |           578 | 2021-09-14   | 2025-06-05 |             578 | 00001      | 00580       |

## 🔮 Prediction Models

> ⚠️ **Disclaimer**: These are experimental models for educational purposes only. Lottery outcomes are random and cannot be predicted reliably.

### 🎲 Random Strategy Backtest

- **Strategy**: Random number selection
- **Tickets per day**: 20
- **Daily cost**: 200,000 VND
- **Results with 5+ matches**:

No significant matches found in backtest period.



## 📈 Power 6/55 Analysis

### 📅 Recent Results (Last 10 draws)
| date       |    id | result                       |   page | process_time               |
|:-----------|------:|:-----------------------------|-------:|:---------------------------|
| 2025-06-07 | 01200 | [12, 17, 21, 46, 48, 52, 45] |      0 | 2025-06-08T19:00:23.946470 |
| 2025-06-05 | 01199 | [14, 21, 33, 37, 46, 49, 34] |      0 | 2025-06-05 19:00:16.186371 |
| 2025-06-03 | 01198 | [2, 11, 14, 16, 27, 38, 51]  |      0 | 2025-06-03 19:01:13.225100 |
| 2025-05-31 | 01197 | [6, 24, 41, 45, 49, 55, 8]   |      0 | 2025-05-31 19:00:15.708033 |
| 2025-05-29 | 01196 | [9, 37, 42, 45, 46, 50, 14]  |      0 | 2025-05-29 19:00:15.005246 |
| 2025-05-27 | 01195 | [4, 12, 18, 19, 44, 48, 42]  |      0 | 2025-05-27 19:00:27.363743 |
| 2025-05-24 | 01194 | [19, 20, 27, 30, 45, 55, 15] |      0 | 2025-05-26 19:00:21.730573 |
| 2025-05-22 | 01193 | [3, 9, 14, 41, 47, 55, 22]   |      0 | 2025-05-22 19:01:11.003151 |
| 2025-05-20 | 01192 | [19, 27, 44, 45, 47, 52, 15] |      0 | 2025-05-20 19:00:19.102116 |
| 2025-05-17 | 01191 | [2, 7, 26, 29, 41, 50, 43]   |      0 | 2025-05-19 09:08:44.622335 |

### 🎲 Number Frequency (All Time)
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |     166 | 1.98 |     |       21 |     150 | 1.79 |     | 41       | 181     | 2.16 |
|        2 |     140 | 1.67 |     |       22 |     171 | 2.04 |     | 42       | 157     | 1.87 |
|        3 |     163 | 1.94 |     |       23 |     167 | 1.99 |     | 43       | 170     | 2.02 |
|        4 |     131 | 1.56 |     |       24 |     153 | 1.82 |     | 44       | 157     | 1.87 |
|        5 |     151 | 1.8  |     |       25 |     139 | 1.65 |     | 45       | 150     | 1.79 |
|        6 |     128 | 1.52 |     |       26 |     141 | 1.68 |     | 46       | 159     | 1.89 |
|        7 |     133 | 1.58 |     |       27 |     140 | 1.67 |     | 47       | 156     | 1.86 |
|        8 |     160 | 1.9  |     |       28 |     135 | 1.61 |     | 48       | 162     | 1.93 |
|        9 |     166 | 1.98 |     |       29 |     161 | 1.92 |     | 49       | 158     | 1.88 |
|       10 |     142 | 1.69 |     |       30 |     133 | 1.58 |     | 50       | 155     | 1.85 |
|       11 |     159 | 1.89 |     |       31 |     157 | 1.87 |     | 51       | 175     | 2.08 |
|       12 |     161 | 1.92 |     |       32 |     157 | 1.87 |     | 52       | 158     | 1.88 |
|       13 |     146 | 1.74 |     |       33 |     152 | 1.81 |     | 53       | 160     | 1.9  |
|       14 |     153 | 1.82 |     |       34 |     168 | 2    |     | 54       | 145     | 1.73 |
|       15 |     144 | 1.71 |     |       35 |     151 | 1.8  |     | 55       | 152     | 1.81 |
|       16 |     141 | 1.68 |     |       36 |     142 | 1.69 |     |          |         |      |
|       17 |     140 | 1.67 |     |       37 |     140 | 1.67 |     |          |         |      |
|       18 |     154 | 1.83 |     |       38 |     144 | 1.71 |     |          |         |      |
|       19 |     152 | 1.81 |     |       39 |     146 | 1.74 |     |          |         |      |
|       20 |     162 | 1.93 |     |       40 |     165 | 1.96 |     |          |         |      |

### 📊 Frequency Analysis by Period

#### Last 30 Days
|   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        2 |       1 | 1.59 |     | 33       | 1       | 1.59 |
|        3 |       1 | 1.59 |     | 34       | 1       | 1.59 |
|        4 |       1 | 1.59 |     | 37       | 2       | 3.17 |
|        6 |       1 | 1.59 |     | 38       | 1       | 1.59 |
|        8 |       1 | 1.59 |     | 41       | 2       | 3.17 |
|        9 |       2 | 3.17 |     | 42       | 2       | 3.17 |
|       11 |       1 | 1.59 |     | 44       | 2       | 3.17 |
|       12 |       2 | 3.17 |     | 45       | 5       | 7.94 |
|       14 |       4 | 6.35 |     | 46       | 3       | 4.76 |
|       15 |       2 | 3.17 |     | 47       | 2       | 3.17 |
|       16 |       1 | 1.59 |     | 48       | 2       | 3.17 |
|       17 |       1 | 1.59 |     | 49       | 2       | 3.17 |
|       18 |       1 | 1.59 |     | 50       | 1       | 1.59 |
|       19 |       3 | 4.76 |     | 51       | 1       | 1.59 |
|       20 |       1 | 1.59 |     | 52       | 2       | 3.17 |
|       21 |       2 | 3.17 |     | 55       | 3       | 4.76 |
|       22 |       1 | 1.59 |     |          |         |      |
|       24 |       1 | 1.59 |     |          |         |      |
|       27 |       3 | 4.76 |     |          |         |      |
|       30 |       1 | 1.59 |     |          |         |      |

#### Last 60 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       1 | 0.65 |     |       21 |       5 | 3.25 |     | 43       | 3       | 1.95 |
|        2 |       3 | 1.95 |     |       22 |       1 | 0.65 |     | 44       | 3       | 1.95 |
|        3 |       4 | 2.6  |     |       23 |       1 | 0.65 |     | 45       | 6       | 3.9  |
|        4 |       1 | 0.65 |     |       24 |       3 | 1.95 |     | 46       | 3       | 1.95 |
|        5 |       2 | 1.3  |     |       25 |       2 | 1.3  |     | 47       | 5       | 3.25 |
|        6 |       2 | 1.3  |     |       26 |       2 | 1.3  |     | 48       | 4       | 2.6  |
|        7 |       3 | 1.95 |     |       27 |       3 | 1.95 |     | 49       | 4       | 2.6  |
|        8 |       2 | 1.3  |     |       28 |       3 | 1.95 |     | 50       | 4       | 2.6  |
|        9 |       3 | 1.95 |     |       29 |       3 | 1.95 |     | 51       | 2       | 1.3  |
|       10 |       1 | 0.65 |     |       30 |       2 | 1.3  |     | 52       | 3       | 1.95 |
|       11 |       2 | 1.3  |     |       31 |       1 | 0.65 |     | 54       | 2       | 1.3  |
|       12 |       3 | 1.95 |     |       32 |       2 | 1.3  |     | 55       | 4       | 2.6  |
|       13 |       1 | 0.65 |     |       33 |       2 | 1.3  |     |          |         |      |
|       14 |       6 | 3.9  |     |       34 |       2 | 1.3  |     |          |         |      |
|       15 |       8 | 5.19 |     |       37 |       4 | 2.6  |     |          |         |      |
|       16 |       4 | 2.6  |     |       38 |       2 | 1.3  |     |          |         |      |
|       17 |       2 | 1.3  |     |       39 |       4 | 2.6  |     |          |         |      |
|       18 |       2 | 1.3  |     |       40 |       2 | 1.3  |     |          |         |      |
|       19 |       6 | 3.9  |     |       41 |       5 | 3.25 |     |          |         |      |
|       20 |       1 | 0.65 |     |       42 |       5 | 3.25 |     |          |         |      |

#### Last 90 Days
|   result |   count |    % | -   |   result |   count |    % | -   | result   | count   | %    |
|---------:|--------:|-----:|:----|---------:|--------:|-----:|:----|:---------|:--------|:-----|
|        1 |       2 | 0.82 |     |       21 |       6 | 2.45 |     | 41       | 11      | 4.49 |
|        2 |       4 | 1.63 |     |       22 |       1 | 0.41 |     | 42       | 10      | 4.08 |
|        3 |       6 | 2.45 |     |       23 |       6 | 2.45 |     | 43       | 5       | 2.04 |
|        4 |       2 | 0.82 |     |       24 |       7 | 2.86 |     | 44       | 4       | 1.63 |
|        5 |       2 | 0.82 |     |       25 |       3 | 1.22 |     | 45       | 6       | 2.45 |
|        6 |       2 | 0.82 |     |       26 |       4 | 1.63 |     | 46       | 3       | 1.22 |
|        7 |       4 | 1.63 |     |       27 |       4 | 1.63 |     | 47       | 6       | 2.45 |
|        8 |       3 | 1.22 |     |       28 |       4 | 1.63 |     | 48       | 5       | 2.04 |
|        9 |       4 | 1.63 |     |       29 |       7 | 2.86 |     | 49       | 5       | 2.04 |
|       10 |       2 | 0.82 |     |       30 |       4 | 1.63 |     | 50       | 6       | 2.45 |
|       11 |       3 | 1.22 |     |       31 |       2 | 0.82 |     | 51       | 3       | 1.22 |
|       12 |       3 | 1.22 |     |       32 |       4 | 1.63 |     | 52       | 5       | 2.04 |
|       13 |       5 | 2.04 |     |       33 |       3 | 1.22 |     | 53       | 2       | 0.82 |
|       14 |      11 | 4.49 |     |       34 |       4 | 1.63 |     | 54       | 3       | 1.22 |
|       15 |       9 | 3.67 |     |       35 |       1 | 0.41 |     | 55       | 5       | 2.04 |
|       16 |       4 | 1.63 |     |       36 |       3 | 1.22 |     |          |         |      |
|       17 |       4 | 1.63 |     |       37 |       7 | 2.86 |     |          |         |      |
|       18 |       2 | 0.82 |     |       38 |       3 | 1.22 |     |          |         |      |
|       19 |       8 | 3.27 |     |       39 |       6 | 2.45 |     |          |         |      |
|       20 |       3 | 1.22 |     |       40 |       4 | 1.63 |     |          |         |      |



## ⚙️ How It Works

### 🤖 Automated Data Collection

This project runs completely automatically using **GitHub Actions** - no server required!

- **⏰ Schedule**: Runs daily via [GitHub Actions workflow](.github/workflows/crawl.yaml)
- **🔄 Process**: Fetches latest results → Processes data → Commits to repository
- **📊 Analysis**: Generates statistics and updates README automatically

### 🕵️ Data Crawling Method

The data collection works by:
1. **🔍 Network Analysis**: Inspecting browser-server communication
2. **🐍 Python Replication**: Recreating the data fetch logic in Python
3. **📋 Structured Storage**: Saving results in JSONL format for easy analysis
4. **🔄 Continuous Updates**: Daily automated runs ensure fresh data

> **Note**: This is purely for educational and research purposes. No gambling advice is provided.


## 🚀 Installation & Usage

### 📦 Install via pip

```bash
pip install -i https://test.pypi.org/simple/ vietlott-data==0.1.3
```

### 💻 Command Line Interface

#### 🔍 Crawl Data

```bash
vietlott-crawl [OPTIONS] PRODUCT

# Options:
#   --run-date TEXT       Specific date to crawl
#   --index_from INTEGER  Starting page index
#   --index_to INTEGER    Ending page index
#   --help               Show help message
```

#### 🔧 Backfill Missing Data

```bash
vietlott-missing [OPTIONS] PRODUCT

# Options:
#   --limit INTEGER  Number of pages to process
#   --help          Show help message
```

### 🛠️ Development Setup

```bash
# Clone the repository
git clone https://github.com/vietvudanh/vietlott-data.git
cd vietlott-data

# Install dependencies
pip install -r requirements-dev.txt

# Run tests
pytest
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <strong>⭐ If you find this project useful, please consider giving it a star!</strong>
</div>

