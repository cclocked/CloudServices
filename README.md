# CloudServices
School project, working with Microsoft Azure


## Backround
The purpose of the project was to complete a task for a school asignment and learn more about working with cloud services, where i have choosen to work with
Microsoft Azure. The project it self relies on some SaaS from the Azure platform.

## Components used in the project and execution:
During the projects course i've tried a wide array of services and methods to try and achive the goal of getting data to storage and displaying it, such as node.js,vanilla js, python, azure function etc. The components that made the cut for the projects were as followed:
- A very simple python program i wrote which took data from openweathermap api to the cosmos databas with the help of the azure/cosmos sdk.
- The virtual raspberry pi provided by Azure
- Message routing in Azure to get the telementery messeages from the raspberrypi to the database.
- A cosmos DB database to facilitate the data and be used to display the readings.
- Power Bi visualization for the data.
- In the begning I worked with Javascript to create a webapp that took data directly from openweathermaps API and showed it on the webapp it looked like this , 


  ![jsgrej](https://user-images.githubusercontent.com/113606983/207416753-5d731d61-531f-4c50-b6f1-640bdb01c1cb.jpg)
But since the criteria for a grade was to display data with the use of cloud services, I decided to instead use Micrososfts Power BI which is included in the Azure platform to satisfy the requirement.
The final visualization based on a few exerts from the database looked like this, taken from Power BI,
![powerbi temps](https://user-images.githubusercontent.com/113606983/207444096-c06ce69f-011c-40c0-ab97-83ab73b8a4e9.png)
There was an issue with getting the data from the virtual raspberryPi to the database in JSON format beacuse it was encrypted with base64, and none of the changed applied to the message-route seemed to make any difference. Same issue with the Raspberry code itself, trying to change to json format with utf-8 was futile. So what I had to do was to convert the raspberries messages from base64 to json and then insert to a csv file which I then upploaded to Power BI to display the data.


## Thoughts about improvment, what went wrong and possible solutions
- One of the big issues with the final stages of the project was the visualization of the data, I would have loved to use the embedded Power BI in azure to show my data but the plan was way to expensive for a school project. So finding a better solution to show data would had been a preferable solution to using the exact same app but not on the cloud.
- Another thing was the encryption that occured with the virtual raspberryPi which was a thorn in the side. I did contemplate to send the data to python, decode it there to later send it back decrypted. But that felt like overkill. I belive that if i would have owned my own device that was capable of conecting to the internet it would maybe have made things easier.
Other than that im pretty content with the project as a whole and feel I have acomplished what is asked of me to complete the task as it contains,
- A simple IoT design, with the raspberry and platform.
- Cloud services related to IoT
- Storage and write/read
- Communication between the raspberry,Hub and database.
- Power Bi visualization for the data.

## MISC
Alot of the services provided by Azure are scaleable pretty easily. Most of the services can be "pay as you go" which means you only pay for what you use, and can be canceled at any time, which makes it perfect if your just trying something out or are moving to downscale or upscale something. Which is why this one of their most popular payment plans.
If it was a more serious project that would have hit the market, Azure alows it's users to incorporate IoT-security right from the hub which i think costs around $0.001 per device per month. This can be applied to just about anything in the hub, everything from device-twins to services/functions running on the platform.

## conclusion
Work finished , thanks for reading.
