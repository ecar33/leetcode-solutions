# Longest Substring Without Repeating Characters

This repository contains Python scripts to find the longest substring without repeating characters using two different approaches:
1. An optimized approach using the sliding window technique.
2. A naive approach with a complexity of O(n<sup>3</sup>).

## Files
- `optimized_solution.py`: Implements the sliding window approach for finding the longest substring without repeating characters.
- `naive_solution.py`: Implements the naive brute-force approach for finding the longest substring without repeating characters.

## Requirements
- Python 3.x

## Setup and Installation

Before running the scripts, ensure that your Python environment is set up correctly. This repository requires Python 3.x and some additional modules that are listed in the `requirements.txt` file.

### Installing Python Modules

To install the required Python modules, run the following command in your terminal:

```bash
pip install -r requirements.txt
```

## How to Run the Scripts


### Running the Optimized Solution
To run the optimized solution using the sliding window technique, execute the following command in your terminal:
```bash
python optimized_solution.py "<input_string>"
```
### Running the Naive Solution
To run the naive solution, use the following command:
```bash
python naive_solution.py "<input_string>"
```

### Example usage:
You can test the scripts using any string. For example:

```bash
python optimized_solution.py "abcabcbb"
```

```bash
python naive_solution.py "abcabcbb"
```