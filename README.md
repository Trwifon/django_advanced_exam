Link to Azure deployment - https://fishermanpoint-dxcugshpghgga0cq.italynorth-01.azurewebsites.net/


Setup project  FishermanPoint
I know this is not the right place for this information but, at this moment, I don't see any other way to send it.

Clone the repository
Install requirements.txt
Create database and run migrations
Create superuser

To create a user through the application, you need to select a group. For this reason, in advance through the admin panel, the superuser must create:

Group ‘fishermen’ with the following rights:
Room | room | Can add room

Group ‘clubs’ with the following rights:
Competition | competition | Can add competition

Group ‘moderator’ with the following rights:
Account | user | Can delete user
Account | user | Can view user
Message | message | Can delete message
Message | message | Can view message
Room | room | Can delete room
Room | room | Can view room
Competition | competition | Can delete competition
Competition | competition | Can view competition

Run the project

Through the application, you can now create:

Users from the ‘fishermen’ group, who have the right to create:
room
message

Users from the ‘clubs’ group, who have the right to create:
competition

Through the admin panel, a superuser can authorize a user by including him in the ‘moderator’ group and making him ‘staff’. As ‘staff’, this user can delete all:
‘users’
’rooms’
‘messages’
‘competitions’


.env
SECRET_KEY = django-insecure-7(u_g@g0mb06vr=-_kx_n603=+nwd%sd@q)vycz1&7d*4-(27z
DEBUG = False
ALLOWED_HOSTS = 127.0.0.1
CSRF_TRUSTED_ORIGINS = https://127.0.0.1
DB_NAME = fisherman_point
DB_USER = postgres
DB_PASSWORD = Proba123+
DB_HOST = 127.0.0.1
DB_PORT = 5432
CLOUD_NAME = dyrqae7cf
API_KEY = 527941524498955
API_SECRET = Waqmgvnw__SKT8Uh5pm3JV5wimU

