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
 
| URL | HTTP Method | Purpose | Purpose | Request Body | Success Response Code | Authentication/Authorisation |
| ---    | ----------- | ------- | ------- | ------------ | --------------------- | ---------------------------- |
|     |              |         |        |              |                       |                              |
|/projects/  |GET| Display all projects |  N/A         |        200       |                       |                              |
| /projects/:id |GET      |  Return a project by id  |      N/A   |     200         |
|/projects?is_open=True             |            GET                  |Return projects is open
|  N/A   |       200      |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
|     |             |         |         |              |                       |                              |
 
 
 
### DB Schema
![]( {{ ./relative/path/to/your/schema/image.png }} )

