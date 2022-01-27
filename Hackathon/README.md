<h2>Overview</h2>
Wipro Limited (NYSE: WIT, BSE: 507685, NSE: WIPRO) is a leading global information technology, consulting and business process services company. We harness the power of cognitive computing, hyper-automation, robotics, cloud, analytics and emerging technologies to help our clients adapt to the digital world and make them successful. A company recognized globally for its comprehensive portfolio of services, strong commitment to sustainability and good corporate citizenship, we have over 220,000 dedicated employees serving clients across six continents. Together, we discover ideas and connect the dots to build a better and a bold new future.

Along with being a global leader in artificial intelligence services from the latest reports of analysts like Forrester, IDC and Everest Group, Wipro has been rated as the second-best organization for data scientists to work in India in 2021 by Analytics India Magazine. The company has also been committed to reaching a Net-Zero Greenhouse Gas Emissions by 2040. 

Though a little late in the day, the world is waking up to the deleterious effect of fossil fuels on our environment. As the doomsday clock ticks away, human beings are turning to renewable energy to avert a possible apocalypse. Fortunately, the sun is a well-spring of clean energy. Taking the cue, Wipro, in association with MachineHack, has designed a forecasting challenge to optimise solar power generation using ML models.

A solar power generation company wants to optimize solar power production and needs the prediction model to predict the Clearsky Global Horizontal Irradiance(GHI). The data is ten years at an interval of every 30 mins with the following data points:

['Year', 'Month', 'Day', 'Hour', 'Minute', 'Temperature', 'Clearsky DHI', 'Clearsky DNI', 'Clearsky GHI', 'Cloud Type', 'Dew Point', 'Fill Flag', 'Relative Humidity', 'Solar Zenith Angle', 'Surface Albedo', 'Pressure', 'Precipitable Water', 'Wind Direction', 'Wind Speed']

<h2>Evaluation</h2>
What is the Metric In this competition? How is the Leaderboard Calculated?
The submission will be evaluated using the Mean Square Error. One can use sklearn.metrics.mean_squared_error to calculate the same
This hackathon supports private and public leaderboards
The public leaderboard is evaluated on 30% of Test data
The private leaderboard will be made available at the end of the hackathon which will be evaluated on 100% of Test data
The Final Score represents the score achieved based on the Best Score on the public leaderboard
How to Generate a valid Submission File
Sklearn models support the predict() method to generate the predicted values
The participant should submit a .csv file with exactly  17,520 rows with 3 column ['Clearsky DHI', 'Clearsky DNI’,'Clearsky GHI']. The submission will return an Invalid Score if you have extra rows or columns.
The file should have exactly 3 column.
