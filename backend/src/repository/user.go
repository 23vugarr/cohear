package repository

import (
	"backend/src/models"
	"backend/src/schemas"
	"backend/src/utils"
	"errors"
	"gorm.io/gorm"
)

type UserRepo struct {
	Db *gorm.DB
}

func NewUserRepo(db *gorm.DB) *UserRepo {
	return &UserRepo{
		db,
	}
}

func (u *UserRepo) CreateUser(name, surname, password string, phoneNumber int32, birthdate string) error {
	var check models.User

	// Define the user struct
	user := models.User{
		Name:        name,
		Surname:     surname,
		Birthday:    birthdate,
		PhoneNumber: phoneNumber,
		Password:    password,
	}

	// Check if a user with the given phone number already exists
	err := u.Db.First(&check, "phone_number = ?", phoneNumber).Error
	if err == nil {
		// User with the phone number already exists
		return errors.New("user with this phone number already exists")
	} else if !errors.Is(err, gorm.ErrRecordNotFound) {
		// An error occurred while querying the database
		return err
	}

	// Create the new user
	res := u.Db.Create(&user)
	if res.Error != nil {
		return res.Error
	}

	return nil
}

func (u *UserRepo) LoginUser(phoneNumber int32, password string) error {
	var user models.User

	err := u.Db.First(&user, "phone_number = ?", phoneNumber).Error
	if err != nil {
		return err
	}
	res := utils.CheckPasswordHash(password, user.Password)
	if !res {
		return errors.New("password is not correct")
	}

	return nil
}

func (u *UserRepo) GetProfileInformation(phoneNumber int32) (*schemas.ProfileInfo, error) {
	var user models.User
	var res schemas.ProfileInfo
	err := u.Db.First(&user, "phone_number = ?", phoneNumber).Error
	if err != nil {
		return nil, err
	}

	res.Name = user.Name
	res.CreatedAt = user.CreatedAt
	res.Streaks = 2
	return &res, nil
}
