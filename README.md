# PC Experience

Live version [here](https://pcexperience.herokuapp.com/)

## Index

* [Project description](#project-description)
* [UX](#ux)
* [Features](#features)
* [Wireframes](#wireframes)
* [Technologies](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Disclaimer](#disclaimer)

## Project Description

PC Experience is a PC Hardware online store. The user can find all main PC hardware components like Motherboards, CPUs, Memory, storage, Power supplies etc.
The user is able to search for products on any category, purchase them, access their profile, with order history and edit their shopbag.  

## UX

### Who is it for

* Store owner, that wants to create a online presence selling their products online and able to manage their products.
* PC Enthusiasts that are looking into upgrading or building their own computers
* General PC user, that needs a specific component, looking into upgrade or just wants to have an idea on how much they'll need to spend on upgrades or what they need to build a PC from scratch.

### User Stories

* As a Owner, I want to be able to add/edit/remove products from my store.
* As a Owner, I want to be able to add news regarding my store, in order to help promote my products.
* As a Owner/Enthusiast/General, I want to be able to see details about each product.
* As a Owner/Enthusiast/General, I want to be able to sign in and logout easily
* As a Owner/Enthusiast/General, I want to be able to search for any specific product, to find quickly what I'm looking for.
* As a Owner/Enthusiast/General, I want to easy navigate so I can find the information I need quickly.
* As a Owner/Enthusiast/General, I want to view components in specific categories so it's easier to find what I want.
* As a Enthusiast/General, I want to be able to create an account, so I can see my order history and update my delivery information in case I order more items.
* As a Enthusiast/General, I want to be able to recover my password in case I forget.
* As a Enthusiast/General, I want to receive a confirmation email, so I know the registration was completed.
* As a Enthusiast/General, I want to view the products I've added to my cart
* As a Enthusiast/General, I want to be able to remove/update items from my cart, In case I add something by mistake or add the incorrect quantity.

## Features

### Existing Features

* Navbar
  * Allows user to navigate easily through the different product categories and sections of the page.

* News
  * Allows the store owner, to create posts about promotions, any store/tech related news with the following categories: News, Info, Promos

* Shopping bag
  * Users ability to add and remove items and update quantities.

* Footer
  * Provides links to the relevant social websites, payment information and quick links to the store.

* Account
  * Ability to create accounts, reset password, logout
  * Product management - Store owner is able to Add, Edit and remove any products.
  * News - Store owner can create posts about promotions, Information or any Store/tech products related news.
  * Profile - User can see their order history and save/update their delivery information.

* Search
  * Ability to search any products in the page

* Product details
  * User can see detailed information for any product chosen and select the quantity they want to purchase and add it to the bag.

### Features left to implement

I would like to implement more features in this app like:

* Stock system
  * Ability to show the user the product availability status: In stock, low stock and out of stock.
* News Comments
  * Ability for the user to comment in the store owner posts in the news section.
* Forum
  * A good addition to the news section where the users could join and discuss tech and other topics.
* Share feature
  * Ability to share news, products in social media
* Social media integration
  * Allow user to use their social media credentials to speed up the login/account creation process.
* Product review
  * Allow user provide their reviews about a product.
  
## Wireframes

Wireframes done with Balsamiq, available here:

* [Desktop](https://github.com/Brainvibe/1UpLoot/blob/master/data/wireframes/Desktop.png)
* [Mobile](https://github.com/Brainvibe/1UpLoot/blob/master/data/wireframes/Mobile.png)
* [Tablet](https://github.com/Brainvibe/1UpLoot/blob/master/data/wireframes/Tablet.png)

## Technologies Used

### Languages

* **[HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)**
  * The project uses HTML to structure the DOM.
* **[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)**
  * Used to style webpages.
* **[JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)**
  * Used to provide interactive and dynamic content on the front end.
* **[Python 3](https://www.python.org/)**
  * Used for all backend functionality.

### Frameworks, tools and Libraries

* **[Django 3.1.1](https://www.djangoproject.com/)**
  * Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* **[Django-Allauth](https://www.intenct.nl/projects/django-allauth/)**
  * A Django app that provides a pre-made user authentication system, using this ensures the login components of this project are well developed and secure
* **[Django-Crispy-Forms](https://github.com/django-crispy-forms/django-crispy-forms)**
  * Allows the use of Django forms. Build programmatic reusable layouts out of components, having full control of the rendered HTML without writing HTML in templates
* **[Stripe](https://stripe.com/)**
  * Payment integration for ecommerce
* **[JQuery](https://jquery.com)**
  * A JavaScript framework to simplify DOM manipulation.
* **[Bootstrap 4.5.2](https://getbootstrap.com/)**
  * Open-source CSS framework directed at responsive, mobile-first front-end web development
* **[Font Awesome](https://fontawesome.com/)**
  * All icons are from Font Awesome
* **[Materialize Icons](https://materializecss.com/icons.html)**
  * Used on Account, search and shopping cart.
* **[Google Fonts](https://fonts.google.com/)**
  * Roboto Condensed was the font used in this project
* **[Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)**
  * AWS SDK to allow the use of AWS S3 Buckets
* **[AWS S3](https://aws.amazon.com/s3/)**
  * AWS's Simple Storage Service provides 'buckets' to store static and media files for the site, as Heroku doesn't allow persistent ones.
* **[Heroku](https://www.heroku.com/)**
  * Cloud-based web hosting service for dynamic websites.

## Testing

### W3C Validation Services

* ```Attribute with not allowed on element img at this point```
  * Had a typo in img: ```with``` instead of ```width```, changed and fixed.
* ```An img element must have an alt attribute, except under certain conditions.```
  * Fixed missing ```alt``` attribute to img.
* ```No space between attributes.```
  * Fixed the space between attributes

### W3C Link Checker

* No errors, all links working properly. Only two links were not able to be tested by the tool. Here's the console log:

  ```info Line: 322 https://www.facebook.com/
       Status: (N/A) Forbidden by robots.txt
       The link was not checked due to robots exclusion rules. Check the link manually.
       info Line: 319 https://www.twitter.com/
       Status: (N/A) Forbidden by robots.txt
       The link was not checked due to robots exclusion rules. Check the link manually.
  ```

  * Both links were tested manually and working.
  
### CSS Validation service

* All errors were from vendor and third party errors and css issues.

## Non-automated testing

### Links

* All links, were checked manually to ensure that all pages were being opened/redirected correctly.
* All footer social icons were checked as well, to make sure they were opening on a new tab.

### Login

* Tried to access all other parts of the site without being logged in to see if the views were correctly secured.
* Accessed with normal user account and with super user to see if the correct links were shown in the navbar and on the site.
* Typed incorrect credentials in order to see if the correct error message was given to the user.
* Tried to login without any text in the input fields to test the validation and feedback message to the user, on both username and password.
* Tested sign up link, to see if it was redirected correctly to register page.
* Tested all links after the user is logged in.

### Register

* Typed username/email that existed already in the database to see if the feedback message was given to the user.
* Typed without any text to see if the form validation was working and the appropriate messaging was delivered to the user.
* Typed only username to test the validation to avoid creating accounts without user name.
* Typed only password to avoid creating accounts without any passwords and the correct message was given to the user.  
* Typed a different email address from the email confirmation field, to see if it was validating correctly before creating the account, the same was done for password and password confirmation as well.

### Logout

* Checked if the correct navbar options were displayed correctly after logout by checking if the user was authenticated or not. The same process was done by logging out from a super user account as well.
* Tested all links after being logged out to see if everything was redirected correctly.

### Product management

* Tried to add products without filling any details, to test if it was letting creating "empty" products in the database.
* Tried to add a product without filling the required fields to see if the validation was working correctly.
* Tried to add rating above 5, to test the validation that only allows to a max of 5.
* Tried to add the product with and without image to see if the product image selected was correct, and in case of no images to display the noimage.png
* Tested Cancel button to see if it was redirecting correctly to products
* Tested Add Product after all validations above.
* Notifications worked correctly after adding each product with the correct information.

### Add News

* Tried to add posts without filling any details, to test if it was letting creating "empty" posts in the blog.
* Tried to add a post without filling the required fields to see if the validation was working correctly.
* Tried to add a post with and without image to see if the product image selected was correct in case of no images to display the noimage.png
* Tested Cancel button to see if it was redirecting correctly to News.
* Tested Add Post after all validations above.
* Notification displayed the correct information when a post was added.

### My Profile

* Made several purchases with different products and see if they were logged correctly in the order history.
* Logged out with different users and logged back in to see if they were being displayed correctly
* Updated every field individually to test if it was updating correctly the delivery information.
* Update information button was posting information correcty while updating each field.

### Edit Products

* Edited every entry, to see if all the information was saving correctly to the database.
* Opened manually the "edit" games page link without a user being authenticated to avoid a non-user to edit the information on an user's account.

### Delete Products

* Delete task was tested several times with different users logged in, to see if the correct games were being deleted for a single user, and not for all users.
* Tested the delete task on results and results_genre to check if everything was being redirected correctly.
* Several combinations of modal delete confirmation, were tested to make sure the game wasn't being deleted by choosing the incorrect option.

### Edit Posts

* Tried to remove the information already submitted to see if the form validation was working and to see if it was letting me add a post without any information.
* Tested by adding a post to all categories to see if they were working correctly.
* Tested individually every input form, to see if all information was being correctly updated.
* Added posts with and without images to see if the condition was working properly by displaying the noimage.png when there's no image.
* Cancel button tested to see if it was being redirected correctly.
* Edit post button worked for every update I tested above.

### Delete posts

* Create several posts to see if was working correctly and deleting the correct post ID.
* Logged in and logged out to see if they were only being removed from session or permanentely.
* Delete button worked for every test above.

### Shopping bag

* Checked if the message "Your bag is empty" was being displayed while there was no items in it. And tested the "Back" button that redirects to the product list.
* Added several products to see if it was being tracked correctly
* Tested updating the quantity with only one item in the bag, then tested with several items and updated them invidualy to see if it was updating correctly each product. The same test was done for the delete button to see if it was removing the products from the shopping bag correctly.
* Tested incrementation on both buttons to see if it was adding the correct value. Tried to add more than the max of products allowed to see if the condition was working correctly.
* Back button tested to see if it was redirecting correctly to products page.
* Checkout button was working correctly placing orders and connecting to stripe.
* Tried to access checkout page without having any products in the bag, to see if the correct message/notification was presented to the user.
* Tested if by removing all products the message "Your bag is empty" would show up.
* For every change and update and removal the notifications were displaying the correct information.

### Navbar

* All categories were tested to see if they were being redirected correctly and showing the correct products per category.

### Search bar

* Tested search bar by using different keywords to see if it was able to find those keywords in the database.
* Tried search without any input text, to see if the appropriate message was being displayed to the user.
* Tested by searching a non existant product, to see if the message of "0 Products found" was being displayed.

### Product details

* Tested if it was possible to add more items than the max allowed.
* Tested if both quantity buttons would be disabled when they reach the max amount.
* Tested back button to see if it was being redirected to products.
* Add to bag button was working correctly by adding a item with the correct quantity.
* Tested adding the same item several times, to see if it was incrementing correctly and updating the shopbag with the correct quantity.
* Every test with quantitiy was double checked in the shopping bag, to make sure the correct information was displayed on both sides.
* Notifications were displaying the correct information while adding items and different quantities.

### Post Details

* Tested if the edit and delete buttons showed up as a super user. Logged in as a normal user as well to see if they were not showing.
* Back button is working as well redirecting correctly to the news page

### Notifications

* All notifications were checked while making all tests above showing the correct information.

### Tested Devices

* Apart from using the dev tools to see if the site was responsive across different resolutions, I've tested all features on the following devices:
  * One Plus 7 pro
  * Fire HD 10
  * Ipad mini 4
  * Iphone 11
  * Macbook Pro 13"
  * Windows 10 desktop

### Tested Browsers

* To ensure browser compatibility I've tested all features above on the following browsers:
  * Chrome
  * Firefox
  * Safari

## Deployment

### Running this project locally

These instructions will be for [Visual Studio Code](https://code.visualstudio.com/), as the project was developed using this code editor.

#### Requirements

* [Visual Studio Code](https://code.visualstudio.com/)
* [Git](https://git-scm.com/downloads)
* [Python 3](https://www.python.org/)
* [Stripe](https://stripe.com/) account
* [pip](https://pypi.org/project/pip/)

After you have everything installed, start by cloning the project from GitHub:

* Go to [GitHub repository](https://github.com/Brainvibe/ms4_pcstore).
* Under the repository name, click the green "Clone or download" button.
* In the Clone with HTTPs section, copy the clone URL for the repository.
* Open the terminal in your IDE.
* Change the current working directory to the location where you want the cloned directory to be created.
* Copy paste the following command:

```git clone https://github.com/Brainvibe/ms4_pcstore```

The repository is now cloned.

* Install the requirements needed to run the project from the terminal using the following command:

```pip3 install -r requirements.txt```

* Next we'll migrate the models into the database using the following command:
 ```python3 manage.py migrate```

* Next create a super user account using the command:
```python3 manage.py createsuperuser```

* Now to run the project just type ```python manage.py runserver``` in the terminal and it will now run locally.

### Deployment to Heroku

To deploy this project to Heroku, follow these steps:

* Log into [Heroku](https://dashboard.heroku.com/).
* From the main dashboard, select the **New** dropdown, then select **Create new app**.
* Give your app a unique name, and select the region you wish to deploy to.
* After the app is created, select **Deploy** from the top of the page, and scroll down to **Deployment Method**.
* Select **GitHub** as the method of deployment.
* Log in using your **Github credentials**.
* Select your username, and search for the reposity in the **repo-name** box.
* Select **Connect** on the repository you wish to connect to.
* Under **Manual deploy**, select the branch you wish to deploy, and hit **Deploy Branch**.
* After the application is built, select **Settings** from the top of the page.
* Select **Reveal Config Vars**.
* Add the config keys for:

```
 AWS_ACCESS_KEY_ID
 AWS_SECRET_ACCESS_KEY
 DATABASE_URL
 SECRET_KEY
 STRIPE_PUBLIC_KEY
 STRIPE_SECRET_KEY
 STRIPE_WH_SECRET
 USE_AWS
```

* Select **More** from the top right of the page, and select **Restart all dynos**.

The project is now deployed.

## Credits

### Content

* All product details text were copied from [Overclockers Uk](https://www.overclockers.co.uk)

### Media

* Main photo from [Pexels](https://www.pexels.com/)
* All product images were downloaded from [Overclockers Uk](https://www.overclockers.co.uk)

### Acknowledgements

I received inspiration for this project, and based the code, from Code Institute's Full Stack Frameworks

As always, I want to thank my mentor [Victor Miclovich](https://github.com/miclovich) for his great knowledge and experience with valuable feedback in our mentoring sessions.

## Disclaimer

### All content for educational use only
