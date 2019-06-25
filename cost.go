package main

import (
	"fmt"
	"net/http"
    "bytes"
    "io/ioutil"
)

func main() {
    url := "http://localhost:5000/api/costs"
    fmt.Println("URL:>", url)

    var jsonStr = []byte(`{'i': 0, 'j': 1, 'value': 10.0},
        {'i': 1, 'j': 1, 'value': 10.0},
        {'i': 3, 'j': 0, 'value': 10.0},
        {'i': 3, 'j': 1, 'value': 10.0},
        {'i': 1, 'j': 3, 'value': 10.0},
        {'i': 2, 'j': 3, 'value': 10.0},
        {'i': 3, 'j': 3, 'value': 10.0},
        `)
    req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonStr))
    req.Header.Set("X-Custom-Header", "myvalue")
    req.Header.Set("Content-Type", "application/json")

    client := &http.Client{}
    resp, err := client.Do(req)
    if err != nil {
        panic(err)
    }
    defer resp.Body.Close()

    fmt.Println("response Status:", resp.Status)
    fmt.Println("response Headers:", resp.Header)
    body, _ := ioutil.ReadAll(resp.Body)
    fmt.Println("response Body:", string(body))
}