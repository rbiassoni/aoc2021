package main

import (
	"fmt"
	"io/ioutil"
	"runtime"
	"strconv"
	"strings"
	"time"
)

func bToMb(b uint64) uint64 {
	return b / 1024 / 1024
}

// from https://golangcode.com/print-the-current-memory-usage/
func PrintMemUsage() {
	var m runtime.MemStats
	runtime.ReadMemStats(&m)
	// For info on each, see: https://golang.org/pkg/runtime/#MemStats
	fmt.Printf("Alloc = %v MiB", bToMb(m.Alloc))
	fmt.Printf("\tTotalAlloc = %v MiB", bToMb(m.TotalAlloc))
	fmt.Printf("\tSys = %v MiB", bToMb(m.Sys))
	fmt.Printf("\tNumGC = %v\n", m.NumGC)
}

// from https://stackoverflow.com/questions/45766572/is-there-an-efficient-way-to-calculate-execution-time-in-golang/45766707
func elapsed(what string) func() {
	start := time.Now()
	return func() {
		fmt.Printf("%s took %v\n", what, time.Since(start))
	}
}

func readFile(fname string) (movement int, err error) {
	forward := 0
	up := 0
	down := 0
	f, err := ioutil.ReadFile(fname)
	if err != nil {
		return movement, err
	}
	lines := strings.Split(string(f), "\n")
	for i := 0; i <= len(lines[:len(lines)-2]); i++ {
		line_components := strings.Split(string(lines[i]), " ")
		instruction := line_components[0]
		value, err := strconv.Atoi(line_components[1])
		if err != nil {
			return movement, err
		}
		switch instruction {
		case "forward":
			forward += value
		case "up":
			up += value
		case "down":
			down += value
		}
	}
	movement = (down - up) * forward
	return movement, err
}

func main() {
	defer elapsed("run")()
	movement, err := readFile("../input.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(movement)
	PrintMemUsage()
}
