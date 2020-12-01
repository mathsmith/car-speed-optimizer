# car-speed-optimizer
A simple algorithm that solves Aneo's Cruise Control Problem [here](https://www.codingame.com/training/medium/aneo)

## Overview
If for whatever reason, the link above is broken this was the original problem.
> GOAL:
> 
> You enter a section of road and you plan to rest entirely on your cruise control to cross the area without having 
> to stop or slow down.
> The goal is to find the maximum speed (off speeding) that will allow you to cross all the traffic lights to green.
> 
> Warning: You can not cross a traffic light the second it turns red !
>
> Your vehicle enters the zone directly at the speed programmed on the cruise control which ensures that it does not 
>change anymore.

The code specific details were as follows:

> **Input**
>
> Line 1: An integer `speed` for the maximum speed allowed on the portion of the road (in km / h).
>
> Line 2: An integer `lightCount` for the number of traffic lights on the road.
>
> `lightCount` next lines:
> - An integer distance representing the distance of the traffic light from the starting point (in meters).
> - An integer duration representing the duration of the traffic light on each color.
>
> A traffic light alternates a period of duration seconds in green and then duration seconds in red.
All traffic lights turn green at the same time as you enter the area.
>
> **Output**
>
> Line 1: The integer speed (km / h) as high as possible that cross all the green lights without committing speeding.
> 
> **Constraints**
> - 1 ≤ speed ≤ 200
> - 1 ≤ lightCount ≤ 9999
> - 1 ≤ distance ≤ 99999
> - 1 ≤ duration ≤ 9999

You may notice that some of these variables are slightly renamed in the source code (to follow naming conventions 
in hopes it makes it more readable for you)


## In-Depth Details
Please see my [blog post](https://www.magnusine.com/blog) that shows:
* my process for how I broke down this problem and solved it.
* thoughtful discussion on the mathematics involved in this problem

## `testSuite/` Folder Details
There are 10 test case files, and 1 excel file. 

### Test Case Files
The test case files are text files that are a record of the original test cases provided by Aneo.
The source code written **does not** actively leverage those test case files. They are here for you to be able to reference
them in case the puzzle link above is no longer available, or down.   

### Excel File
This file shows some of the analysis I was doing to verify the patterns and conditions I derived to solve this problem. 
You could, in theory, take some of the test case files' data and put it into the excel file's to see useful results.
