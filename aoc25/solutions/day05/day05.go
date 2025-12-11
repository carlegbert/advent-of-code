package day05

import (
	"log"
	"strconv"
	"strings"

	"slices"

	"github.com/carlegbert/advent-of-code/aoc25/lib"
)

func parseInput(s string) ([]lib.IntRange, []int64) {
	parts := strings.Split(s, "\n\n")
	rangesRaw := strings.Split(strings.TrimSpace(parts[0]), "\n")
	ranges := make([]lib.IntRange, len(rangesRaw))
	for i, rr := range rangesRaw {
		x := strings.Split(rr, "-")
		left, err := strconv.ParseInt(x[0], 10, 64)
		if err != nil {
			log.Fatalf("Error parsing %s", x[0])
		}
		right, err := strconv.ParseInt(x[1], 10, 64)
		if err != nil {
			log.Fatalf("Error parsing %s", x[1])
		}
		ranges[i] = lib.IntRange{
			Left:  left,
			Right: right + 1,
		}
	}

	numsRaw := strings.Split(strings.TrimSpace(parts[1]), "\n")
	nums := make([]int64, len(numsRaw))
	for i, nr := range numsRaw {
		x, _ := strconv.ParseInt(nr, 10, 64)
		nums[i] = x
	}

	return ranges, nums
}

func SolveP1(inputPath string) int {
	ranges, nums := parseInput(lib.GetString(inputPath))
	result := 0
	for _, n := range nums {
		for _, r := range ranges {
			if r.HasNumber(n) {
				result += 1
				break
			}
		}
	}

	return result
}

func SolveP2(inputPath string) int {
	uncombinedRanges, _ := parseInput(lib.GetString(inputPath))
	combinedRanges := make([]lib.IntRange, 0)

	for len(uncombinedRanges) > 0 {
		n := len(uncombinedRanges) - 1
		r := uncombinedRanges[n]

		combined := false
		for i, cr := range combinedRanges {
			c, ok := cr.Combine(r)
			if !ok {
				continue
			}

			combined = true
			combinedRanges = slices.Delete(combinedRanges, i, i+1)
			uncombinedRanges[n] = c
			break
		}

		if combined {
			continue
		}

		combinedRanges = append(combinedRanges, r)
		uncombinedRanges = uncombinedRanges[0:n]
	}

	result := 0
	for _, r := range combinedRanges {
		result += int(r.Right - r.Left)
	}

	return result
}
