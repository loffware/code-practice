package main

import "fmt"

// determines the smallest positive number evenly divisible by all numbers from 1 to 20
func main() {
	i := 1
	for true {
		divisible := true
		i += 1
		for j := 1; j <= 20; j++ {
			if i % j != 0{
				divisible = false  //if i % j is not 0, then it is not divisible by that number
			}
		}
		if divisible == true { //so if divisible is still true after 1 through 20, the number matches
			break
		}
	}

	fmt.Println(i)
}
