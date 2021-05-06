# Searchify  

### Welcome to Searchify!  

This is a backend application developed using Django as a demonstration that allows user to upload, share, and search for images and find other users.    

### Searchify App  

#### Functions  
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
- Configure to allow migrations for image URLs relating to the image directory.  
- SQLite database management system.  

#### URL  
- Allow direct access to profile and search results pages through URLs (permission required). 

#### Static  
- Images folder contains upload images. 
- Simulate a cloud service like S3 for demonstration purposes.  
- CSS file.  

#### Template  
- html files, using Django Template Language.  

#### Forms  
- Search, Create, Upload.  

#### Admins  
- Create superuser and manage db.  

#### venv  
- Utilize virtual environment.  

#### requirements.txt  
- Include dependencies.  