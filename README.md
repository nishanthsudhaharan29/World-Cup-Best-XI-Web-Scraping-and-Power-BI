# Cricket World Cup Best XI Selection and Dashboard

## Project Description

This project involves analyzing scorecards from the Cricket World Cup to identify and visualize the best eleven players (Best XI) of the tournament. The end-to-end process includes web data scraping, data processing, player selection based on predefined criteria, and dashboard creation using Power BI for effective visual storytelling.

The goal is to provide cricket enthusiasts, analysts, and decision-makers with a transparent and data-driven approach to selecting the top performers in the tournament.

---

## Project Walkthrough

### 1. Data Collection

- **Objective**: Scrape individual game scorecards from Cricket World Cup matches.
- **Tools**: Python libraries such as `BeautifulSoup`, `requests`.
- **Process**:
  - Extract player-specific data from web pages.
  - Validate and compile data to ensure completeness and consistency.

### 2. Data Processing and Cleaning

- **Objective**: Clean and preprocess the raw data for analysis.
- **Tools**: Python (`pandas`, `numpy`)
- **Process**:
  - Handle missing values and inconsistent formats.
  - Convert data to appropriate types.
  - Create a structured dataset with key player statistics.

### 3. Player Selection Criteria

- **Objective**: Apply predefined performance benchmarks to select the Best XI.
- **Reference**: Detailed in the accompanying "Player Selection Criteria" documentation.
- **Roles and Metrics**:
  - **Openers**: 
    - Average Runs > 30
    - Strike Rate > 140
    - Boundary % > 50%
  - **Middle Order**: 
    - Average Runs > 40
    - Strike Rate > 125
    - Avg. Balls Faced > 20
  - **Finishers**: 
    - Average Runs > 25
    - Strike Rate > 130
  - **All-Rounders**: 
    - Batting Average > 15
    - Bowling Economy < 7
  - **Specialist Bowlers**: 
    - Bowling Economy < 7
    - Strike Rate < 16

### 4. Data Analysis

- **Objective**: Calculate and compare player metrics against selection thresholds.
- **Tools**: Python (`pandas`, `numpy`)
- **Process**:
  - Compute batting and bowling performance indicators.
  - Evaluate all players and assign roles based on comparative analysis.
  - Shortlist top performers for each role.

### 5. Dashboard Creation

- **Objective**: Visualize insights and final player selection in Power BI.
- **Tools**: Power BI
- **Process**:
  - Import and structure the processed data.
  - Create visuals such as tables, bar charts, and line graphs.
  - Add interactive elements like slicers to filter by role and team.
  - Present the Best XI with contextual performance metrics.

---

## Power BI Dashboard Overview

### 1. Player Statistics Overview

- **Visual Elements**:
  - Table: Player name, team, batting style, total runs, strike rate, batting average, boundary percentage.
  - Charts: Trends in key batting metrics across matches or innings.

### 2. Role-Based Analysis

- **Openers/Quick Hitters**: Strike rate vs. average comparisons.
- **Middle Order/Anchors**: Focus on stability and scoring efficiency.
- **Finishers/Power Hitters**: Late-innings strike rates and contribution.
- **All-Rounders**: Combined batting and bowling statistics.
- **Specialist Bowlers**: Economy rates, strike rates, and dot ball percentages.

### 3. Final Team Selection

- **Interactive Feature**: Drill down into individual player stats by selection.
- **Summary View**: Display of the selected Best XI with performance justifications.

### 4. Team Performance Analysis

- **Overview**:
  - Aggregate statistics for the Best XI team.
  - Side-by-side comparisons of batting and bowling performances.

---

## Tools and Technologies

- **Languages**: Python
- **Libraries**: BeautifulSoup, requests, pandas, numpy
- **Visualization**: Power BI
- **Development Environment**: Jupyter Notebook

---

## Future Enhancements

- Automate data scraping for real-time updates during ongoing tournaments.
- Incorporate advanced metrics (e.g., win shares, pressure situations).
- Add machine learning models for predictive team composition.
- Build a web dashboard using Streamlit for broader accessibility.

---

## Repository Structure

