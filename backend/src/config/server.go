package config

import (
	"log"
)

type Server struct {
	Db *Database
}

func NewServer() *Server {
	return &Server{
		Db: nil,
	}
}

func (s *Server) Run() error {
	// loading environment variables
	env := NewEnv()
	log.Println("Env variables loaded...")

	// connecting to the database
	db, err := NewDatabase(env.DatabaseUrl)
	if err != nil {
		return err
	}
	// assigning db to server's db
	s.Db = db
	log.Println("Connected to the database...")

	return nil
}
