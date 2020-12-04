# Membership Function
## Soil Moisture
### Dry
- [0 , 5] -> 1
- [5 , 15] -> (15-value)/10
- [15 , ..] -> 0
### Moist
- [0 , 10] -> 0
- [10 , 20] -> (value-10)/10
- [20 , 30] -> (30-value)/10
- [30 , ..] -> 0
### Wet
- [0 , 10] -> 0
- [10 , 30] -> (value-10)/20
- [30 , ..] -> 1

## Sun Intensity
### Dark
- [0 , 10] -> 1
- [10 , 25] -> (25-value)/15
- [25 , ..] -> 0
### Dim
- [0 , 20] -> 0
- [20 , 35] -> (value-20)/15
- [35 , 50] -> (50-value)/15
- [50 , ..] -> 0
### Bright
- [0 , 40] -> 0
- [40 , 70] -> (value-40)/30
- [70 , ..] -> 1
    
## Leaves
### Few
- ???
- ???
- ???
### Many
- ???
- ???
- ???

# Reference for :
## Moisture 
- https://support.spruceirrigation.com/knowledge-base/what-is-my-target-moisture-level/

## Intensity 
- 

## Leaves