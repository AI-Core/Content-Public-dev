# Templates For Lab Deployment

> This document contains information about the required CloudFormation templates for deploying infrastructure for AiCore user labs.

## Table of contents

- [Templates For Lab Deployment](#templates-for-lab-deployment)
  - [Table of contents](#table-of-contents)
  - [Infrastructure](#infrastructure)
    - [Basic Project Template](#basic-project-template)
  - [Setup](#setup)
  - [Lab Specific Guides](#lab-specific-guides)

## Infrastructure

- All required infrastructure for the specified lab is setup using CloudFormation, each lab that requires AWS resources has a dedicated template written in yaml that is used by cloudformation to automate the deployment.

- Current infrastructure and technologies required:
  - S3 (Data Lakes)
  - EC2 (To run docker and docker-compose)
  - Lambda (To run python functions for S3 population)
  - Bash (To run commands for installing dependencies in EC2 instances)

- The basic template for spinning up infrastructure for a lab is defined in `BasicProjectTemplate.yaml` and its components are used in the lab specific templates.

- Data lakes are required to contain the associated data on start of the project, the approach taken to achieve this was to first populate the data lake by means of an S3 to S3 transfer.

    > For some projects (Facebook Marketplace currently), the data is read from the EC2 upon creation, since S3 to S3 transfer is more expensive than reading data. 

- To define the structure needed for creating the stack, follow the syntax used in the [Basic Project Template](BasicProjectTemplate.yaml) file. Name the new file `template.yaml` and move it to the `aws` folder of the specific project. 

  - For example, to create a new template for the `Facebook Marketplace` project, create a new file called `template.yaml` in the `aws` folder in the `scenarios/Facebook-Marketplace` folder.

### Basic Project Template

- The basic project template is used to define the basic infrastructure required for the project. It is a CloudFormation template that is used to create the required resources for the project.

- The template contains the following keys (among others that are not relevant to the resources to be created):

  **`Parameters`**: The variables that will be used to create the resources. _DO NOT EDIT THEM UNLESS THE FUNCTION THAT CREATES THE RESOURCES IS ALSO EDITED._
  - `ProjectUserPassword`: The password that the user will use to login to the AWS console.
  - `AdminUserPassword`: The password that the admin user will use to login to the AWS console.
  - `ProjectID`: The uuid of the project in the database.
  - `UserID`: The uuid of the user in the database.
  - `SourceBucketName`: The name of the bucket that contains the data to be copied to the data lake (or the EC2 if the data is too large).
  - `KeyPairName`: The name of the key pair that will be used to login to the EC2 instance. It defaults to `project_key`.
  <br><br>

  **`Resources`**: The resources that will be created. 
  
  - `AdminRole` **Role**: The role that will be assigned to the admin user allowing them to access the AWS console.
  - `AdminUser` **User**: The admin user that will be created. The password is defined in the `AdminUserPassword` parameter.
  - `ProjectUser` **User**: The user that will be created for the project. The password is defined in the `ProjectUserPassword` parameter.
  - `ProjectUserBasicPolicy` **Policy**: The policy that will be assigned to the project user. It allows the user to access different resources in the AWS console.
  - `LambdaExecutionRole` **Role**: The role that will be assigned to the lambda function that will be created. It allows the lambda function to access the S3 bucket.
  - `CreateEC2KeypairFn` **Lambda Function**: The lambda function that will be used to create the key pair that will be used to login to the EC2 instance. It moves the key to the `SourceBucketName` bucket.
  - `CreateEC2Keypair` **Custom Resource**: The custom resource that will be used to create the key pair. It calls the `CreateEC2KeypairFn` lambda function.
  - `DataLake` **Bucket**. The bucket that will be used as the data lake.
  - `DataLakeBucketPolicy` **Policy**: The policy that will be assigned to the data lake bucket. It allows the project user to get and put objects in the bucket.
  - `s3KeyTransferLambda` **Lambda Function**: The lambda function that will be used to transfer the key pair from the `SourceBucketName` bucket to the `DataLake` bucket.
  - `InvokeKeyTransfer` **Custom Resource**: The custom resource that will be used to invoke the `s3KeyTransferLambda` lambda function.
  - `EC2SecurityGroup` **Security Group**: The security group that will be assigned to the EC2 instance. It allows SSH (port 22) traffic from anywhere.
  - `EC2IAMPolicy` **Policy**: The policy that will be assigned to the EC2 instance. It allows the EC2 instance to get and list objects from the source bucket and to get, list and put objects to the data lake bucket created in the stack.
  - `EC2IAMRole` **Role**: The role that will be assigned to the EC2 instance. It allows the EC2 instance to access the source bucket and the data lake bucket.
  - `EC2InstanceProfile` **Instance Profile**: The instance profile that will be assigned to the EC2 instance. It allows the EC2 instance to access the source bucket and the data lake bucket.
  - `EC2Instance` **EC2 Instance**: The EC2 instance that will be created. It is created using the `EC2IAMRole` role and the `EC2SecurityGroup` security group. It is accessed using the `KeyPairName` key pair. It is created using the `EC2IAMPolicy` policy. Additionally, it has a key called `UserData` that contains the commands that will be run on the EC2 instance upon creation. The commands are used to install docker and awscli. 

Each specific lab will have a particular set of additional resources and commands depending on the requirements of the lab.

The links for each lab template are provided in [the lab specific guides](#lab-specific-guides).

## Setup

- No setup is required as the cloudformation stacks for the labs are nested and called in the user account creation stack.

## Lab Specific Guides

- All lab specific documentation has been moved to their respective folders in the projects directory.

- Links to lab specific templates are provided below:
  - [Facebook Marketplace MLE](/scenarios/Facebook-Marketplace/aws/template.yaml)
  - [Pinterest Data Engineering](/Scenarios/PinterestDataEng/aws/template.yaml)
