package main

import (
	"backend/src/config"
)

// entry point to the backend application
func main() {
	// creating the server
	server := config.NewServer()

	// running the server
	err := server.Run()
	if err != nil {
		return
	}
}
