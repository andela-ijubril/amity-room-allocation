#amity-room-allocation

#####this solutions randomly allocate people to offices and living spaces based on conditions 


```
Offices prepopulated are: 'Carat', 'Anvil', 'Crucible', 'Kiln', 'Forge', 'Foundry', 'Furnace', 'Boiler', 'Mint', 'Vulcan'
Living Spaces prepopulated are: 'topaz', 'silver', 'gold', 'onyx', 'opal'
```
```

The Conditions are:

1. No staff should be allocated to Living spaces
2. Living spaces should not exceed 4 persons
3. office allocation should not exceed 6 persons

```
######Format of input files
The input into this Script can be found in the input.txt file where the input format can be viewed or seen below:

```
ANDREW PHILLIPS	FELLOW	Y
MATTHEW CONNOR	STAFF
JOHN ADEWALE	FELLOW	N
IYANU ALIMI		FELLOW	Y
AHMED AKUBE		STAFF
```


###Running the script

To run the Script run
```
$ python main.py
```
To display the result in an output file
```
$ python main.py > output.txt
```

To run the tests
```
$ python -m unittest discover tests

