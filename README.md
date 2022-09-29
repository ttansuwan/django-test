# API School & Students - Test

Interview assignment to evaluate how good you are with building APIs with Django.
### Submission
Heroku url: https://agile-waters-63686.herokuapp.com/


## Timeline
| Feature | Date | Estimated time|
|---------|:------:|------:|
|  Setting up git   |   27/09   | 10m |
|  Step 1 - Setup       |    26/09  | 30m |
|  Step 1 - Model    |   26/09   | 15m | 
| Step 2 - DRF Endpoints   | 27/09   | 4hrs |
| Step 3 - Nested Endpoints   | 28/09  | 2hrs |
|  Deploying to Heroku |  29/09 | 3hrs  |
| Additional - Pagination| 29/09 | 20m |


## Usage

### Set up environment 
```bash
pipenv install
pipenv shell
```
### Start django server - dev
```bash
python manage.py runserver
```

## Paths
All path with {pk} are available in GET/PUT/PATCH/DELETE
All path with no specific {pk} are available in GET/POST

### Students
```
/students/ <- Students list
/students/{student_pk}/ <- One student, from {pk}
```

### Schools
```
/schools/ <- Schools list
/schools/{school_pk}/ <- One school, from {pk}
/schools/{school_pk}/students <- Student list of {school_pk} school
/schools/{school_pk}/students/{student_pk} <- Specfic {student_pk} student from {school_pk} school
```