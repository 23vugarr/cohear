package config

import (
	"github.com/gin-gonic/gin"
	"log"
)

type Server struct {
	AppUrl string
	Db     *Database
	Router *gin.Engine
	JwtKey []byte
}

func NewServer() (*Server, error) {
	// loading environment variables
	env := NewEnv()
	log.Println("Env variables loaded...")

	// connecting to the database
	db, err := NewDatabase(env.DatabaseUrl)
	if err != nil {
		return nil, err
	}
	// assigning db to server's db
	log.Println("Connected to the database...")

	router := gin.Default()

	return &Server{
		AppUrl: env.AppUrl,
		Db:     db,
		Router: router,
		JwtKey: []byte(env.JwtSecret),
	}, nil
}

func (s *Server) Run() error {
	err := s.Router.Run(s.AppUrl)
	if err != nil {
		return err
	}

	return nil
}
