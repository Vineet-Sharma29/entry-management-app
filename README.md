# entry-management-app

Managing meetings can be difficult sometimes. This web-app tries to handle this problem by taking visitor and host information, and storing the info in backend, along with sending email and mobile-sms notifications.

## Features

- [x] SMS-Notification
- [x] Email Notification
- [X] Check-out email
- [x] Form validation

## Implementation Details

- SMS-Notification using `AWS SNS`
- Email Notification using `Twilio Sendgrid` SMTP API
- Check-out email using `Celery` workers with `Reddis` broker
- Froentend implemented in `VueJS`
- Backend implemented in `Django`
- Form validation and Error handling in frontend and backend


## Tech Stack

- Django
- VueJS
- Django Rest Framework
- Redis
- Celery
- AWS-SNS
- Sendgrid

## Screenshots
![visitor.png](https://github.com/Vineet-Sharma29/entry-management-app/blob/master/docs/1.png)
![host.png](https://github.com/Vineet-Sharma29/entry-management-app/blob/master/docs/2.png)
![confirm.png](https://github.com/Vineet-Sharma29/entry-management-app/blob/master/docs/3.png)
## How To Run EMS

- Install all dependencies for server and client by:-

  - `pip install -r requirements.txt`
  - `cd client/ && npm i && cd ..`

- Then in order to specify API Keys for AWS IAM user and Sendgrid, run following commands:-

  - `cd ems`
  - `mv env.template .env`
  - Enter API Keys in `.env` file

- Run server by running following commands in root folder:-

  - `python manage.py runserver`
  - (In new terminal tab) `celery -A ems worker -l info`
  - (In new terminal tab) `celery -A ems beat -l info`

- Run client by:-
  - `cd client/ && npm run serve`
