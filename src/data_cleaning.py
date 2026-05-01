import pandas as pd
import numpy as np

def haversine(lat1, lon1, lat2, lon2):
    """Calculates distance between two coordinates in kilometers."""
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a)) 
    r = 6371 # Radius of earth in kilometers
    return c * r

def clean_zomato_data(filepath):
    """
    Loads raw Zomato data, imputes missing values, 
    engineers the distance feature, and returns a clean DataFrame.
    """
    # 1. Load the data
    df = pd.read_csv(filepath)
    
    # 2. Fill Missing Numerical Values
    df['Delivery_person_Age'] = df['Delivery_person_Age'].fillna(df['Delivery_person_Age'].median())
    df['Delivery_person_Ratings'] = df['Delivery_person_Ratings'].fillna(df['Delivery_person_Ratings'].median())
    df['multiple_deliveries'] = df['multiple_deliveries'].fillna(df['multiple_deliveries'].median())
    
    # 3. Fill Missing Categorical Values
    df['Weather_conditions'] = df['Weather_conditions'].fillna(df['Weather_conditions'].mode()[0])
    df['Road_traffic_density'] = df['Road_traffic_density'].fillna(df['Road_traffic_density'].mode()[0])
    df['Festival'] = df['Festival'].fillna(df['Festival'].mode()[0])
    df['City'] = df['City'].fillna(df['City'].mode()[0])
    
    # 4. Drop unfillable rows
    df.dropna(subset=['Time_Orderd'], inplace=True)
    
    # 5. Feature Engineering: Distance
    df['Distance_km'] = haversine(df['Restaurant_latitude'], df['Restaurant_longitude'], 
                                  df['Delivery_location_latitude'], df['Delivery_location_longitude'])
    
    # Filter out extreme anomalies in distance (e.g. distance > 50km)
    df = df[df['Distance_km'] <= 50]
    
    return df

if __name__ == "__main__":
    # Test the function by running this script directly
    clean_df = clean_zomato_data('data/raw/zomato-dataset.csv') # Update filename if needed
    
    # Save the cleaned dataset to the processed folder
    clean_df.to_csv('data/processed/zomato-cleaned.csv', index=False)
    print("Data cleaned and saved to data/processed/zomato-cleaned.csv")