package models

import (
	"gorm.io/gorm"
)

type User struct {
	gorm.Model
	Name        string `json:"name"`
	Surname     string `json:"surname"`
	Password    string `json:"password"`
	PhoneNumber int32  `json:"phoneNumber"`
	Birthday    string `json:"birthday"`
}
