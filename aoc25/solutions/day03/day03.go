package day03

import (
	"github.com/carlegbert/advent-of-code/aoc25/lib"
)

func joltageForBank(bank string, n int) int {
	counter := make(map[int]int)
	nums := make([]int, len(bank))
	windowSize := 1 + len(bank) - n
	for i, c := range bank {
		num := int(c) - '0'
		nums[i] = num
	}
	for i := range windowSize {
		counter[nums[i]]++
	}

	consumed := -1
	unavailable := windowSize
	result := 0
	counted := 0

	for counted < n {
		for needle := 9; needle >= 0; needle-- {
			count, _ := counter[needle]
			if count == 0 {
				continue
			}

			result *= 10
			result += needle
			consumed++
			counted++

			for nums[consumed] != needle {
				counter[nums[consumed]]--
				consumed++
			}
			counter[needle]--

			if unavailable < len(nums) {
				counter[nums[unavailable]]++
				unavailable++
			}
			break
		}
	}

	return result

}

func SolveP1(inputPath string) int {
	result := 0
	for s := range lib.GetLines(inputPath) {
		result += joltageForBank(s, 2)
	}

	return result
}

func SolveP2(inputPath string) int {
	result := 0
	for s := range lib.GetLines(inputPath) {
		result += joltageForBank(s, 12)
	}

	return result
}
