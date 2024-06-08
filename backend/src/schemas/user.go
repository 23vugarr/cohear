package schemas

import "time"

type UserLogin struct {
	PhoneNumber int32  `json:"phoneNumber"`
	Password    string `json:"password"`
}

type ProfileInfo struct {
	Name      string    `json:"name"`
	CreatedAt time.Time `json:"createdAt"`
	Streaks   int       `json:"streaks"`
}
