# Pound/Euro tracker
Small flask web app that shows the currency rate on a graph


### Installation

* Clone the repo:

`git clone https://github.com/patillacode/pound-euro-tracker.git`

* Move into the repo folder:

`cd pound-euro-tracker`

* Create a virtual environment ([mkvirtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/)):

```mkvirtualenv pound-euro-tracker```

* Activate the virtualenv:
```workon pound-euro-tracker```

* Install requirements:

    * `pip install -r requirements.txt`

* _You are ready to execute the code!_

------------

### Usage
* Run `python application.py`
* go to `localhost:4040/` in your browser

------------

### Update

* To update the displayed data you will need to hit `http:127.0.0.1:4040/populate/<from _date>/`
* `<from_date>` should follow the following format: `YEAR-MONTH-DAY` like `2017-05-30`

This will take some time to update the database with data retrieved via `http://fixer.io/` API

------------


### Demo
[Live Demo](http://currency.patilla.es/)

------------

### Attribution ###
-------------------
I use [Flask](https://github.com/pallets/flask) as a python web framework - Thanks to [pallets](https://github.com/pallets/) and all who collaborated.

I use [Chart.js](https://github.com/chartjs/Chart.js) as a javascript lib for data representation - Thanks to [chartjs](https://github.com/chartjs) and all who collaborated.

I use [tinydb](https://github.com/msiemens/tinydb) as a document oriented database - Thanks to [msiemens](https://github.com/msiemens/) and all who collaborated.

I use [fixer.io](https://github.com/hakanensari/fixer-io/) as a currency rates api - Thanks to [hakanensari](https://github.com/hakanensari/) and all who collaborated.