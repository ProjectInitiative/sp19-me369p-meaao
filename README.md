# MEAAO

>Released under the [MIT License](./LICENSE.txt).  
>Copyright &copy; 2019 Andrew Gu, Annie Tsai, Kyle Petryszak

**Institution:** The University of Texas at Austin  
**Semester:** Spring 2019  
**Course:** M E 369P #18169 (Application Programming for Engineers)  
**Professor:** Mitchell Pryor  
**Team Members:** Andrew Gu, Annie Tsai, Kyle Petryszak  
**Assignment:** Final Project

## Objective

Our team is planning on creating a website for the Mechanical Engineering Academic Advising Office (MEAAO). The Python package Django was chosen because the class is based upon learning Python. As students at The University of Texas at Austin, the members of our team became aware of the office's need for a way to better communicate with students, and to keep track of events using a sort of "ticketing" system.

## Key Deliverables

 1. **Website:** Provide a functioning website that demonstrates our knowledge of Django and at minimum some functionality for continued development. The website should leverage Django to serve dynamically-generated pages, persist data in a database, and allow for user authentication. The key features of the website are tickets that will keep track of students' visits, a centralized appointment system for students to schedule a visit with an advisor, and a permissions system.
 2. **Documentation:** Given the short timeframe of this project, it may not be able to program a fully-functional website that meets all of the requirements to be implemented at the office itself. We would like to generate some amount of documentation that helps potential future developers to better understand the the system. Documentation should also be clear enough that non-development users of the system should be able to answer basic questions about website usage by consulting it.

## Roles

| Member | Roles |
| --- | --- |
| Andrew Gu | frontend/backend integration, backend logic, code review |
| Annie Tsai | project management and direction, unauthenticated pages |
| Kyle Petryszak | coordination with MEAAO, frontend UI, authenticated pages |

Our team expects to share and interchange roles and responsibilities, although the expected primary roles of each team member are tabulated above.

## Installation

>Installation instructions assume that [Git](https://git-scm.com/) and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) are installed

 1. Clone this repository
    ([Reference](https://help.github.com/en/articles/cloning-a-repository))

    ```bash
    git clone git@github.com:a-gu/sp19-me369p-meaao.git
    cd sp19-me369p-meaao
    ```

 2. Create a Heroku remote
    ([Reference](https://devcenter.heroku.com/articles/git#for-a-new-heroku-app))

    ```bash
    heroku create
    ```

    Or add an existing Heroku remote
    ([Reference](https://devcenter.heroku.com/articles/git#for-an-existing-heroku-app))

    ```bash
    heroku git:remote -a YOUR_HEROKU_APP_NAME
    ```

 3. Push to the Heroku remote to deploy
    ([Reference](https://devcenter.heroku.com/articles/git#deploying-code))

    ```bash
    git push heroku master
    ```

 4. Attach a PostgresSQL or other SQL database to your Heroku app
    ([Reference](https://devcenter.heroku.com/articles/managing-add-ons#creating-an-add-on))

    >A tier different from `hobby-dev` may be used on non-free plans

    ```bash
    heroku addons:create heroku-postgresql:hobby-dev
    ```

 5. Set up environment variables
    ([Reference](https://devcenter.heroku.com/articles/config-vars))

    >These environment variables should be set as config vars on Heroku if deploying to Heroku  
    >For local development, a `.env` file may be used (do not add to VCS)

    - `SECRET_KEY` the [secret key](https://docs.djangoproject.com/en/2.2/ref/settings/#secret-key) used by Django primarily for signing and encrypting data
    - `DATABASE_URL` if not already set, points to the SQL server instance and includes authentication details so Django can connect

## Running Locally

>These steps assume that [Python](https://www.python.org/), [pipenv](https://pypi.org/project/pipenv/), and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  are installed

 1. Follow most of the steps from "[Installation](#installation)", although a local SQL server may be used, or the `DATABASES` variable in [settings.py](./meaao/meaao/settings.py) may be changed to use a SQLite file

 2. Install dependencies and launch a shell with the Python interpreter in the virtual environment

    ```bash
    pipenv install
    pipenv shell
    ```

 3. Start the local server using the Heroku CLI to launch it locally
    ([Reference](https://devcenter.heroku.com/articles/heroku-local))

    ```bash
    heroku local web-local
    ```
