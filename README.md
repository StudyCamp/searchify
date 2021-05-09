# Searchify  

### Welcome to Searchify!  

This is a backend application developed using Django as a demonstration that allows user to upload, share, and search for images and find other users. 

### Instructions  

The Navbar contains all the features below. Start by registering and logging in. Then you may upload, share, and search for images and user profiles. Enjoy!   

### Searchify App  

#### Functions  
Location: searchify/searchify/searchifyApp/views.py  
1. Upload an image, with content, multiple tags, username, and automatic timestamp.  
2. Store images to a separated location through a configured media root.
3. Display uploaded images by using the urls stored in the database.    
4. Search for other user profiles using substring, display as a list.  
5. Search images by text in content and by multiple tags(characteristics input by user).  
6. Permission/Authentication required for search functions.  
7. Private profile page viewing is (a perk) for registered users only.   
8. Login Authentication, Logout, Register for an account.  

#### Unitest  
Location: searchify/searchify/searchifyApp/tests    
- Tests for forms, urls, and views.  

#### Database Relational Model  
- Tables: User, Post, Tag.  
- Configure migrations to allow customized file storage system
- SQLite database management system.  

#### URL  
- Allow direct access to profile and search results pages through URLs (permission required). 

#### Staticfiles  
- Images folder contains upload images. 
- Simulate a cloud service like S3 for demonstration purposes (dev-local).  
- CSS.  

#### Template  
- HTML, using Django Template Language.  
- Mobile Responsive Bootstrap.  

#### Forms  
- Search, Create, Upload.  

#### Admin  
- Create superuser and manage DB.  

#### venv  
- Utilize virtual environment.  

#### requirements.txt  
- Include dependencies.  