package lib

import "math"

func DigitsInNum(num int) int {
	if num == 0 {
		return 1
	}

	if num < 0 {
		num = -num
	}

	return int(math.Floor(math.Log10(float64(num)))) + 1
}
