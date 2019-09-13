#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `a = 0` -- > O(1)
   `while(a < n * n * n):` --> O(n^3)
       `a = a + n * n` --> O(n)
    
    Overall: O(n) because it will increment n times as long as the condition is met


b)

`sum = 0` 
`for i in range(n):` --> O(n) ...incrementing one every time
    `j = 1` 
    `while j < n:` --> O(log n)
        `j *= 2` --> doubles every time (doesn't grow at linear rate)
        `sum += 1` 

    Overall: O(n log(n)) 


c) def bunnyEars(bunnies): --> how do the parameters change? they change by one each time
        `if bunnies == 0:`
            return 0
        return 2 + bunnyEars(bunnies - 1) --> O(n)

    Overall: O(n)

## Exercise II

n-story building eggs

greater than floor f...broken egg (thrown)
less than floor f ... not broken egg (dropped)

Teeeeccchnically ... being thrown and being dropped are two different things. So if we are looking to determine the value of f such that the number of dropped and the number of broken eggs is minimized...we are looking for a floor that will have  a chance of either being broken OR not broken. 

I would take the height of the building. Divide by two. Test theory. If it breaks, split the floors below in half. If not, split floors above in half. Retest theory...up until you get to a solution you want. 

In CS, this is called binary search and has O(log n) runtime. 



