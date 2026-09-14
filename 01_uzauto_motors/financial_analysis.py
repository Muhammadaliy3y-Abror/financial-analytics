# ==============================================================================
# UzAuto Motors JSC (FY 2022–2025) Financial Analysis & Visualization Script
# Project: 01_uzauto_motors
# Purpose: Calculates corporate financial metrics and generates 300-DPI publication-ready charts.
# ==============================================================================

import matplotlib.pyplot as plt
import numpy as np
import os

# Create the 'charts' directory if it doesn't exist
os.makedirs('charts', exist_ok=True)

# ------------------------------------------------------------------------------
# 1. DATASET SETUP & FINANCIAL METRICS
# ------------------------------------------------------------------------------
years = ['FY 2022', 'FY 2023', 'FY 2024', 'FY 2025']

# Core Statement Variables ($ Millions)
revenue = [3260.0, 4450.0, 4200.0, 4100.0]
net_income = [235.1, 333.6, 314.9, 339.6]
total_assets = [2100.0, 2350.0, 2500.0, 2600.0]
total_equity = [650.0, 780.0, 908.8, 1300.0]

# Financial Ratios (%)
gross_margin = [14.72, 12.55, 13.85, 11.21]
operating_margin = [9.51, 8.20, 9.13, 7.13]
net_margin = [7.21, 7.50, 7.50, 8.28]

# Visual Styling Setup
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

# ------------------------------------------------------------------------------
# 2. CHART 1: Net Revenue vs. Net Income (Dual-Axis Combo Chart)
# ------------------------------------------------------------------------------
fig, ax1 = plt.subplots(figsize=(9, 5.5))

color_rev = '#4c9be8'
ax1.set_title('UzAuto Motors: Revenue vs. Net Income (2022–2025)', fontsize=14, fontweight='bold', pad=15)
ax1.set_ylabel('Net Revenue ($ Millions)', color='#1f77b4', fontsize=11, fontweight='bold')
bars = ax1.bar(years, revenue, color=color_rev, alpha=0.75, width=0.4, label='Net Revenue')
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.set_ylim(0, 5000)

# Secondary Axis for Net Income
ax2 = ax1.twinx()
color_ni = '#2ca02c'
ax2.set_ylabel('Net Income ($ Millions)', color=color_ni, fontsize=11, fontweight='bold')
line = ax2.plot(years, net_income, color=color_ni, marker='o', linewidth=3, markersize=9, label='Net Income')
ax2.tick_params(axis='y', labelcolor=color_ni)
ax2.set_ylim(200, 360)

# Data Annotations
for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval - 250, f'${yval:,.1f}M', ha='center', va='bottom', color='white', fontweight='bold')

for i, txt in enumerate(net_income):
    ax2.annotate(f'${txt:.1f}M', (years[i], net_income[i]), textcoords="offset points", xytext=(0,10), ha='center', fontweight='bold', color='#2ca02c')

plt.tight_layout()
plt.savefig('charts/chart1_revenue_vs_net_income.png', dpi=300)
plt.close()

# ------------------------------------------------------------------------------
# 3. CHART 2: Profitability Margin Trends (Line Chart)
# ------------------------------------------------------------------------------
plt.figure(figsize=(9, 5.5))
plt.plot(years, gross_margin, marker='o', linewidth=2.5, label='Gross Margin %', color='#d62728')
plt.plot(years, operating_margin, marker='s', linewidth=2.5, label='Operating Margin %', color='#ff7f0e')
plt.plot(years, net_margin, marker='^', linewidth=2.5, label='Net Profit Margin %', color='#2ca02c')

plt.title('UzAuto Motors: Profitability Margin Trends (2022–2025)', fontsize=14, fontweight='bold', pad=15)
plt.ylabel('Margin (%)', fontsize=11, fontweight='bold')
plt.ylim(6, 16)
plt.legend(loc='center right', frameon=True)

# Data Annotations
for i in range(len(years)):
    plt.text(years[i], gross_margin[i] + 0.35, f'{gross_margin[i]:.2f}%', ha='center', fontweight='bold', color='#d62728')
    plt.text(years[i], operating_margin[i] + 0.35, f'{operating_margin[i]:.2f}%', ha='center', fontweight='bold', color='#ff7f0e')
    plt.text(years[i], net_margin[i] - 0.55, f'{net_margin[i]:.2f}%', ha='center', fontweight='bold', color='#2ca02c')

plt.tight_layout()
plt.savefig('charts/chart2_margin_trends.png', dpi=300)
plt.close()

# ------------------------------------------------------------------------------
# 4. CHART 3: Capital Structure Expansion (Grouped Bar Chart)
# ------------------------------------------------------------------------------
x = np.arange(len(years))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5.5))
rects1 = ax.bar(x - width/2, total_assets, width, label='Total Assets', color='#1f77b4')
rects2 = ax.bar(x + width/2, total_equity, width, label='Total Equity', color='#9467bd')

ax.set_title('UzAuto Motors: Capital Structure Expansion (2022–2025)', fontsize=14, fontweight='bold', pad=15)
ax.set_ylabel('Amount ($ Millions)', fontsize=11, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_ylim(0, 3000)
ax.legend(loc='upper left', frameon=True)

# Data Annotations
for rect in rects1:
    height = rect.get_height()
    ax.annotate(f'${height:,.0f}M', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')

for rect in rects2:
    height = rect.get_height()
    ax.annotate(f'${height:,.0f}M', xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 4), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('charts/chart3_capital_structure.png', dpi=300)
plt.close()

print("Execution complete: All 3 charts rendered and saved to /charts directory.")
