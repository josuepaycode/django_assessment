from authentication.models import Administrator

def run():
    try:
        # creating first admin
        Administrator.objects.create({
            "username": "admin@dev.com",
            "email": "admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "Admin"
        })

        Administrator.objects.create({
            "username": "super-admin@dev.com",
            "email": "super-admin@dev.com",
            "password": "J2GkLnAccCHm",
            "name": "SuperAdmin",
            "role": "super_administrator"
        })
    except Exception:
        print('Admins already exists')
    print('Admin and Super created successfully!!')
