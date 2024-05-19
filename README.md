# Web Project
# "Quoraii" Forum platform with automated AI-based response capabilities

## Members

- Junyang Shang 24071326
- Zhe Han 23905652    
- Joel(Yuqiao) Qian 24129392
- Junting Yang 24043287

## Technologies and Libraries

- HTML
- CSS
- JavaScript
- jQuery
- AJAX
- Flask
- SQLite
- Python

## External Resources Used in the Project
### CSS References
1. Bootstrap CSS
- Source: Bootstrap CDN
- Version: 5.3.3
- Purpose: Provides styling and layout control throughout the website.
- Integrity & Crossorigin: Ensures the resource is loaded without tampering and CORS policies are respected.

2. Bootstrap Icons
- Source: jsDelivr CDN
- Version: 1.11.3
- Purpose: Provides scalable vector icons for use across the website.

3. Custom CSS
- Source: Loaded dynamically using Flask's url_for function.
- Purpose: Adds specific page styles unique to our website.

### JavaScript References
1. Moment.js
- Source: cdnjs
- Version: 2.30.1
- Purpose: A powerful library for parsing, validating, manipulating, and formatting dates.

2. jQuery
- Source: jQuery CDN
- Version: 3.7.1
- Purpose: Simplifies DOM manipulation, event handling, and Ajax interactions.

3. Bootstrap Bundle JS
- Source: jsDelivr CDN
- Version: 5.3.3
- Purpose: Includes Popper for tooltips and popovers; supports Bootstrap's JavaScript plugins.

4. Custom JavaScript
- Source: Loaded dynamically using Flask's url_for function.
- Purpose: Adds specific functionalities to the webpage.

### Image References
- Website Logo
- Favicon
- User Avatar




## Description

**Quoraii** is an innovative online forum platform where users can post questions and respond to queries posted by others. It integrates a unique AI-powered feature that automatically generates responses to questions, placing these AI responses as the first comment on a post. Users can view the AI-generated answers by refreshing the web page following on-screen prompts. This feature aims to provide immediate assistance and enrich the discussion by offering quick insights or solutions to posed questions.

### Key Features:
- Question & Answer Posting
- Automatically generating random NFT Avatars
- AI-Generated Responses
- Dynamic Refresh Capability
- User Profile Management
- Interactive Dashboard

Quoraii is designed for curious individuals and learners who seek to engage in meaningful discussions and exchange knowledge in a structured and efficient manner. The AI component adds a layer of rapid response that enriches user interaction and satisfaction. 


## Tasks

### Web Pages
- **Home Page**: Displays basic forum information and navigation.
- **Personal Profile Page**: Allows users to view and edit their profiles.
- **Post Details Page**: Shows detailed views of posts and responses.
- **Ranking Page**: Displays rankings of users or posts.
- **New Discussion Page**: Enables users to initiate new discussions.

### Functional Tasks
- **Post Function (Start a Question)**: Enables users to post new questions, a core feature.
- **Reply (Includes AI Automated Reply)**: Facilitates user responses, including an AI-generated reply as the first comment on new posts.
**Search Function**: Allows users to search for posts, replies, and topics within the forum, enhancing navigability and user experience.

### Authentication and User Management
- **Sign-In, Login, and Logout**: Handles user login, registration, and logout, ensuring data security and privacy.

## Route Design 

### Authentication Routes
`/register` (POST): Registers new users by accepting username, email, and password.
`/login` (POST): Authenticates users allowing access to the system based on username and password.
`/logout` (GET, `@login_required`): Logs out the current user and redirects to the home page.

### Content Management and Interaction
`/` (GET): The homepage displaying posts, optionally filtered by category.
`/new-discussion` (GET, POST): Allows users to start new discussions. GET displays the page, and POST handles the creation of a new post.
`/post-details/<int:post_id>`(GET, POST): Displays details of a specific post and allows logged-in users to post comments.
`/user-posts/<username>` (GET): Displays all posts created by a specific user.
`/personal-profile` (GET, POST): Displays and allows updates to the personal profile of the logged-in user.
`/search` (GET): Allows users to search for posts by keywords.

### Gamification and Community Features
`/ranking-page` (GET): Displays a leaderboard based on user credits.

### AI Integration
`/gpt/<int:post_id>` (POST): Generates AI-driven responses for posts using GPT-3.5-Turbo. The route captures a POST request, uses the content of the specified post to generate a response, and updates the post with the AI-generated content. This function begins by posting a placeholder comment to manage user expectations during response generation, then queries the OpenAI API, retrieves the generated content, and updates the comment in the database with the AI-generated response.

## Folder Design

1. `/model.py` db design and connect
2. `/templates` store all the page html
3. `/static` store all the static files
   1. `/js` store all the js the pages use
   2. `/css` store all the css
   3. `img` store all images

## How to run

## Virtual Environment Setup
To ensure a safe and isolated development and testing environment for your application, it's advisable to use Python's virtual environment. Below is a guide on setting up your virtual environment:

### 1. Setting Up a Python Virtual Environment
First, make sure that your working directory contains the requirements.txt file, which is typically located at the root of your project. Then, create a virtual environment by running:

`$ python -m venv venv`

Note: On some systems, `python` may be aliased as `python3`.

### 2. Activating the Virtual Environment
The method to activate the virtual environment depends on your operating system:

For Unix/Linux systems:

`$ source venv/bin/activate`

For Windows systems:

`$ venv\Scripts\activate`

## Installing Dependencies
The dependencies required for the application are listed in the requirements.txt file. To install these dependencies, use the following command:

`$ pip install -r requirements.txt`

Note: On some systems, `pip` may be aliased as `pip3`.

## Launching the Application Server
Once the dependencies are installed, you can start the application server by running:

`$ python app.py`

## How to test

Run unit test by running:

`$ python -m unittest ./test/test_unit.py`

All tests passed if terminal return the following:

..
----------------------------------------------------------------------
Ran 5 tests in 0.379s

OK




## How to use

### 1.Registration and Login

<img src='../cits5505proj2/app/static/img/login-sign-up.png' center height='400'/>

1. User Registration:

- Users click the Sign-up button located in the upper right corner of the webpage.
- They fill out the registration form with their username, email, and password.

2. User Login:

- Users click the Login button and enter their email and password.
- The system checks if the entered credentials match the stored data in the database.
- If the credentials are correct, the user is granted access and logged into the system.
- If a user forgets their password, they can click the "forgot password" button and proceed to reset their password via their registered email.

<img src='../cits5505proj2/app/static/img/forgetpassword.png' center height='400'/>

### 2. Generating NFT Avatars

When users register on the platform, a unique and personalized NFT avatar is automatically generated for them. Here’s a detailed overview of how this feature operates:

- Activation: The avatar generation is automatically triggered when a new user completes the registration process.
- Process: A unique identifier (such as the user’s email address or a randomly generated string) is used to generate a distinctive NFT (Non-Fungible Token) avatar.
- Technology: The platform uses a specific algorithm or service, possibly integrated with blockchain technology, to create and assign the NFT avatar.

### 3. Permission Control
- Users who are not logged in can browse posts but cannot initiate new questions or respond to others.
- When attempting to initiate a question or reply, the system checks the user's login status:
- If not logged in, a message “please login first” is displayed, possibly redirecting to the login page.

<img src='../cits5505proj2/app/static/img/withoutlogin.png' center height='400'/>

- Logged-in users can proceed to post questions and replies normally.


### 4. Search Functionality

- A search box is provided at the top of the site, allowing users to enter keywords to search.
- The system retrieves posts from the database matching the keywords and returns relevant results.


### 5. Starting a Question

On the homepage, there is a prominent yellow "Start a Question" button located on the left side. Here's how it functions:

<img src='../cits5505proj2/app/static/img/question.png' center height='400'/>

- Access: Users can click the yellow "Start a Question" button to initiate posting a question.
- Category Selection: Upon clicking, users are prompted to select a category for their question. The available categories include Maths, Sports, Tech, Movies, and Gaming.
- Post Submission: After selecting the appropriate category and entering their question, users submit the post.

### 6. AI-Generated Answers

This setup not only facilitates user engagement by simplifying the process of asking questions but also enhances the interactive experience by incorporating AI-driven responses, which are displayed immediately after user interaction.

- Default First Reply: The first reply in the comment section under the user's post is automatically generated by an AI.
- User Interaction: Users are prompted to refresh the page after submitting their question.

<img src='../cits5505proj2/app/static/img/airefresh.png' center height='400'/>

-Viewing AI Reply: Upon refreshing, users can see the AI-generated answer as the first comment.

<img src='../cits5505proj2/app/static/img/aianswer.png' center height='400'/>

### 7.Posting a Comment

<img src='../cits5505proj2/app/static/img/comment.png' center height='400'/>


Button Location: The "Post a Comment" button is conveniently placed to the right of the post content, making it easily accessible for users who wish to respond.

- Interaction: Users can click this button to open a comment input field where they can type their response.
- Submission: After typing their comment, users can submit it to be displayed under the post.

This feature promotes user interaction by providing a straightforward and visible means to participate in discussions and share opinions on the forum.


### 8. Features of the Personal Profile Page

<img src='../cits5505proj2/app/static/img/username.png' center height='400'/>

When users click on their username at the top of the webpage, they are redirected to their personal profile page. Here's what users can do on this page:

1. Edit Personal Bio: Users have the option to edit their personal signature or bio, allowing them to share more about themselves or update their information.

<img src='../cits5505proj2/app/static/img/bio.png' center height='400'/>

2. View Posts and Discussions: Users can view a list of all the posts they have made and discussions they have participated in, helping them navigate through their contributions easily.

3. Delete Posts: If needed, users also have the capability to delete any of their posts directly from this page(The button looks like a bin which is on the right of the post), providing control over their content and interactions on the platform.

<img src='../cits5505proj2/app/static/img/deletesymbol.png' center height='400'/>

This personal profile page acts as a central hub for users to manage their identity and interactions within the forum, enhancing user experience by offering control and accessibility.


### 9. Features of the Ranking Page
When users click on the "Ranking" link at the top of the webpage, they can view a leaderboard displaying the scores of all users. Points are awarded based on the number of posts made and the number of discussions a user has participated in. This feature encourages active participation by highlighting the most engaged members of the community.

<img src='../cits5505proj2/app/static/img/ranking.png' center height='400'/>












