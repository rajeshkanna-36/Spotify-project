from app.auth.password import hash_password, verify_password

password = "@Rajesh5630"

hashed_password = hash_password(password)
print(hashed_password)

print(verify_password(password, hashed_password))