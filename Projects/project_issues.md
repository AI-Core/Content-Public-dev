### Data collection pipeline

(Blair)
- The use of friendly ID's and UIID4 is unclear people have no idea why they're doing it and what the use of it is. 
- Unclear to people what method to use to stop rescraping of the data. 
- A lot of questions about whether to upload, drop dups in batch, or stream a single json per data point and what the trade offs are with it. 
- People not sure whether to use a list of dictionaries or a dictionary of lists. 
- Testing is super confusing for people if they're writing their code wrongly to begin with they struggle to test it. Lack of parameters for users in their methods. No return statements from functions so there is no object to test. 
- No mention on the course I think at the moment unless it's recently been updated on how to protect credentials. We need content on supplying the credentials to the container/scraper locally at runtime and having those credentials not uploaded to Github or baked into a docker image. 
- People adding too much to their projects sometimes they don't know when to stop. 
- Seem to see more websites getting blocked these days, lot of Cloudflare protection. 
- Unclear to people that a Docker container has it's own network, file structure so they aren't aware that it has it's own system inside. So related file paths on their system don't relate to file paths inside the container.  
- I don't think there is any mention of ports or networking in general on the course so that's confusing for people. 
- There are three layers to the networking we have the docker container on an EC2 trying to be accessed from the local machine a lot to understand if you aren't sure about ports or the correct IP addresses to use.
- No observability with cron jobs, hard for people to understand if it's working or not. 

(Maya)
- People are confused about testing. There is no clear content on which methods should be tested which should not --> content on private versus public methods. Essentials for them to understand for testing
- seen a lot of users recently scraping data by going to final product page - changing the URL. Need to make it clear that they need to write navigation methods themselves.

### Computer Vision Rock Paper Scissors

(Blair)
- What is going on with the template code is confusing for users. They don't know why it needs to be in a while loop and how it is capturing frames from the camera/getting predictions from the model. 
- Not obvious why we need to use a countdown to change the state of the game. Could do with a video example on why for instance sleep won't work. 
- People normally get stuck at providing the prediction from the model to their rock, paper, scissors game. They're unsure that the 
- Don't normally have as many issue with the project though. 

(Maya)
- users confused if predictions should be continuous and why if we are only interested in the prediction when timer is equal to zero.
- M1 issues with installing tenserflow + M2 issues for opencv

(Ivan)
- Users don't understand why the error says `cv2` not found when they have installed opencv. Perhaps just explain how to create and activate a virtual environment in the terminal, VSCode, and Jupyter Notebook.
- They usually ask questions about the warning messages thrown by tensorflow
- They have difficulties thinking logically about the methods and how they interact between each others
- They forget about using self in the methods
- Not so common, but I've seen a few times. Using `global` keyword. 

### Hangman Project

(Blair)
- No mention to use `isalpha()` to check if the letter is a character. I have seen all sorts of implementations not using `isalpha()` which people struggle to get working.
- The only other part people mainly struggle with is inserting duplicate letters into the word but I think it's ok it's just the hardest part of the project.
- Biggest issue I see is people not knowing that because their terminal is in the base conda environment it doesn't mean that VSCode's interpreter is set to that environment.
- Environment use is still confusing for users why are they using different environments?
- See a lot of users having Github repos inside other Git repos causing a lot of problems.  

(Maya)
- main issue is people not being able to run their code, because when they do it from Jupyter Notebooks it's not clear to them how to select the correct environment in which they installed the necessary dependencies. 

(Ivan)

- Users confuse parameters, arguments, and attributes

### Data Engineering project

(Blair)
- A lot of MAC issues just generally certain things not working with it, cassandra and presto being the main ones. 
- No support for M1 MACs with Presto so it needs to be containerised or a work around for it. Maya has now added a work around to the Presto notebook so this should work ok now. 
- Airflow content needs updated it's very confusing for people, people find it hard to implement. 
- People not sure how to get the data on S3 is the slowest part of the project. 
- Spark streaming content is totally outdated so when it comes to streaming they get stuck. They don't know to use `foreachBatch` method of the write stream to apply transformations to each mini batch of data. 

(Maya)
- Mac issues for Spark, Cassandra, Presto & monitoring tools Prometheus & Grafana. Problem is there no content on homebrew for Mac, they should be encouraged to use it
- Cassandra and Presto milestones are poor. We hardly show them how to install and load some data in. Hard for users to understand why are we using these tools, as they are not making use of their strengths
- people overcomplicating reading data from S3 bucket which leads to corrupted records.
- Spark transformations are ambigous - should include what are the transformations they need to make so they get more practice with using pyspark.


### Data Science project

(Ivan)

- Users find it hard to understand what's the difference between test and validation set. They are not sure if they should use the validation set to tune the hyperparameters or not
- Users don't know how to find the dataset
- Users don't know how to create DataLoaders and why they are needed
- Users don't know how to tune the hyperparameters, or why they are needed

### Machine Learning project

(Ivan)

- Users don't know how to use and what TF-IDF is. Perhaps we can add a link to a video or a blog post that explains it.
- The same problems as with the Data Science project actually
