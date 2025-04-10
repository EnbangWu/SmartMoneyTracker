# SmartMoneyTracker

## Overview
This repository aims to identify "smart money" in cryptocurrency trading by analyzing wallet addresses that are the top gainers across multiple tokens. It specifically looks for addresses that appear in the top 100 gainers of different tokens, indicating potential smart money activity. The tokens currently analyzed include:

- EGGFLATION
- HOUSE
- PT
- REMUS
- RFC

## Usage
1. Place your CSV files containing wallet and profit data into the `data/` directory.
2. Run the analysis script:
   ```bash
   python analyze_addresses.py