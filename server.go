package main

import (
	"fmt"
	"net/http"
	"strings"
    "io"
    "strconv"
	"log"
    //"encoding/json"
)

type obstacle struct {
	x int
	y int
    value int
}

func ProcMaps(s string) (int,int) {
    start1 := strings.Index(s, ":")
    end1 := strings.Index(s, ",")
    subs1 := s[start1+1:end1]
    subs1= strings.Trim(subs1, " ")
    row, err1 := strconv.Atoi(subs1)
    if err1 != nil {
		log.Fatal("ProcMaps: ", err1)
	}
    //fmt.Println(row)
    
    subs2 := s[end1+1:]
    start2 := strings.Index(subs2, ":")
    end2 := strings.Index(subs2, "}")
    subs2 = subs2[start2+1:end2]
    subs2= strings.Trim(subs2, " ")
    col, err2 := strconv.Atoi(subs2)
    if err2 != nil {
		log.Fatal("ProcMaps: ", err2)
	}
    //fmt.Println(col)
    return row,col
}

func Handler(w http.ResponseWriter, r *http.Request) {
    // This handler will run for all types of HTTP request, but we can use r.Method to 
    // determine which method is being used and validate the request based on this.
    if r.Method == http.MethodGet {
        io.WriteString(w, "This is a get request")
    } else if r.Method == http.MethodPost {
        fmt.Println("This is a post request")
        len := r.ContentLength
        body := make([]byte, len)
        r.Body.Read(body)
        path := r.URL.Path
        operate := strings.Contains(path, "maps")
        if operate == true{
            //fmt.Println(operate)
            fmt.Println(string(body))
            R,C := ProcMaps(string(body))
            fmt.Println(R)
            fmt.Println(C)
        res := "201 Created" + string(body)
        io.WriteString(w, res)
        }
        
        operate = strings.Contains(path, "start")
        if operate == true{
            fmt.Println(string(body))
            s1,s2 := ProcMaps(string(body))
            fmt.Println(s1)
            fmt.Println(s2)
            res := "201 Created" + string(body)
            io.WriteString(w, res)
        }
        operate = strings.Contains(path, "goal")
        if operate == true{
            fmt.Println(string(body))
            g1,g2 := ProcMaps(string(body))
            fmt.Println(g1)
            fmt.Println(g2)
            res := "201 Created" + string(body)
            io.WriteString(w, res)
        }
    } else {
        io.WriteString(w, "This is a " + r.Method + " request")
    }
}

func main() {
    // Create a basic http example to demonstrate example
    http.Handle("/", http.HandlerFunc(Handler))
    http.ListenAndServe(":3000", nil)
}

