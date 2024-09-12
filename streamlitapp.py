import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

# Connect to MySQL database using SQLAlchemy
def get_connection():
    engine = create_engine('mysql+pymysql://chakradhar:chakradhar123456789@localhost/bus')
    return engine

# Function to fetch route names starting with a specific letter, arranged alphabetically
def fetch_route_names(engine, starting_letter):
    query = text("SELECT DISTINCT Route_Name FROM all1 WHERE Route_Name LIKE :starting_letter ORDER BY Route_Name")
    with engine.connect() as connection:
        result = pd.read_sql(query, connection, params={"starting_letter": f"{starting_letter.upper()}%"})
    return result['Route_Name'].tolist()

# Function to fetch data based on Route_Name and price sorting order
def fetch_data(engine, route_name, price_sort_order):
    price_sort_order_sql = "ASC" if price_sort_order == "Low to High" else "DESC"
    query = text("SELECT * FROM all1 WHERE Route_Name = :route_name ORDER BY Star_Rating DESC, Price " + price_sort_order_sql)
    with engine.connect() as connection:
        df = pd.read_sql(query, connection, params={"route_name": route_name})
    return df

# Function to filter data based on Star_Rating and Bus_Type
def filter_data(df, star_ratings, bus_types):
    filtered_df = df[df['Star_Rating'].isin(star_ratings) & df['Bus_Type'].isin(bus_types)]
    return filtered_df

def main():
    st.header('Easy and Secure Online Bus Tickets Booking')

    engine = get_connection()

    try:
        # Sidebar - Input for starting letter
        starting_letter = st.sidebar.text_input('Enter starting letter of Route Name', 'A')

        # Fetch route names starting with the specified letter
        if starting_letter:
            route_names = fetch_route_names(engine, starting_letter)

            if route_names:
                # Sidebar - Radio for Route_Name
                selected_route = st.sidebar.radio('Select Route Name', route_names)

                if selected_route:
                    # Sidebar - Selectbox for sorting preference
                    price_sort_order = st.sidebar.selectbox('Sort by Price', ['Low to High', 'High to Low'])

                    # Fetch data based on selected Route_Name and price sort order
                    data = fetch_data(engine, selected_route, price_sort_order)

                    if not data.empty:
                        # Display data table with a subheader
                        st.write(f"### Data for Route: {selected_route}")
                        st.write(data)

                        # Filter by Star_Rating and Bus_Type
                        star_ratings = data['Star_Rating'].unique().tolist()
                        selected_ratings = st.multiselect('Filter by Star Rating', star_ratings)

                        bus_types = data['Bus_Type'].unique().tolist()
                        selected_bus_types = st.multiselect('Filter by Bus Type', bus_types)

                        if selected_ratings and selected_bus_types:
                            filtered_data = filter_data(data, selected_ratings, selected_bus_types)
                            # Display filtered data table with a subheader
                            st.write(f"### Filtered Data for Star Rating: {selected_ratings} and Bus Type: {selected_bus_types}")
                            st.write(filtered_data)
                    else:
                        st.write(f"No data found for Route: {selected_route} with the specified price sort order.")
            else:
                st.write("No routes found starting with the specified letter.")
    finally:
        engine.dispose()  # Dispose of the SQLAlchemy engine

if __name__ == '__main__':
    main()
