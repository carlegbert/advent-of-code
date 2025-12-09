package day04

import (
	"strings"

	"github.com/carlegbert/advent-of-code/aoc25/lib"
)

type Point struct {
	x int
	y int
}

func grid(inputPath string) [][]rune {
	s := lib.GetString(inputPath)
	lines := strings.Split(s, "\n")
	g := make([][]rune, len(lines))
	for y, line := range lines {
		g[y] = []rune(line)
	}

	return g
}

func neighbors(grid [][]rune, p Point) []Point {
	n := make([]Point, 0)
	for yv := range 3 {
		y := p.y + yv - 1
		if y < 0 || y >= len(grid) {
			continue
		}
		for xv := range 3 {
			x := p.x + xv - 1
			if x < 0 || x >= len(grid[0]) {
				continue
			}

			if xv == 1 && yv == 1 {
				continue
			}

			n = append(n, Point{x: x, y: y})
		}
	}

	return n
}

func SolveP1(inputPath string) int {
	g := grid(inputPath)
	result := 0
	for y, line := range g {
		for x, b := range line {
			if b == '.' {
				continue
			}

			c := 0
			for _, n := range neighbors(g, Point{x: x, y: y}) {
				if g[n.y][n.x] == '@' {
					c++
				}
				if c > 3 {
					break
				}
			}
			if c <= 3 {
				result++
			}
		}
	}

	return result
}

func SolveP2(inputPath string) int {
	changed := true

	result := 0
	g := grid(inputPath)
	for changed {
		changed = false
		for y, line := range g {
			for x, b := range line {
				if b == '.' {
					continue
				}

				c := 0
				for _, n := range neighbors(g, Point{x: x, y: y}) {
					if g[n.y][n.x] == '@' {
						c++
					}
					if c > 3 {
						break
					}
				}
				if c <= 3 {
					changed = true
					g[y][x] = '.'
					result++
				}
			}
		}
	}

	return result
}
