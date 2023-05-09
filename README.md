# Project_III
![image](https://user-images.githubusercontent.com/128729754/237021617-e63f8d07-c018-449c-820d-6ab3a1deec74.png)

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

<img width="456" alt="requi" src="https://user-images.githubusercontent.com/128729754/236957237-b58d33a3-dad1-44ce-a1d1-cab062f3d6cf.PNG">

By assigning weights, setting maximum distances, and considering the importance of each requirement, the strategy will guide the selection of a location that best satisfies the company's goals and employee preferences. The weights and distances can be adjusted based on the company's specific values and priorities.

## 3. Methodology

### 1. Mongo extraction:

- First, we do an exploration of MongoDb: Before we start, we make an exploration of the data we have to make the best decision
- We take into account competitors from the same category "Video games". Potentially, as more people are interested in design topics related to video games, more probably that design talks take place. We use a 3 condition query, and projection to obtain a data frame with this information.
- Cleaning and extraction data from the df: the column offices contain a list with different dictionaries that we need to take.
- we create a plot to visualize the top 3 cities to focus our research:

<img width="583" alt="12" src="https://user-images.githubusercontent.com/128729754/236956939-69fff5f5-a44e-4784-bc29-52d99cb7811a.PNG">

- After this, we create a subset of the 3 cities that contains latitude and longitude and we elaborate a heatmap.
- We create a heatmap to visualize where we have our top 3 cities:

<img width="556" alt="13" src="https://user-images.githubusercontent.com/128729754/236956966-d46a9512-6446-438a-9882-f9378a3d80f1.PNG">

### 2. Countries' area decision

- SAN FRANCISCO

To determine a mean starting point to find venues in Foursquare, we analyze first all the companies that matched our criteria. With all of them, will determine a middle point as a radius. We verify that Sf city has more matched points than Palo Alto. Therefore, we drop Palo Alto:

<img width="503" alt="14" src="https://user-images.githubusercontent.com/128729754/236956993-4eabf6c8-cfd6-4f8c-92e1-dedf0f947cbb.PNG">
<img width="463" alt="15" src="https://user-images.githubusercontent.com/128729754/236957046-aeeae429-0f61-47a7-8880-9b8ec1dea002.PNG">

 We calculate a middle point between all the venues to have a starting point to extract data in Foursquare:

    Location A, latitude: 37.785077, "longitude": -122.400605}, (3rd avenida/mission st)
    Location B latitude: 37.781644, "longitude": -122.4057407}  (5th avenue/mission st)
    Location C, latitude": 37.786873, "longitude": -122.398352} (2nd avenue/mission st)
    
    
    ![image](https://user-images.githubusercontent.com/128729754/236957107-1c7300e1-b44e-4376-99fe-1dd43b2ad1fd.png)

- NEW YORK

 Same procedure:
 
<img width="494" alt="16" src="https://user-images.githubusercontent.com/128729754/236957130-e402fa01-1cae-4815-a2bf-bf795bf65979.PNG">

 We center our focus in Manhattan.
 
<img width="476" alt="Capture17" src="https://user-images.githubusercontent.com/128729754/236957160-9b8dab45-a184-47b4-bcaa-2b47c9a5610c.PNG">

- LOS ANGELES:

<img width="530" alt="18" src="https://user-images.githubusercontent.com/128729754/236957202-b5ab2a13-5e40-4e21-8305-8263edac6573.PNG">

  With the obtained results, We decide to dismiss and don't explore Los Angeles, as the requirements of more than one company more than 1B$, and related gaming&design companies are not met.

### 3. Apis

- SAN FRANCISCO

To verify the best location, we need to verify each venue in Foursquare or through external APIs:
    - Api Airport from "https://www.kaggle.com/"
We iterate through each location of each airport, then, we extract a df per each City to have the closest airports to the main points.
We query Foursquare about the following venues: schools, vegan restaurants, Starbucks, pet grooming services, and nightclubs&bars.
Creation of a map through folium to place all the points on the map and evaluate the best place.
Iteration thought each requirement and weigh. These are the results:

<img width="405" alt="compli_scores" src="https://user-images.githubusercontent.com/128729754/237003632-05b5bc3e-4a85-489b-836b-04af988925db.PNG">


- SAN FRANCISCO RESULTS

<img width="947" alt="requirements" src="https://user-images.githubusercontent.com/128729754/237003703-8455210a-7b89-4d04-a0dc-327e0652f751.PNG">
<img width="905" alt="compliance scores" src="https://user-images.githubusercontent.com/128729754/237003739-381f3db1-e913-4e00-91cd-e5fba4485d25.PNG">

### 4. Conclusions

- The best locations is in San Francisco (location A & B) (3rd avenue/ mission st and 5th Avenue/mission st) with a total score of 1 ( maximum total score). Location C ends with a 0.6 score,.
- Location A & B meets all the requirements, C with 75% compliance

