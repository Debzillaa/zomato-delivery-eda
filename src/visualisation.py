import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualizations(input_path, output_dir):

    # 1. Load the cleaned data
    print("Loading cleaned data...")
    df = pd.read_csv(input_path)
    
    # Ensure the figures directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Set a professional visual theme for all plots
    sns.set_theme(style="whitegrid", palette="muted")
    
    # ---------------------------------------------------------
    # Chart 1: Baseline Distribution of Delivery Times
    # ---------------------------------------------------------
    print("Generating Chart 1: Delivery Time Distribution...")
    plt.figure(figsize=(10, 6))
    sns.histplot(df['Time_taken (min)'], kde=True, bins=30, color='royalblue')
    plt.title('Distribution of Delivery Times', fontsize=16, pad=15)
    plt.xlabel('Time Taken (Minutes)', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '01_delivery_time_distribution.png'), dpi=300)
    plt.close()

    # ---------------------------------------------------------
    # Chart 2: The Bottleneck (Traffic Density vs. Time)
    # ---------------------------------------------------------
    print("Generating Chart 2: Traffic vs Delivery Time...")
    plt.figure(figsize=(10, 6))
    traffic_order = ['Low', 'Medium', 'High', 'Jam']
    sns.boxplot(x='Road_traffic_density', y='Time_taken (min)', data=df, 
                order=traffic_order, palette='Reds')
    plt.title('Impact of Traffic Density on Delivery Time', fontsize=16, pad=15)
    plt.xlabel('Traffic Density', fontsize=12)
    plt.ylabel('Delivery Time (Minutes)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '02_traffic_impact.png'), dpi=300)
    plt.close()

    # ---------------------------------------------------------
    # Chart 3: The Environment (Weather Conditions vs. Time)
    # ---------------------------------------------------------
    print("Generating Chart 3: Weather vs Delivery Time...")
    plt.figure(figsize=(12, 6))
    weather_order = df.groupby('Weather_conditions')['Time_taken (min)'].median().sort_values(ascending=False).index
    sns.boxplot(x='Weather_conditions', y='Time_taken (min)', data=df, 
                order=weather_order, palette='Blues_r')
    plt.title('Impact of Weather Conditions on Delivery Time', fontsize=16, pad=15)
    plt.xlabel('Weather Condition', fontsize=12)
    plt.ylabel('Delivery Time (Minutes)', fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '03_weather_impact.png'), dpi=300)
    plt.close()

    # ---------------------------------------------------------
    # Chart 4: The Driver Factor (Ratings vs. Time)
    # ---------------------------------------------------------
    print("Generating Chart 4: Driver Ratings vs Delivery Time...")
    plt.figure(figsize=(10, 6))
    df['Rating_Bin'] = pd.cut(df['Delivery_person_Ratings'], bins=[0, 3, 4, 4.5, 5], labels=['<3', '3-4', '4-4.5', '4.5-5'])
    sns.barplot(x='Rating_Bin', y='Time_taken (min)', data=df, palette='viridis', errorbar=None)
    plt.title('Average Delivery Time by Driver Rating', fontsize=16, pad=15)
    plt.xlabel('Driver Rating', fontsize=12)
    plt.ylabel('Average Delivery Time (Minutes)', fontsize=12)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '04_driver_rating_impact.png'), dpi=300)
    plt.close()

    # ---------------------------------------------------------
    # Chart 5: The Physics (Distance vs. Time)
    # ---------------------------------------------------------
    print("Generating Chart 5: Distance vs Delivery Time...")
    plt.figure(figsize=(10, 6))
    sample_df = df.sample(frac=0.1, random_state=42)
    sns.regplot(x='Distance_km', y='Time_taken (min)', data=sample_df, 
                scatter_kws={'alpha':0.3, 'color':'gray'}, line_kws={'color':'red', 'linewidth': 2})
    plt.title('Correlation: Distance vs Delivery Time', fontsize=16, pad=15)
    plt.xlabel('Distance (km)', fontsize=12)
    plt.ylabel('Delivery Time (Minutes)', fontsize=12)
    plt.xlim(0, 30) 
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '05_distance_correlation.png'), dpi=300)
    plt.close()

    # ---------------------------------------------------------
    # Chart 6: Operations Plot (Vehicle Type and Age vs Time)
    # ---------------------------------------------------------
    print("Generating Chart 6: Vehicle Type and Age vs Delivery Time...")
    plt.figure(figsize=(10, 6))
    # Create age groups for readability
    df['Age_Group'] = pd.cut(df['Delivery_person_Age'], 
                             bins=[18, 25, 35, 45, 60], 
                             labels=['18-25', '26-35', '36-45', '46+'])
    
    # Grouped bar chart comparing vehicle types across age groups
    sns.barplot(x='Age_Group', y='Time_taken (min)', hue='Type_of_vehicle', 
                data=df, palette='Set2', errorbar=None)
    
    plt.title('Delivery Time by Driver Age and Vehicle Type', fontsize=16, pad=15)
    plt.xlabel('Driver Age Group', fontsize=12)
    plt.ylabel('Average Delivery Time (Minutes)', fontsize=12)
    
    # Position legend outside the chart to prevent overlapping bars
    plt.legend(title='Vehicle Type', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, '06_vehicle_and_age_impact.png'), dpi=300)
    plt.close()

    print(f"Success! All charts have been saved to the '{output_dir}' directory.")

if __name__ == "__main__":
    input_filepath = '../data/processed/zomato-cleaned.csv'
    output_directory = '../figures'
    create_visualizations(input_filepath, output_directory)