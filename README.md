Redbus Data Scraping and Filtering with Streamlit Application
Introduction
The aim is to provide a robust solution for collecting, analyzing, and visualizing bus travel data from Redbus, utilizing Selenium for web scraping and Streamlit for interactive data filtering. This document will focus on the approach to data scraping, storage, and the development of the Streamlit application, with particular attention to the database schema involving the All1 table.

Approach:
1.Data Scraping:
Tool: Selenium
Purpose: Automate the extraction of bus travel data from Redbus.
Data to be Extracted:The Required data attributes are provided in the document.
Bus Routes Name: Start and end locations of the bus journey.
Bus Routes Link: URL for detailed route information.
Bus Name: Name of the bus or service provider.
Bus Type: Type of bus (e.g., Sleeper, Seater, AC, Non-AC).
Departing Time: Scheduled departure time.
Duration: Total journey duration.
Reaching Time: Expected arrival time.
Star Rating: Quality rating provided by passengers.
Price: Ticket cost.
Seat Availability: Number of seats available at the time of scraping.
Process
Setup: Configure Selenium with a web driver (e.g., ChromeDriver).
Navigation: Automate navigation to the relevant sections of the Redbus website.
Data Extraction: Use Selenium to locate and extract data fields from web pages.
Data Storage: Save the extracted data into the SQL database.
2.Data Storage
Table: All1
Data Type: All attributes in the All1 table are of type VARCHAR.
Purpose: Store all scraped data from Redbus in a structured format.
Table Schema
Column Name	Data Type	Description
route_name	VARCHAR	Bus route information for each state transport
route_link	VARCHAR	Link to the route details
busname	VARCHAR	Name of the bus or service provider
bustype	VARCHAR	Type of bus (e.g., Sleeper, Seater, AC, Non-AC)
departing_time	VARCHAR	Departure time (formatted as 'HH:MM')
duration	VARCHAR	Duration of the journey (formatted as 'Xh Ym')
reaching_time	VARCHAR	Arrival time (formatted as 'HH:MM')
star_rating	VARCHAR	Rating provided by passengers (e.g., '4.5')
price	VARCHAR	Ticket price (formatted as a currency string)
seats_available	VARCHAR	Number of seats available
3.Streamlit Application
Objective
Develop an interactive application using Streamlit to display and filter the scraped data.
Features
Data Display: Show the bus data in a table format.
Filters: Implement filters for:
Bus Type: Filter by bus type (e.g., Sleeper, Seater).
Route: Filter by specific bus routes.
Price Range: Filter by ticket price range.
Star Rating: Filter by star rating.
Availability: Filter by seat availability.
Implementation
User Interface: Create a user-friendly interface with Streamlit components.
Data Loading: Load data from the SQL database into the Streamlit application.
Interactive Filters: Use Streamlit widgets to enable dynamic filtering based on user inputs.
Visualization: Display filtered results and visualizations (e.g., charts) if needed.
4>Data Analysis/Filtering
SQL Queries
Purpose: Retrieve and filter data based on user inputs from the Streamlit application.
Examples:
Filter by Bus Type: SELECT * FROM All1 WHERE bustype = 'Sleeper';
Filter by Price Range: SELECT * FROM All1 WHERE price BETWEEN '500' AND '1000';
Filter by Star Rating: SELECT * FROM All1 WHERE star_rating >= '4.0';
Streamlit Integration
Data Interaction: Allow users to interact with and filter the data through Streamlit.
Visualization: Present filtered data in an intuitive and accessible format.
Conclusion
The approach outlined above provides a comprehensive framework for scraping, storing, and analyzing bus travel data from Redbus. By utilizing Selenium for data extraction, storing data in a structured SQL table (All1), and developing an interactive Streamlit application, this project aims to offer valuable insights and improved operational efficiency in the transportation industry.
