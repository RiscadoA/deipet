# DEIPet

A project made for the selection stage of my application to a
[DEI]([https://dei.tecnico.ulisboa.pt/]) scholarship at
[Instituto Superior Técnico](https://tecnico.ulisboa.pt/en/).
This project was developed using Django and Bootstrap. It is built on top of the
PetStore API, hosted by DEI.

## Testing locally

This project can be tested using `docker` and `docker-compose`. Before testing,
a `.env` file needs to be created which defines both `SECRET_KEY` and
`AUTH_TOKEN:` the Django secret key used and the authorization token used on the
PetStore API. To test the project, run `docker-compose up` on the project's root
directory.

You can also test this without `docker`. The python dependencies are listed on
the file `requirements.txt`. They can be installed using
`pip install -r requirements.txt`. The SECRET_KEY and AUTH_TOKEN environment
variables must be set and then the project can be run using
`python manage.py runserver`.

## Authors

- Ricardo Antunes - [RiscadoA](https://github.com/RiscadoA)