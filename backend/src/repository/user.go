package repository

import (
	"backend/src/models"
	"backend/src/utils"
	"errors"
	"gorm.io/gorm"
	"time"
)

type UserRepo struct {
	Db *gorm.DB
}

func NewUserRepo(db *gorm.DB) *UserRepo {
	return &UserRepo{
		db,
	}
}

func (u *UserRepo) CreateUser(name, surname, password string, phoneNumber int32, birthdate time.Time) error {
	user := models.User{
		Name:        name,
		Surname:     surname,
		Birthday:    birthdate,
		PhoneNumber: phoneNumber,
		Password:    password,
	}
	res := u.Db.Create(&user)
	if res.Error != nil {
		return res.Error
	}

	return nil
}

func (u *UserRepo) LoginUser(phoneNumber int32, password string) error {
	var user models.User

	_ = u.Db.First(&user, "phone_number = ?", phoneNumber)
	if user.Password == "" {
		return errors.New("no such user")
	}
	res := utils.CheckPasswordHash(password, user.Password)
	if !res {
		return errors.New("password is not correct")
	}

	return nil
}
