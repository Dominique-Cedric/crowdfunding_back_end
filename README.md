# Crowdfunding Back End
Rising Athletes
 
## Planning:
### Concept/Name: 
The platform aims to support children in sports by raising funds and incentives for families facing unexpected expenses such as travel and accommodation; sporting gear and fees and levys.
 
### Intended Audience/User Stories
 
1. **Parents of Young Athletes**: Seeking financial assistance for their children's sports-related expenses.
2. **Coaches and Team Managers**: Looking for resources to help families navigate costs and access support.
3. **Community Organizations**: Interested in partnerships or funding opportunities to promote youth sports.
4. **Potential Donors/Sponsors**: Individuals or businesses wanting to contribute to youth sports initiatives.
5. **Youth Athletes**: Kids looking for information and encouragement to pursue sports safely and effectively.
 
User Stories
1. **As a parent**, I want to find funding options to help cover my child’s sports expenses, so I can support their athletic pursuits without financial strain.
2. **As a coach**, I want to access resources and links on health and wellbeing, so I can better support my team’s overall development.
3. **As a community organization representative**, I want to partner with the website for fundraising events, so we can collectively enhance youth sports opportunities.
4. **As a potential donor**, I want to read testimonials from families who have benefited from the support, so I can understand the impact of my contribution.
5. **As a young athlete**, I want to learn about the importance of safety gear and proper uniforms, so I can participate in my sport safely and confidently.
 
### Front End Pages/Functionality
 
Front-End Pages
 
    1. **Home Page**
       - Overview of the mission and services.
       - Call-to-action buttons for donations and support.
    
    2. **About Us**
       - Information about the organization, its goals, and the team behind it.
       - Mission statement and vision.
    
    3. **Fundraising Page**
       - Detailed description of how funds are raised and distributed.
       - Options for individuals to donate or sponsor families.
       - A breakdown of specific costs (e.g., travel, gear).
    
    4. **Support Resources**
       - Links to external resources on health and wellbeing.
       - Guides for parents on managing sports-related expenses.
        
    5. **Contact Us**
       - Contact form for inquiries.
       - Information on social media links and other ways to connect.
 
Functionality
 
    1. **Donation System**
       - Secure payment gateway for online donations.
       - Options for one-time or recurring donations.  
        
    2. **Responsive Design**
       - Mobile-friendly layout ensuring accessibility on all devices.
    
    3. **User Accounts**
       - Ability for users to create accounts to track donations or access exclusive resources.
       - Login functionality for families to share their stories or updates.
    
    4. **Social Media Integration**
       - Share buttons for users to easily share content on social media platforms.
       - Embedded social media feeds showcasing updates and community engagement.
 
    5. Error handling page
        - Login is required
        - Unauthorized - not project owner or admin
        - Bad request - missing field.
    
    
 
 
 
### API Spec
| URL                    | HTTP METHOD | PURPOSE                             | REQUEST BODY                                             | SUCCESS RESPONSE CODE | Authentication/Authorization                                   |
|------------------------|-------------|-------------------------------------|---------------------------------------------------------|-----------------------|-----------------------------------------------------------------|
| /projects/             | GET         | Display all projects                | N/A                                                     | 200                   | N/A                                                             |
| /projects/:id          | GET         | Return a project by id              | N/A                                                     | 200                   | N/A                                                             |
| /projects?is_open=True | GET         | Return projects that are open       | N/A                                                     | 200                   | N/A                                                             |
| /projects/             | POST        | Create a new project                | Project object                                          | 201                   | Login required                                                  |
| /projects/:id          | PUT         | Update the project                  | Project object                                          | 200                   | Login required / Must be the project owner or admin            |
| /projects/:id          | DELETE      | Delete the project                  | N/A                                                     | 200                   | Login required / Must be the project owner or admin            |
| /pledges?is_open=True  | GET         | Get a list of open pledges         | N/A                                                     | 200                   | Login required / Must be the project owner or admin            |
| /pledges/             | GET         | Return all pledges                  | N/A                                                     | 200                   | N/A                                                             |
| /pledges/:id          | GET         | Return a pledge by id               | N/A                                                     | 200                   | N/A                                                             |
| /pledges/             | POST        | Create a pledge                     | Pledge object                                          | 201                   | Login required                                                  |
| /pledges/:id          | PUT         | Update a pledge                     | Pledge object                                          | 200                   | Login required / Must be the project owner or admin            |
| /pledges/:id          | DELETE      | Delete the pledge by id             | N/A                                                     | 200                   | Login required / Must be the project owner or admin            |
| /users/               | GET         | Return all users                    | N/A                                                     | 200                   | Login required / Must be the admin                              |
| /users/:id/           | GET         | Return users by id                  | N/A                                                     | 200                   |                                                                 |
| /users/               | POST        | Sign up                             | `{ "username": "", "password": "" }`                   | 201                   | N/A                                                             |
| /users/login          | POST        | Login                               | User object                                            | 200                   | N/A                                                             |
| /users/:id            | PUT         | Update the user by id              | `{ "id": , "last_login": null, "is_superuser": false, "username": "", "first_name": "", "last_name": "", "email": "", "is_staff": false, "is_active": true, "date_joined": "2024-10-22T04:02:24.300732Z", "groups": [], "user_permissions": [] }` | 200                   | Login required / Must be the project owner or admin            |
| /users/:id            | DELETE      | Delete the user by id              | N/A                                                     | 200                   | Login required / Must be the project owner or admin            |
| api-token-auth/       | POST        | Get User Auth Token                | `{ "username": "", "password": "" }`                   | 200                   | Login required / Must be the project owner or admin            |

 
### DB Schema
https://github.com/Dominique-Cedric/crowdfunding_back_end/blob/main/DB%20Schema.png


### Deployed project 
![image](https://github.com/user-attachments/assets/247768e1-4cbb-439a-b110-9b25400b4f77)

