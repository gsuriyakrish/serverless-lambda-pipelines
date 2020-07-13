# Serverless Implemetation #
This project is intended for implementing a serverless computing with AWS

# Description #
 1. The project uses [serverless](https://serverless.com) architecture with single service multiple AWS Lambda functions. \
 2. Maintaining a multiple versions. \
 3. CI/CD with [Bitbucket pipelines](https://bitbucket.org/product/features/pipelines). \
 4. Two stages (dev, stage, prod) with two versions of code in each to differentiate the lambda consumption. \
 5. UnitTest with nose (Easy and fastest implementation). \
 6. buildspec.yml is available for AWSCodeBuild (Just a base reference for this project - **Not Implemented**). \
 7. serverless.yml for deploying to AWS with serverless framework.

# Run the project #
1. Download this project or clone the repository.
2. Go to the project folder.
3. Create a virtual environment \
     &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; - virtualenv venv
4. Activate the environment \
     &nbsp; &nbsp; &nbsp; &nbsp;  - source venv/bin/activate
5. Install dependencies \
     &nbsp; &nbsp; &nbsp; &nbsp;  - pip install -r requirements.txt
6. Run the unittests with nosetests \
     &nbsp; &nbsp; &nbsp; &nbsp;  - nosetests -sv --with-xunit --xunit-file=nosetests.xml
7. Local lambda deployment using invoke \
     &nbsp; &nbsp; &nbsp; &nbsp;  - sls invoke local -f fibonacci-version1 -p unit_test_data/fibonacci.json \
     &nbsp; &nbsp; &nbsp; &nbsp;  - sls invoke local -f factorial-version1 -p unit_test_data/factorial.json \
     &nbsp; &nbsp; &nbsp; &nbsp;  - sls invoke local -f ackermann-version1 -p unit_test_data/ackermann.json
8. Deploy into AWS from local \
     &nbsp; &nbsp; &nbsp; &nbsp;  - sls deploy
9. After a couple of minutes, the endpoints will get exposed in the terminal and open the endpoints by passing parameters (https://XXXXX.XX.XXapigateway/version_2/factorial?n=6)

# Reference Screenshots #

![reference_screenshots](reference_screenshots/Deploying_in_master.png)

![reference_screenshots](reference_screenshots/Deployment_Pipelines.png)

![reference_screenshots](reference_screenshots/Deployment_Stage.png)

![reference_screenshots](reference_screenshots/Cloud_Formation_using_SLS.png)

![reference_screenshots](reference_screenshots/Lambda.png)

![reference_screenshots](reference_screenshots/API_Gateway.png)

![reference_screenshots](reference_screenshots/API_Gateway_Methods.png)

![reference_screenshots](reference_screenshots/Dashboard.png)






 
         
      
 