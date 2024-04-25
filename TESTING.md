# Playdate


This file only contains the exstensive testing done to the webpage. All other information regarding the site will be found in [README](README.md).


## PEP8 Linter 

### Playdate

<details>
<summary> Admin
</summary>

![playdateAdmin](documentation/validation/playdate/playdateAdmin.png)
</details>

<details>
<summary> Apps
</summary>

![playdateApps](documentation/validation/playdate/playdateApps.png)
</details>

<details>
<summary> Filter
</summary>

![playdateFilter](documentation/validation/playdate/playdateFilter.png)
</details>

<details>
<summary> Models
</summary>

![playdateModels](documentation/validation/playdate/playdateModels.png)
</details>

<details>
<summary> Permission
</summary>

![playdatePermission](documentation/validation/playdate/playdatePermission.png)
</details>

<details>
<summary> Serializer
</summary>

![playdateSerializer](documentation/validation/playdate/playdateSerializer.png)
</details>

<details>
<summary> Urls
</summary>

![playdateUrls](documentation/validation/playdate/playdateUrls.png)
</details>

<details>
<summary> Views
</summary>

![playdateViews](documentation/validation/playdate/playdateViews.png)
</details>

### Comments

<details>
<summary> Admin
</summary>

![commentAdmin](documentation/validation/comments/commentAdmin.png)
</details>

<details>
<summary> Apps
</summary>

![commentApps](documentation/validation/comments/commentsApps.png)
</details>

<details>
<summary> Models
</summary>

![commentModels](documentation/validation/comments/commentsModels.png)
</details>

<details>
<summary> Serializer
</summary>

![commentSerializer](documentation/validation/comments/commentsSerializer.png)
</details>

<details>
<summary> Urls
</summary>

![commentUrls](documentation/validation/comments/commentsUrls.png)
</details>

<details>
<summary> Views
</summary>

![commentViews](documentation/validation/comments/commentViews.png)
</details>

### Contact

<details>
<summary> Admin
</summary>

![contactAdmin](documentation/validation/contact/contactAdmin.png)
</details>

<details>
<summary> Apps
</summary>

![contactApps](documentation/validation/contact/contactApps.png)
</details>

<details>
<summary> Models
</summary>

![contactModels](documentation/validation/contact/contactModels.png)
</details>

<details>
<summary> Serializer
</summary>

![contactSerializer](documentation/validation/contact/contactSerializer.png)
</details>

<details>
<summary> Urls
</summary>

![contactUrls](documentation/validation/contact/contactUrls.png)
</details>

<details>
<summary> Views
</summary>

![contactViews](documentation/validation/contact/contactViews.png)
</details>

### Review

<details>
<summary> Admin
</summary>

![reviewAdmin](documentation/validation/review/reviewAdmin.png)
</details>

<details>
<summary> Apps
</summary>

![reviewApps](documentation/validation/review/reviewApps.png)
</details>

<details>
<summary> Models
</summary>

![reviewModels](documentation/validation/review/reviewModles.png)
</details>

<details>
<summary> Serializer
</summary>

![reviewSerializer](documentation/validation/review/reviewSerializer.png)
</details>

<details>
<summary> Urls
</summary>

![reviewUrls](documentation/validation/review/reviewUrls.png)
</details>

<details>
<summary> Views
</summary>

![reviewViews](documentation/validation/review/reviewViews.png)
</details>

### DRF API

<details>
<summary> Permission
</summary>

![drfPermissions](documentation/validation/drf/drfPermissions.png)
</details>

<details>
<summary> Serializer
</summary>

![drfSerializer](documentation/validation/drf/drfSerializer.png)
</details>

<details>
<summary> Setting
</summary>

![drfSetting](documentation/validation/drf/drfSetting.png)
</details>

<details>
<summary> Urls
</summary>

![drfUrls](documentation/validation/drf/drfUrls.png)
</details>

<details>
<summary> Views
</summary>

![drfViews](documentation/validation/drf/drfViews.png)
</details>

## Feature Testing

Tests done in DEV mode:

| Page          | User Action   | Expected Result  | Notes            |
|---------------|---------------|------------------|------------------|
| Start page    |               |                  |                  |
|               | Enter api url | welcome message shown | PASS        |
|               | Click on Sign in button | Redirect to sign in page | PASS |
| /playdate     |               |                  |                  |
|               | Enter /playdate in url | All playdates are displayed | PASS |
|               | Filter playdates on date | Display playdates accordig to the date | PASS |
|               | Typing in searchbar | Display playdates accordig to the text | PASS |
|               | Filter playdates on organizer | Display playdates by organizer | PASS |
|               | Typing  in title filter | Display playdates if text match title | PASS |
|               | Typing  in location filter | Display playdates if text match location | PASS |
|               | Filter playdates on parent stay required | Display playdates by parent stay required | PASS |
|               | Filter playdates on sutable age | Display playdates by sutable age | PASS |
|               | Typing  in date filter | Display playdates if text match date | PASS |
|               | Typing  in date is greater than filter | Display playdates if text match date | PASS |
|               | Typing  in date is less than filter | Display playdates if text match date | PASS |
| /playdate (Logged In - User)  |                 |          |  |
|               | After Login | Sign Up button is now logout button | PASS |
|               | After Login | Users name is displayed | PASS |
|               | User sees a create playdate form | logged in user can create a playdate | PASS |
| /playdate/id  |                 |          |  |
|               | Enter /playdate/id in url | One specific playdates is displayed | PASS |
| /playdate/id (Logged In - User)  |                 |          |  |
|               | User sees edit playdate form on own playdates| user can edit their own playdate | PASS |
|               | User sees delete button on own playdates| user can delete their own playdate | PASS |
| /contact      |                 |          |  |
|               | Enter info in contact form | contact form info sends | PASS |
|               | Types in name filter | Display contact forms if text match name | PASS |
| /comments     |               |                  |                  |
|               | Enter /comments in url | All comments are displayed | PASS |
| /comments (Logged In - User)  |                 |          |  |
|               | User sees create comment form | user can make a comment | PASS |
|               | Types in playdate filter | Display comment for that playdate | PASS |
| /comments/id     |               |                  |                  |
|               | Enter /comments/id in url | One specific comments is displayed | PASS |
| /comments/id (Logged In - User)  |                 |          |  |
|               | User sees edit comment form on own comments| user can edit their own comment | PASS |
|               | User sees delete button on own comment| user can delete their own comment | PASS |
| /review     |               |                  |                  |
|               | Enter /review in url | All review are displayed | PASS |
| /review (Logged In - User)  |                 |          |  |
|               | User sees create review form | user can make a review | PASS |
|               | Types in playdate filter | Display review for that playdate | PASS |
|               | Types in username filter | Display reviews from that user | PASS |
| /review/id    |               |                  |                  |
|               | Enter /review/id in url | One specific review is displayed | PASS |
| /review/id (Logged In - User)  |                 |          |  |
|               | User sees edit review form on own review| user can edit their own review | PASS |
|               | User sees delete button on own review| user can delete their own review | PASS |
| /admin        |               |                  |                  |
|               | Enter admin panel | Admin can see all playdates | PASS |
|               | Enter admin panel | Admin can create playdates | PASS |
|               | Enter admin panel | Admin can edit playdates | PASS |
|               | Enter admin panel | Admin can delete playdates | PASS |
|               | Enter admin panel | Admin can see all comments | PASS |
|               | Enter admin panel | Admin can create comments | PASS |
|               | Enter admin panel | Admin can edit comments | PASS |
|               | Enter admin panel | Admin can delete comments | PASS |
|               | Enter admin panel | Admin can see all reviews | PASS |
|               | Enter admin panel | Admin can create reviews  | PASS |
|               | Enter admin panel | Admin can edit reviews  | PASS |
|               | Enter admin panel | Admin can delete reviews  | PASS |
|               | Enter admin panel | Admin can see all contact forms | PASS |
|               | Enter admin panel | Admin can create contact forms  | PASS |
|               | Enter admin panel | Admin can edit contact forms  | PASS |
|               | Enter admin panel | Admin can delete contact  | PASS |
|               | Enter admin panel | Admin can see all users  | PASS |
