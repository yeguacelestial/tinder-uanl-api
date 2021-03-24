<div align="center">
  <img src="https://raw.githubusercontent.com/yeguacelestial/tinder-uanl-mobile/main/assets/project_logo.png"/>
  <img src="./assets/tinderuanlapi.png" width="30%"/>
  <br><br>

  <img src="https://img.shields.io/badge/by-%40YeguaCelestial-blue"/>

  <img src="https://github.com/yeguacelestial/tinder-uanl-api/workflows/tests/badge.svg"/>

  <h1 align="center"><i>Alentando la flama del amor.</i></h1>
</div>

## Description

This API is consumed by an external React Native app.

## Features

- [x] Sign in with school e-mail
- [x] User model: create custom fields.
  
  Each user object should have the following key-value pairs:
  ```javascript
    {
      email_address: string,
      first_name: string,
      last_name: string,
      profile_pictures: [string array],
      about_me: string,
      sex: string,
      age: int,
      orientation: string,
      last_seen: Date,
      location: string,

      school_dependency_data: {
        job_title: string,
        office_location: string
      },

      liked_by: [
        {
          email_address: string
        },
      ],

      has_liked: [
        {
          email_address: string
        },
      ],

      suggested_candidates: [
        {
          email_address: string
        },
      ],

    }
  ```

- [ ] Create chat functionality.