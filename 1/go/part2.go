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

func readFile(fname string) (incr_counter int, err error) {
	incr_counter = 0
	b, err := ioutil.ReadFile(fname)
	if err != nil {
		return incr_counter, err
	}
	lines := strings.Split(string(b), "\n")
	for i := 0; i+3 <= len(lines[:len(lines)-2]); i++ {
		// TODO this is ugly, maybe a fun over a range?
		na, erra := strconv.Atoi(lines[i])
		if erra != nil {
			return incr_counter, erra
		}
		nb, errb := strconv.Atoi(lines[i+1])
		if errb != nil {
			return incr_counter, errb
		}
		nc, errc := strconv.Atoi(lines[i+2])
		if errc != nil {
			return incr_counter, errc
		}
		nd, errd := strconv.Atoi(lines[i+3])
		if errd != nil {
			return incr_counter, errd
		}
		if (na + nb + nc) < (nb + nc + nd) {
			incr_counter++
		}
	}
	return incr_counter, nil
}

func main() {
	defer elapsed("run")()
	incr_counter, err := readFile("input.txt")
	if err != nil {
		panic(err)
	}
	fmt.Println(incr_counter)
	PrintMemUsage()
}
