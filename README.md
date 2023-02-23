# My-Digital-Portfolio-Website
1 Usability
  This assignment mainly uses the Bootstrap framework to realize the Personal digital portfolio
website, and cooperates with javascipt, css and other technologies to provide users with a beautiful
and practical interface. My digital portfolio website is a complete dynamic website with
many perfect functions. The webpage is also deployed on openshift and can be directly accessed
through the URL link. 
  Entering the home page of the website is my personal information display
page. On the right side of the homepage, my personal information will be displayed, including
my skills, work experience, etc., and you can quickly understand my personal information
through the display bar on the right. The website implements the account login function. Before
logging in, the function of using the mailbox to register is also realized. In terms of login and
registration, a lot of small functions have been implemented. For example, administrators can
delete users or user passwords. Similarly, when users use their own accounts, they can upload
avatars, post messages, etc., with A perfect account experience.
  The most important thing is the article publishing section located in the middle of the homepage,
which is also an essential function of the personal website. I myself can publish the website
in the website for other users to read.
  This can include the following news information, technical
blogs, and my personal skills display, etc., which is equivalent to multi-dimensional display
of personal information in the form of articles. In the article, a lot of effort has been spent to
improve this function. For example, the number of reading visits and likes of the article will be
displayed and updated in real time, which has strong usability.
  More importantly, a very practical function is that each account can comment on the article
below the article. Similarly, I can also reply to comments myself, which is a very valuable and
practical function. Related to this is that both comments and replies will have message prompts,
that is, when someone sends you a message, you can receive a prompt on your homepage to
tell you that someone has replied or commented on you, which is also very practical.
  It is worth mentioning that when publishing an article, you can use markdown to write the article, and at
the same time, you can add tags to the article and search for the text, so that you can quickly
check the article you want to read.
2 Security
  User data is the most important property of many websites, and it is very important to
ensure the security of user data. Therefore, some work has been done on the security of the
website to improve the data security of the website. Deleting data is very dangerous, and it
will cause irreversible loss if done wrong. Therefore, we hope to impose some restrictions on
the operator, such as only the user can log in and the user must be the user to perform the
delete operation. First of all, this can be limited by extracting database account information
and comparing. Furthermore, in the development process, in order to prevent CSRF attacks,
certain security work has been done. A CSRF attack is also a cross-domain request forgery
attack. 
  A CSRF attack can be simply understood as: the attacker steals your identity and sends
a malicious request in your name. Take deleting an article as an example: the user logs in to
website A, the browser records the session and keeps the login status, and the user accidentally
opens the evil attacking website B without logging out, attacking website B Malicious code is
implanted in the page, and a request to delete the article is quietly sent to website A. At this
time, the browser mistakenly thinks that the user is doing the operation, and thus successfully
executes the deletion operation. Due to the browser’s same-origin policy, CSRF attackers can’t
get the actual content of your login data, but they can trick the browser into making malicious
requests attach the correct login data.
  The specific security policy is to delete articles using the POST method and verify the csrf
token. The general process is: when a user visits the site, there is a hidden field ‘csrf_token‘ in
the form that the website feeds back to the user. This value is randomly generated on the server
side and is different every time. 
  Before the backend processes the POST request, the background
of the website will verify whether the ‘csrf_token‘ in the requested cookie is consistent with the
‘csrf_token‘ in the form. If they match, the request is legal, otherwise the request may come
from a CSRF attack, and a 403 server access forbidden is returned.
3 Conclusion
  In general, my digital portfolio website has a certain degree of usability and security. In terms
of practicality, it realizes functions such as user registration and login, posting articles, deleting
articles, posting comments, prompting notifications, etc. It is safe and convenient, and it defends
against csrf attacks With sql injection attack, etc., it is practical, safe and fully functional.
4 Appendix A: list of advanced functionality
  Registration and account login
  Use Markdown to write articles
  Publish and delete articles
  Count the number of views and likes
  Post comments and reply prompts
  Database stores articles and account information
  Sort articles according to time or popularity
  Search article content by keyword
  Display personal information on the homepage
  Defense against csrf attacks and sql injection attacks
5 Appendix B: screenshots of website’s pages
![image](https://user-images.githubusercontent.com/115378528/220857272-fd33659a-5b00-4221-a887-0a34f9bdd4a9.png)
![image](https://user-images.githubusercontent.com/115378528/220857320-2d41ed3c-d1bf-4d19-9021-59aa2af5a288.png)
![image](https://user-images.githubusercontent.com/115378528/220857337-c31b3a57-47c2-4666-bd0f-5d848a499362.png)
![image](https://user-images.githubusercontent.com/115378528/220857349-1dddde9a-2eb1-4b75-bb97-2289a8f51a2d.png)
![image](https://user-images.githubusercontent.com/115378528/220857397-055d2520-6ec1-490b-96c8-7eb61a5342cf.png)
![image](https://user-images.githubusercontent.com/115378528/220857415-275daf9d-c74c-419a-a45c-6206e53b044f.png)
![image](https://user-images.githubusercontent.com/115378528/220857445-a59f452b-ce32-42c0-a57f-66599b98cadb.png)
![image](https://user-images.githubusercontent.com/115378528/220857461-a49538da-e547-4968-82bd-bd2f6aa205c8.png)
![image](https://user-images.githubusercontent.com/115378528/220857475-ab19969b-16cd-439a-b3b1-3781a69ab586.png)
![image](https://user-images.githubusercontent.com/115378528/220857491-299235a7-d63a-4f7a-9d23-5a5c39bc650a.png)
