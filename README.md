# Module for calculating and displaying complete information about training according to data from the sensor unit.

## A task
Implement a module according to the OOP methodology for calculating and displaying information
about the past training according to the data from the sensor unit.

## Base class
```python
class Training
```
### Class properties

* action - the main readable action during training (step - running, walking; stroke - swimming);
* duration - the duration of the workout;
* weight — athlete's weight;
* M_IN_KM = 1000 - constant for converting values ​​from meters to kilometers;
* LEN_STEP - the distance that the athlete overcomes in one step or stroke. One step is `0.65` meters, one stroke is `1.38` meters.

### Class methods

* get_distance() - the method returns the value of the distance covered during the training.
```python
# basic calculation formula
step * LEN_STEP / M_IN_KM
```
* get_mean_speed() - method returns the value of the average movement speed during training.
```python
# basic calculation formula
distance / duration
```
* get_spent_calories() - method returns the number of calories burned.
* show_training_info() - method returns a message class object.

## Derived classes
Running class
```python
class Running
```
### Class properties

inherited

### Class methods
override method:
* get_spent_calories() - method returns the number of calories burned.
```python
# calculation formula
(18 * average_speed - 20) * athlete_weight / M_IN_KM * training_time_in_minutes
```
---
---
Walking class
```python
class SportsWalking
```
### Class properties
Added properties:
* height - height

### Class methods
override method:
* get_spent_calories() - method returns the number of calories burned.
```python
# calculation formula
(0.035 * weight + (speed ** 2 // height) * 0.029 * weight) * workout_time_minutes
```
---
---
Pool workout class
```python
class Swimming
```
### Class properties
Added properties:
* length_pool — pool length;
* count_pool - the number of swimming pools.

### Class methods
override method:
* get_mean_speed() - method returns the value of the average movement speed during training.
```python
# calculation formula
pool_length * count_pool / M_IN_KM / training_time
```
* get_spent_calories() - method returns the number of calories burned.
```python
# calculation formula
(speed + 1.1) * 2 * weight
```
## Information message class
```python
class InfoMessage
```
### Class properties
* training_type — training type;
* duration - the duration of the workout;
* distance — distance covered during the workout;
* speed - average speed of movement;
*calories - calories burned during the workout.


### Class methods

* get_message() - method returns a message string.
```python
# output message
# all float values ​​are rounded to 3 decimal places
'Training type: {training_type}; Duration: {duration} hours; Distance: {distance} km; Wed speed: {speed} km/h; Calories burned: {calories}'.
```

## Module functions
```python
def read_package()
```
* The read_package() function takes as input a training code and a list of its parameters.
* The function must determine the type of training and create an object of the appropriate class,
passing to it the parameters received in the second argument. The function must return this object.

---
---
```python
def main(training)
```
The `main()` function must take an instance of the `Training` class as input.

– When executing the `main()` function, the `show_training_info()` method must be called for this instance;
the result of the method execution must be an object of the `InfoMessage` class, it must be stored in the `info` variable.
– For the `InfoMessage` object stored in the `info` variable, the method must be called
which will return a message string with training data; this string must be passed to the `print()` function.