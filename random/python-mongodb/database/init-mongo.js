db.createUser(
    {
        user: "user",
        pwd: "password",
        roles: [
            {
                role: "readWrite",
                db: "mymongodb"
            }
        ]
    }
)

db.createCollection("employees")
db.employees.insertMany(
    [
        {
            "emp_id": 123,
            "firstName": "Keith"
        },
        {
            "emp_id": 124,
            "firstName": "Emma"
        },
        {
            "emp_id": 125,
            "firstName": "Yuri"
        }
    ]
)