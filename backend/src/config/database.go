package config

import (
	"backend/src/models"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Database struct {
	Db *gorm.DB
}

func NewDatabase(dsn string) (*Database, error) {
	// connecting to the database using dsn
	db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	if err != nil {
		return nil, err
	}

	// conducting orm
	err = db.AutoMigrate(&models.User{})
	if err != nil {
		return nil, err
	}

	return &Database{
		Db: db,
	}, nil
}
