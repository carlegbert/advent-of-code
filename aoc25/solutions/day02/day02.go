package day02

import (
	"math"
	"strconv"
	"strings"

	"github.com/carlegbert/advent-of-code/aoc25/lib"
)

type Range struct {
	left  int64
	right int64
}

func getRanges(inputPath string) <-chan Range {
	content := lib.GetString(inputPath)
	parts := strings.Split(content, ",")
	ch := make(chan Range)
	go func() {
		defer close(ch)
		for _, part := range parts {
			rangeParts := strings.Split(part, "-")
			left, _ := strconv.ParseInt(strings.TrimSpace(rangeParts[0]), 10, 64)
			right, _ := strconv.ParseInt(strings.TrimSpace(rangeParts[1]), 10, 64)
			ch <- Range{
				left:  left,
				right: right,
			}
		}
	}()

	return ch
}

func numberRepeatsOnce(n int64) bool {
	d := lib.DigitsInNum(n)
	if d%2 == 1 {
		return false
	}
	h := int(d / 2)
	s := int64(math.Pow10(h))
	return n/s == n%s
}

func numberRepeats(num int64, f int) bool {
	h := int64(math.Pow10(f))
	checkme := num % h
	for num > 0 {
		if checkme != num%h {
			return false
		}
		num /= h
	}

	return true
}

func invalidNumbersInRange1(r Range) <-chan int64 {
	ch := make(chan int64)
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

func invalidNumbersInRange2(r Range) <-chan int64 {
	ch := make(chan int64)
	go func() {
		defer close(ch)
		for i := r.left; i <= r.right; i++ {
			d := lib.DigitsInNum(i)
			factors := lib.Factors(d)
			for _, f := range factors {
				if f == d {
					continue
				}

				if numberRepeats(i, int(f)) {
					ch <- i
					break
				}
			}

		}
	}()

	return ch
}

func SolveP1(inputPath string) int {
	ranges := getRanges(inputPath)
	invalidNumbers := lib.FlatMap(ranges, invalidNumbersInRange1)
	return int(lib.ReduceChannel(invalidNumbers, func(acc, val int64) int64 {
		return acc + val
	}, 0))
}

func SolveP2(inputPath string) int {
	ranges := getRanges(inputPath)
	invalidNumbers := lib.FlatMap(ranges, invalidNumbersInRange2)
	return int(lib.ReduceChannel(invalidNumbers, func(acc, val int64) int64 {
		return acc + val
	}, 0))
}
