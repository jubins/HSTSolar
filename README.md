# Client Matching App
This app has been created using Python Django web framework as backend, MongoDB as database and HTML, CSS, Bootstrap and jQuery for the fronend.
In this app I have created two interfaces:
1. A view where a seller can create a list of energy (kWhs) to sell from projects, and
2. A view where a buyer can input a location and desired quantity of energy, and will be given a
list of projects to buy from.

### Setup
You will need to Python 3, Django 2.2 and MongoDb to run this project.
All other dependencies are mentioned in the `requirements.txt` file or you can use directly use `venv` file as your virtual environment that has dependencies preloaded.
Once the above steps are done, go to your terminal and type
```
# To activate the virtual environment
source venv/bin/activate

# To start the django server
python manage.py runserver
```
You should see something like below output in your terminal which indicates django server has started
```
Performing system checks...

System check identified no issues (0 silenced).
February 17, 2020 - 06:28:26
Django version 2.2.10, using settings 'SolarShop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Go to http://127.0.0.1:8000/ browser and you should be able to access the pages.

### Homepage
This is the first page you will see when you start the project
![Dashboard](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/homepage.png)

### Seller Page
The seller page follows these properties:
1. A name
2. A location (latitude/longitude)
3. An amount of energy to sell (kWh)
4. A price for the energy ($/kWh)

The view consists of:
1. An interface where the user can input the above properties to create a new project
2. A list of projects that user has created

Note:
- Every project in the list is not editable, but it is deletable.

Seller Page Create Project
![SellerApp_CreateProject](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/sellerpage_create_project.png)

Seller Page Delete Project
![SellerApp_DeleteProject](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/sellerpage_delete_project.png)

Seller Page Form Validation
![SellerApp_FormValidation](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/sellerpage_form_validation.png)

Seller Page Location Tracking - for easy input via browser
![SellerApp_LocationTracking](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/sellerpage_location_tracking.png)


### Buyer Page
The Buyer view follows below properties:
1. A set of inputs that allows the user to enter a location (latitude/longitude) and an amount
of energy (kWh).
2. A list (returned by the above query) of project names, the amount of energy purchased from
each project (kWh), and the amount of money spent on that energy ($).

Note:
- The user wants to pay as little as possible for the inputted energy, so I have sorted the energy by price in ascending order to the price is shown from lowest to highest.
- The projects that the query returns are within 500km of the requested location, I have made this option configurable in the input with 500km as default value.
- A user does not have to purchase all of the energy provided by a project. For example, if the
user requests 100kWh, and the only project within 500km is selling 500kWh, then the user
would only have to buy 100kWh of the available 500kWh.
- If there is not available energy nearby to satisfy the query, the user sees a list of all
the energy they can purchase, and receive a message detailing how much energy they
would still need to find.

Buyer Page Filtered Results - based on search criteria
![BuyerApp_FilteredResults](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/buyerpage_filtered_results.png)

Buyer Page All Results - when no criteria matches search query
![BuyerApp_AllResults](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/buyerpage_all_results.png)

Buyer Page Form Validation
![BuyerApp_FormValidation](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/buyerpage_form_validation.png)

Buyer Page Location Tracking - for easy input via browser
![BuyerApp_LocationTracking](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/buyerpage_location_tracking.png)


### Database
![MongoDb](https://raw.githubusercontent.com/jubins/HSTSolar/master/images/mongodb.png)
