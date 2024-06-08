package main

import (
	"backend/src/config"
	"backend/src/handlers"
	"backend/src/handlers/middlewares"
	"backend/src/repository"
)

// entry point to the backend application
func main() {
	// creating the server
	server, err := config.NewServer()

	usrHandler := handlers.NewUserHandler()
	if err != nil {
		return
	}

	userRepo := repository.NewUserRepo(server.Db.Db)

	v1 := server.Router.Group("api/v1")
	{
		v1.POST("/register", usrHandler.Register(userRepo))
		v1.POST("/login", usrHandler.Login(userRepo, server.JwtKey))

		i := v1.Group("/inside").Use(middlewares.AuthMiddleware(server.JwtKey))
		{
			i.GET("/test", usrHandler.Test())
		}
	}

	err = server.Run()
	if err != nil {
		return
	}
}
