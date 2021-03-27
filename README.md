[![License: MIT](https://img.shields.io/github/license/vintasoftware/django-react-boilerplate.svg)](LICENSE.txt)

# Ideabox backend

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/www-norma-dev/idea-box-backend)

## Running
### Setup
  (This should not be necessary but is kept here just in case)
- ~~Inside the `backend` folder, do the following:~~
- ~~Create a copy of ``ideabox_backend/settings/local.py.example``:~~
  ~~`cp ideabox_backend/settings/local.py.example ideabox_backend/settings/local.py`~~
- ~~Create a copy of ``.env.example``:~~
  ~~`cp .env.example .env`~~

#### If you are using plain python:
- Create the migrations for `users` app: 
  `python3 manage.py makemigrations`
- Run the migrations:
  `python3 manage.py migrate`

#### If you are using Docker:
- Create the migrations for `users` app:  
  `docker-compose run --rm backend python manage.py makemigrations`
- Run the migrations:
  `docker-compose run --rm backend python manage.py migrate`

### Tools
- Setup [editorconfig](http://editorconfig.org/), [prospector](https://prospector.landscape.io/en/master/) and [ESLint](http://eslint.org/) in the text editor you will use to develop.

### Running the project (without docker)
- Open a command line window.
- `pip3 install -r requirements.txt && pip install -r dev-requirements.txt`
- Go to the `backend` directory.
- `python manage.py runserver`


### Running the project (with docker)
- Open a command line window and go to the project's directory.
- `docker-compose up -d `
To access the logs for each service run `docker-compose logs -f service_name` (either backend, frontend, etc)

#### Celery
- Open a command line window and go to the project's directory
- `workon theprojectname` or `source theprojectname/bin/activate` depending on if you are using virtualenvwrapper or just virtualenv.
- `python manage.py celery`

### Testing
`make test`

Will run django tests using `--keepdb` and `--parallel`. You may pass a path to the desired test module in the make command. E.g.:

`make test someapp.tests.test_views`

### Adding new pypi libs
Add the libname to either requirements.in or dev-requirents.in, then either upgrade the libs with `make upgrade` or manually compile it and then,  install.
`pip-compile requirements.in > requirements.txt` or `make upgrade`
`pip install -r requirements.txt`

### Cleaning example code
Before you start creating your own apps remove the example:
- Run the command `make clean_examples` in order to clean up the example apps from the front and backend.
- Deregister the example app by removing `'exampleapp.apps.ExampleappConfig'` from ``backend/ideabox_backend/settings/base.py``.
- Adjust ``backend/ideabox_backend/urls.py`` to point to your newly created Django app and remove the path configuration that redirects to the deleted example app.

## Deployment 
### Setup
This project comes with an `app.json` file, which can be used to create an app on Heroku from a GitHub repository.

After setting up the project, you can init a repository and push it on GitHub. If your repository is public, you can use the following button:

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy) 

If you are in a private repository, access the following link replacing `$YOUR_REPOSITORY_LINK$` with your repository link.

- `https://heroku.com/deploy?template=$YOUR_REPOSITORY_LINK$`

Remember to fill the `ALLOWED_HOSTS` with the URL of your app, the default on heroku is `appname.herokuapp.com`. Replace `appname` with your heroku app name.

### Sentry

[Sentry](https://sentry.io) is already set up on the project. For production, add `SENTRY_DSN` environment variable on Heroku, with your Sentry DSN as the value.

You can test your Sentry configuration by deploying the boilerplate with the sample page and clicking on the corresponding button.

### Sentry source maps for JS files

The `bin/post_compile` script has a step to push Javascript source maps to Sentry, however some environment variables need to be set on Heroku.

You need to enable Heroku dyno metadata on your Heroku App. Use the following command on Heroku CLI:

- `heroku labs:enable runtime-dyno-metadata -a <app name>`

The environment variables that need to be set are:

- `SENTRY_ORG` - Name of the Sentry Organization that owns your Sentry Project.
- `SENTRY_PROJECT_NAME` - Name of the Sentry Project.
- `SENTRY_API_KEY` - Sentry API key that needs to be generated on Sentry. [You can find or create authentication tokens within Sentry](https://sentry.io/api/).

After enabling dyno metadata and setting the environment variables, your next Heroku Deploys will create a release on Sentry where the release name is the commit SHA, and it will push the source maps to it.

## Linting
- Manually with `prospector` and `npm run lint` on project root.
- During development with an editor compatible with prospector and ESLint.

## Pre-commit hooks
- Run `pre-commit install` to enable the hook into your git repo. The hook will run automatically for each commit.
- Run `git commit -m "Your message" -n` to skip the hook if you need.

## Opinionated Settings
Some settings defaults were decided based on Vinta's experiences. Here's the rationale behind them:

### `CELERY_ACKS_LATE = True`
We believe Celery tasks should be idempotent. So for us it's safe to set `CELERY_ACKS_LATE = True` to ensure tasks will be re-queued after a worker failure. Check Celery docs on ["Should I use retry or acks_late?"](https://docs.celeryproject.org/en/latest/faq.html#should-i-use-retry-or-acks-late) for more info.

## Commercial Support
This project, as other Vinta open-source projects, is used in products of Vinta clients. We are always looking for exciting work, so if you need any commercial support, feel free to get in touch: contact@vinta.com.br

Copyright (c) 2020 Vinta Serviços e Soluções Tecnológicas Ltda.

[MIT License](LICENSE.txt)
