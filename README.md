# geir-dashboard

This is a Google Appengine Python powered dashboard with JSON API from Quandl

## Run Locally

You will need the following thins properly installed on you computer.
- [Git](http://git-scm.com)
- [ App Engine Python SDK](https://cloud.google.com/appengine/downloads)

Then you can run this project locally from the command line:
```
dev_appserver.py .
```

## Aplication Flow
### Populating the datastore and getting information from Quandl
The aplication take a list of stocks, commodities, exchanges rates and interest rates (Defined in the model of every object `/app/core/models/<object_model.py>`)
and make requests to the Quandl API in order to get information for every object. It procces this information
and save it in the ndb datastore. This procces is all made when making a request to `/tasks/update-info/`
This procces is made every 120 minutes. You can change this cron job in the `cron.yaml` file.
### Viewing the information
When the user make a request to `/`, the application query all the information about the objects to the ndb database
and it render it with Jinja2 in the dashboard.

## Structure
```
/app
  /core
    /controllers
    /helpers
    /models
  /templates
  /tests
```
### Core
You can find all the source code of the application in core. It contains the main files that supports the entire app.

#### Controllers
Controllers have the task of making sense of a request and returning an appropriate response.
Web applications typically support adding, editing, deleting and showing details of a resource.
In this app we only have the controller for the main page.

#### Helpers
We define here all the methods that help the controllers to perform it's task. 
We define the helper to get and procces all the information from the Quandl API here.

#### Models
The model describes how the data looks like. We have here a model for every object (Stock, Commoditie, Exchange rates and Interest rates).
All this objects have the same structure. That is why we define a base model with this structure, and the we extend the other models from the base_model.

### Templates
We have here all the templates for every route or controller. We just have the main page template.

#### Static
We have here all our assets(Javascript, CSS, ...) and dependencies. We are using bootstrap.

### Tests
We define here our unit test. We start the application doing TDD with the Quandl Helper because is the main code of the entire app. Here we query the information that we need for every object.
