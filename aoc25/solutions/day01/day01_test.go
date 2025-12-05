package day01_test

import (
	"testing"

	"github.com/carlegbert/advent-of-code/aoc25/solutions/day01"
)

const inputPath = "example.txt"

func TestSolveP1(t *testing.T) {
	expected := 3

	result := day01.SolveP1(inputPath)

	if result != expected {
		t.Errorf("SolveP1(%s) failed, got: %d, want: %d", inputPath, result, expected)
	}
}

func TestSolveP2(t *testing.T) {
	expected := 6

	result := day01.SolveP2(inputPath)

	if result != expected {
		t.Errorf("SolveP2(%s) failed, got: %d, want: %d", inputPath, result, expected)
	}
}
