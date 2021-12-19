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

func computeFromFile(fname string) (consumption int, err error) {
	var most_common_seq, least_common_seq string
	f, err := ioutil.ReadFile(fname)
	if err != nil {
		return consumption, err
	}
	lines := strings.Split(string(f), "\n")
	zero_counter := make([]int, len(lines[0]))
	var col_majority_threshold int = len(lines) / 2
	for i := 0; i <= len(lines[:len(lines)-2]); i++ {
		for j, c := range strings.Split(lines[i], "") {
			if c == "0" {
				zero_counter[j] += 1
			}
		}
	}
	for _, count := range zero_counter {
		if count > col_majority_threshold {
			most_common_seq += "0"
			least_common_seq += "1"
		} else {
			most_common_seq += "1"
			least_common_seq += "0"
		}
	}
	mcs, err := strconv.ParseInt(most_common_seq, 2, 64)
	if err != nil {
		return consumption, err
	}
	lcs, err := strconv.ParseInt(least_common_seq, 2, 64)
	if err != nil {
		return consumption, err
	}
	consumption = int(mcs * lcs)
	return consumption, err
}

func main() {
	defer elapsed("run")()
	consumption, err := computeFromFile("../input.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(consumption)
	PrintMemUsage()
}
