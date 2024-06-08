package config

import (
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

	return &Database{
		Db: db,
	}, nil
}
