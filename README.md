# Project_III

## 1. GeoSpatial Data Project
This project aims to find the best location for a new company office based on various requirements and preferences of the employees. The company operates in the GAMING industry and has the following employee distribution:

- 20 Designers
- 5 UI/UX Engineers
- 10 Frontend Developers
- 15 Data Engineers
- 5 Backend Developers
- 20 Account Managers
- 1 Maintenance guy who loves 
- basketball
- 10 Executives
- 1 CEO/President

Requirements:

- Designers prefer to be in proximity - to design-focused companies and attend design talks.
- Approximately 30% of the company - staff have at least one child.
- Developers prefer to be close to successful tech startups that have raised at least 1 Million dollars.
- Executives have a strong preference for Starbucks locations nearby.
- Account managers frequently travel, so good connectivity and proximity to transportation hubs are important.
- The company's employees, who are between 25 and 40 years old, would appreciate nearby entertainment and nightlife options.
- The CEO is vegan, so having vegan-friendly establishments nearby is desirable.
- The maintenance guy would appreciate having a basketball stadium within a 10 km radius.
- The office dog, "Dobby," needs a monthly visit to a nearby dog hairdresser.


## 2. Strategy
To determine the best location for the new company office, a strategy will be implemented based on the defined requirements and preferences of the employees. Each requirement will be assigned a weightage based on the company's values and priorities. Additionally, a maximum distance limit will be set for each requirement to ensure practicality and convenience. The strategy will prioritize the following aspects:

By assigning weights, setting maximum distances, and considering the importance of each requirement, the strategy will guide the selection of a location that best satisfies the company's goals and employee preferences. The weights and distances can be adjusted based on the company's specific values and priorities.

Hereby is the strategy:



## 3. Methodology

### 1. Mongo extraction:

- First, we do an exploration of MongoDb: Before we start, we make an exploration of the data we have to make the best decision
- We take into account competitors from the same category "Video games". Potentially, as more people are interested in design topics related to video games, more probably that design talks take place. We use a 3 condition query, and projection to obtain a data frame with this information.
- Cleaning and extraction data from the df: the column offices contain a list with different dictionaries that we need to take.
- we create a plot to visualize the top 3 cities to focus our research:

- After this, we create a subset of the 3 cities that contains latitude and longitude and we elaborate a heatmap.
- We create a heatmap to visualize where we have our top 3 cities:

### 2. Countries' area decision

- SAN FRANCISCO

- To determine a mean starting point to find venues in Foursquare, we analyze first all the companies that matched our criteria. With all of them, will determine a middle point as a radius. We verify that Sf city has more matched points than Palo Alto. Therefore, we drop Palo Alto:

- We calculate a middle point between all the venues to have a starting point to extract data in Foursquare:

    Location A", "latitude": 37.785077, "longitude": -122.400605}, (3rd avenida/mission st)
    Location B"latitude": 37.781644, "longitude": -122.4057407}  (5th avenue/mission st)
    Location C", "latitude": 37.786873, "longitude": -122.398352} (2nd avenue/mission st)

- NEW YORK


- Same procedure:


- We center our focus in Manhattan.



- SAN FRANCISCO:



With the obtained results, We decide to dismiss and don't explore Los Angeles, as the requirements of more than one company more than 1B$, and related gaming&design companies are not met.

### 3. Apis

- SAN FRANCISCO

- To verify the best location, we need to verify each venue in Foursquare or through external APIs:
    - Api Airport from "https://www.kaggle.com/"
- We iterate through each location of each airport, then, we extract a df per each City to have the closest airports to the main points.
- We query Foursquare about the following venues: schools, vegan restaurants, Starbucks, pet grooming services, and nightclubs&bars.
- Creation of a map through folium to place all the points on the map and evaluate the best place.
- Iteration thought each requirement and weigh. These are the results.

- SAN FRANCISCO RESULTS


### 4. Conclusions

- The best location is in San Francisco (location B) (5th Avenue/mission st) with a total score of 1 ( maximum total score). Location A ens with a 0.7 score, and location A 0.5 score.
- Location B meets all the requirements
- However, location B and C meet 62.5% of the requirements



