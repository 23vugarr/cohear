package models

import (
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Name        string
	Surname     string
	Password    string
	PhoneNumber int32
	Birthday    string
}
