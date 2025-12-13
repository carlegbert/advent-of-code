package day06

import (
	"strconv"
	"strings"

	"github.com/carlegbert/advent-of-code/aoc25/lib"
)

func collectNums(inputPath string) [][]int64 {
	s := lib.GetString(inputPath)
	lines := strings.Split(s, "\n")
	lines = lines[0 : len(lines)-1]
	nums := make([][]int64, len(lines))
	for i, line := range lines {
		parts := strings.Fields(line)
		nums[i] = make([]int64, len(parts))
		for j, part := range parts {
			n, _ := strconv.ParseInt(part, 10, 64)
			nums[i][j] = n
		}

	}

	return nums
}

func collectLastLine(inputPath string) []string {
	s := lib.GetString(inputPath)
	lines := strings.Split(s, "\n")
	line := lines[len(lines)-1]
	return strings.Fields(line)
}

func SolveP1(inputPath string) int {
	nums := collectNums(inputPath)
	ops := collectLastLine(inputPath)
	result := int64(0)
	firstLine := nums[0]
	nums = nums[1:]
	for i, op := range ops {
		val := firstLine[i]
		for j := range len(nums) {
			x := nums[j][i]
			if op == "+" {
				val += x
			} else {
				val *= x
			}
		}
		result += val
	}
	return int(result)
}

func SolveP2(inputPath string) int {
	_ = inputPath

	return 0
}
