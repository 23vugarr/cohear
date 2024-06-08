package schemas

type UserLogin struct {
	PhoneNumber int32  `json:"phoneNumber"`
	Password    string `json:"password"`
}
