sumOfPowers :: Integer -> Integer
sumOfPowers n = sum [k^k | k <- [1..n]]
