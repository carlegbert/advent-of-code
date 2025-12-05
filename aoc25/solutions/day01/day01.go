package day01

import (
	"bufio"
	"log"
	"math"
	"os"
	"strconv"
)

func rotation(inputPath string) <-chan int {
	ch := make(chan int)

	go func() {
		defer close(ch)
		file, err := os.Open(inputPath)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			line := scanner.Text()
			n, _ := strconv.Atoi(line[1:])
			if line[0] == 'L' {
				n *= -1
			}
			ch <- n
		}

	}()

	return ch
}

func SolveP1(inputPath string) int {
	dial := 50
	count := 0
	for r := range rotation(inputPath) {
		dial += r
		if dial < 0 {
			dial += 100
		}
		dial %= 100
		if dial == 0 {
			count += 1
		}

	}

	return count
}

func SolveP2(inputPath string) int {
	clicks := 0
	dial := 50

	bucket := 0.0
	for r := range rotation(inputPath) {
		newDial := dial + r
		newBucket := math.Floor(float64(newDial) / 100.0)
		if bucket > newBucket {
			clicks += int(bucket - newBucket)
		} else {
			clicks += int(newBucket - bucket)
		}
		// Leaving from zero and going down changes
		// buckets, but is not an actual click, so
		// we accomodate with a little hack.
		if dial%100 == 0 && r < 0 {
			clicks -= 1
		}
		// And the converse- going down and landing on zero
		// _doesn't_ change buckets but _is_ a click.
		if newDial%100 == 0 && r < 0 {
			clicks += 1
		}
		dial = newDial
		bucket = newBucket
	}

	return clicks
}
