import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create figures directory if it doesn't exist
os.makedirs('../figures', exist_ok=True)

# Set academic plotting style
sns.set_theme(style="whitegrid")
plt.rcParams.update({'font.size': 12, 'axes.labelsize': 14, 'axes.titlesize': 16})

def plot_domain_rates():
    categories = ['Scientific', 'Historical', 'Mathematical', 'Health', 'Cultural']
    tamil_sr = [20.0, 40.0, 0.0, 20.0, 60.0]
    hindi_sr = [0.0, 20.0, 0.0, 0.0, 40.0]

    x = np.arange(len(categories))
    width = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(x - width/2, tamil_sr, width, label='Tamil', color='#4C72B0')
    ax.bar(x + width/2, hindi_sr, width, label='Hindi', color='#DD8452')

    ax.set_ylabel('Sycophancy Rate (%)')
    ax.set_title('Sycophancy Rates by Domain: Tamil vs. Hindi')
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    plt.tight_layout()
    plt.savefig('../figures/fig1_domain_rates.png', dpi=300)
    print("Saved fig1_domain_rates.png")

def plot_spiraling():
    turns = [1, 2, 3, 4, 5]
    tamil_flips = [0, 0, 0, 7, 7] 
    hindi_flips = [0, 0, 0, 1, 3]

    plt.figure(figsize=(8, 5))
    plt.plot(turns, tamil_flips, marker='o', linestyle='-', linewidth=2, label='Tamil', color='#4C72B0')
    plt.plot(turns, hindi_flips, marker='s', linestyle='--', linewidth=2, label='Hindi', color='#DD8452')

    plt.xlabel('Conversation Turn')
    plt.ylabel('Cumulative Number of Flipped Scenarios')
    plt.title('Delusional Spiraling: Flips Across Escalation Turns')
    plt.xticks(turns)
    plt.yticks(np.arange(0, 10, 2))
    plt.legend()
    plt.tight_layout()
    plt.savefig('../figures/fig2_delusional_spiraling.png', dpi=300)
    print("Saved fig2_delusional_spiraling.png")

def plot_heatmap():
    score_matrix = np.array([
        [95, 20, 3, 7, 0],  # Tamil
        [105, 17, 0, 3, 0]  # Hindi
    ])

    plt.figure(figsize=(8, 4))
    sns.heatmap(score_matrix, annot=True, fmt="d", cmap="YlGnBu", 
                xticklabels=['0 (Firm)', '1 (Hesitant)', '2 (Neutral)', '3 (Partial)', '4 (Full)'],
                yticklabels=['Tamil', 'Hindi'])
    plt.xlabel('Sycophancy Score')
    plt.ylabel('Language')
    plt.title('Global Response Score Distribution')
    plt.tight_layout()
    plt.savefig('../figures/fig3_score_heatmap.png', dpi=300)
    print("Saved fig3_score_heatmap.png")

if __name__ == "__main__":
    print("Generating SYCON-Indic Visualizations...")
    plot_domain_rates()
    plot_spiraling()
    plot_heatmap()
    print("Done!")