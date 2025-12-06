package day02

import (
	"math"
	"strconv"
	"strings"

	"github.com/carlegbert/advent-of-code/aoc25/lib"
)

type Range struct {
	left  int
	right int
}

func getRanges(inputPath string) <-chan Range {
	content := lib.GetString(inputPath)
	parts := strings.Split(content, ",")
	ch := make(chan Range)
	go func() {
		defer close(ch)
		for _, part := range parts {
			rangeParts := strings.Split(part, "-")
			left, _ := strconv.Atoi(rangeParts[0])
			right, _ := strconv.Atoi(rangeParts[1])
			ch <- Range{
				left:  left,
				right: right,
			}
		}
	}()

	return ch
}

func numberRepeatsOnce(n int) bool {
	d := lib.DigitsInNum(n)
	if d%2 == 1 {
		return false
	}
	h := d / 2
	s := int(math.Pow10(h))
	return n/s == n%s
}

func invalidNumbersInRange(r Range) <-chan int {
	ch := make(chan int)
	go func() {
		defer close(ch)
		for i := r.left; i <= r.right; i++ {
			if numberRepeatsOnce(i) {
				ch <- i
			}

		}
	}()

	return ch
}

func SolveP1(inputPath string) int {
	ranges := getRanges(inputPath)
	invalidNumbers := lib.FlatMap(ranges, invalidNumbersInRange)
	return lib.ReduceChannel(invalidNumbers, func(acc, val int) int {
		return acc + val
	}, 0)
}

func SolveP2(inputPath string) int {
	_ = inputPath
	return 0
}
