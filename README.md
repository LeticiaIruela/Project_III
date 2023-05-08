# Project_III
![image](https://user-images.githubusercontent.com/128729754/236957549-14ea18b5-84d7-46a2-8cb7-7d7ba9016926.png)

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
- 
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

<img width="589" alt="19" src="https://user-images.githubusercontent.com/128729754/236957256-d9c6197d-7c2f-4eba-bdf0-471323979931.PNG">

- SAN FRANCISCO RESULTS

<img width="591" alt="20" src="https://user-images.githubusercontent.com/128729754/236957285-9d4c80f2-1527-438a-99f4-e7ca395f4c3f.PNG">

<img width="624" alt="21" src="https://user-images.githubusercontent.com/128729754/236957297-2e6028e7-6a57-4873-bb16-da44b893669c.PNG">


### 4. Conclusions

- The best location is in San Francisco (location B) (5th Avenue/mission st) with a total score of 1 ( maximum total score). Location A ens with a 0.7 score, and location A 0.5 score.
- Location B meets all the requirements
- However, location B and C meet 62.5% of the requirements



