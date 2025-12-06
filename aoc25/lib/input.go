package lib

import (
	"bufio"
	"log"
	"os"
)

func GetLines(inputPath string) <-chan string {
	ch := make(chan string)
	go func() {
		defer close(ch)
		file, err := os.Open(inputPath)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()
		scanner := bufio.NewScanner(file)
		for scanner.Scan() {
			ch <- scanner.Text()
		}
	}()

	return ch
}

func GetString(inputPath string) string {
	contentBytes, err := os.ReadFile(inputPath)
	if err != nil {
		log.Fatal(err)
	}

	return string(contentBytes)
}
