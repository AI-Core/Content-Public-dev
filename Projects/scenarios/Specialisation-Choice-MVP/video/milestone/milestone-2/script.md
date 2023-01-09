# Data Science

So what do data scientists do? Data Scientists are data analytics experts, they can analyse massive datasets from multiple sources using complex techniques, such as: machine learning, statistical analysis and mathematical methods. 

Through their analysis they will gain key insights that can help drive better business decisions.

Data scientists will follow a common lifecycle before their analysis is implemented by the business. 

The first step in the process will be to investigate the businesses needs, you'll need to talk with stakeholders and people at the company to understand how data can help solve the businesses problems.

Once you have a problem to solve the next step will to frame the problem clearly so you can understand what data might help you arrive at a solution. 

Once you've framed the problem you will need to acquire the required data, which could be from multiple data sources. This could be from data engineers in larger organisations who are specialists in structuring and procuring data or you might have to gather the data yourself from multiple sources.

Once the data is gathered it needs to be cleaned and prepared for you to perform your analysis. This could include, removing duplicates from the data, replacing missing values and removing outliers. 

Once your data is cleaned an in the right format you would perform some exploratory data analysis or EDA. This may involve investigating the relationships between each of your datas features, visualising the data and performing some initial statistical analysis. This step is commonly done using the popular python framework allowing you to handle huge datasets.

With the data prepared it's ready to apply your machine learning techniques. This is the experimentation phase where you will train baseline machine learning models to understand how your models perform to solve the problem. You might use packages such as the popular machine learning framework SKlearn to prototype your models. You might create new features from your data to improve your models performance and evaluate and tune the model to get the best possible performance.

The process may further involve critically thinking about whether your model will solve the businesses needs and possibly procurement of new data to improve the performance. 

If your model is performant, at the stage you will be concern with optimising your models performance and collating the results. You would then present your results to show how your model could help with the businesses decision making. If accepted the model would go into to production to be used live.

Following this lifecycle is how you as a data scientist can use your technical expertise to deliver value to a business. 


# Data Engineering

Data Engineers are experts in preparing analytical or operational data for businesses use. Once a companies ingestion of data becomes too great to handle with simple system data engineers will be tasked with developing complex systems to handle a large intake of data. Some companies will crunch millions of records an hour and that data needs to be cleaned stored and easily accessible. It will be your job as a data engineer to manage this data infrastructure, this could include managing data warehouses, data pipelines and databases.

One of the main tasks as a data engineer will be to build data pipelines. A data pipeline is a set of steps that ingest raw data from from a source or multiple sources and move that data to the required destination for storage or analysis. An example of which might be retrieving raw data from an API. Then stream that data in real time using the popular event streaming platform Kafka. In the process of streaming the data you might need to perform many transformations to get the data into a format that is useful for analysis. This can be done using Apache Spark with it's powerful in-memory processing capabilities. After which you might store in teh data in a big data warehouse like cassandra to be easily accessible. 

You will need to have good communication skills as you will need to communicate with many different departments to understand their requirements for the structure, storage and accessibility of their data. Creating these pipelines will involve using many different tools and frameworks, there are multiple options for databases, cloud technologies, data warehouses so you will need to well versed in a broad range of technologies. 

A companies data requirements could very quickly change over time, the amount of data being ingested, what data is required and the speed at which it needs to be delivered will evolve. These factors all need to be taken into account when designed the data architecture. If the business starts ingesting more data you'll need to make sure your systems are built to scale and are fault tolerant when doing so. If your company has new data requirements you might need to design new architecture.

# ML Engineering

A machine learning engineer is someone who has a combination of software engineering expertise and the knowledge of machine learning to build the infrastructure to support artificial intelligence systems. They bridge the gap between data scientists creating the models for use and putting those models into production. Their goal is to create highly performant, scalable and robust systems that learn to improve as more and more data is fed to the system. 

As a machine learning engineer you will need to have a good understanding of machine learning as they will need to work closely with data scientists to understand the models requirements. Using frameworks such as SKlearn and Pytorch can help machine learning engineers tune and optimise the models.

Machine learning are fundamentally different to traditional software systems because they aim to optimise some metric and the best way to optimise it can change overtime. The distribution of data can change overtime due to the change in size or scale of the customer base effecting the metric. 

Since these systems are always running and learning. Machine learning engineers will be tasked with creating continuous deployment systems which can quickly retrain, test, scale and deploy the machine learning models.

This could involve many techniques such as storing models in a model store to make them readily available to be deployed. Containerising the model using specialist tools like Docker so that the model is easily reproducible and can be deployed anywhere. 

Machine learning engineers will need to implement monitoring systems to catch any drift in the data so that models can be quickly retrained and deployed to ensure the stability of the system. 

# Data Analyst

Data analysts collect, clean and interpret trends in data to allow a business to make better data-driven decisions. The role of the data analyst could take on many forms depending on the extent to which the business makes data driven decisions. 

This could include the maintenance and fixing of data related code if you're working in a small company.  You might be developing processes and systems to make data more easily accessible and more efficiently accessed. Due to their interaction with data on a daily basis they will need to be well versed in the data querying language SQL.

They might use specialist tools such as Pandas to clean, prepare and perform statistical analysis of the data to gain a better insight into it's meaning.

They will use tools such as Tableau to help visualise the data into more easily understandable formats such as diagrams, graphs, dashboards or reports to help tell the story of the data. 

After visualising the data they will present their findings to business stakeholders to help them make more informed data driven decisions. 
