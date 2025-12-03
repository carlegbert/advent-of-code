package day01

import (
	"bufio"
	"log"
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
	_ = inputPath
	return 0
}
