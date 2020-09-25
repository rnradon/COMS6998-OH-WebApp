
# WebApp Basics and Demo

### What is a WebApp?
A software or a program which runs on a web server and is accessible using any web browser. 
It constitutes of three things:
1. **front-end**: Usually created using languages like HTML, CSS, Javascript, which are supported by major browsers. They are static files and are generally stored in static web hosting containers like Amazon S3.

2. **back-end**: Application program or logic that essentially runs the web application. This program logic can hosted on Elastic Beanstalk, Lambda Handlers, EC2, etc.

4. **REST APIs**: A channel or a service that allows you to communicate with the back-end program without essentially understanding the server logic running in the background.
For instance: lets explore this open API [http://dummy.restapiexample.com/](http://dummy.restapiexample.com/)

### Lets talk about MVC
![What is MVC Architecture?](https://www.w3schools.in/wp-content/uploads/2019/03/MVC-Architecture.png)
Image taken from: [https://www.w3schools.in/mvc-architecture/](https://www.w3schools.in/mvc-architecture/)

1.  **Model**: Model is responsible for interacting with the database. However, model doesn't deal with any application logic regarding how to present the data.
2.  **View**: View is something that we see on the front-end, ie presentation of the data fetched by the model. This layer is the layer with which the user communicates.
3.  **Controller**: Controller defines the application logic that on request (either from view, or direct HTTP API request) performs the operations and sends the request to model to fetch the relevant data. We can also term it as something that allows user (from view or REST APIs) to communicate with the model (database).
_______
### Lets dive deep and create a simple WebApp
As mentioned earlier, we'll be having three components namely frontend, backend and APIs. APIs are exposed in the backend itself.

#### 1. Front End
We'll be using Vue.JS in the demo, however, there are many other JavaScript frameworks (Angular, React, Vue, etc) that you can use.

> *client/* Contains the Front End logic

##### Why do we need such frameworks?
They support the MVC architecture and are modular in nature whether it is components, directives, pipes, or services making application functionality organization easy, segregating it into features and reusable chunks.

##### Deployment
We'll be hosting the "static" site on S3 Bucket


#### 2. Back End
We'll be using Flask (framework provided by Python). We do have other frameworks such as Django, Express, etc, and can choose any of our choice. 
This segmenet constitutes of the application logic
> *server/* Contains the Back End logic

##### Deployment
For deployment, we need a server that can run our business logic. As mentioned above, we can use EC2, ElasticBeanstalk, or even Lambdas to do the same.
In this tutorial, however, we are using ElasticBeanstalk

##### Advantages of EB:
1. Quickly deploy and manage applications in the AWS Cloud

2. No need to worry about the infrastructure that runs those applications.

3. Elastic Beanstalk automatically handles
		a. Capacity provisioning
		b. Load balancing
		c. Scaling
		d. Application health monitoring.

Supports Go Java, .NET, Node.js, PHP, Python, and Ruby, as well as different platform configurations for each language.

Easy to use EBCLI to deploy apps to Elastic Beanstalk

https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

Website Link:
http://webapp-rn2490.s3-website-us-east-1.amazonaws.com/#/ta