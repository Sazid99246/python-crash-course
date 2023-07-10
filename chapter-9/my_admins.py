from admin import Admin

sazid = Admin("sazidul", "islam", 23, "Dhaka, Bangladesh", "sheikhmdsazidulislam@gmail.com", "sazid991")
sazid.show_privileges()  # This will display the admin privileges
sazid.privileges.privileges = ["can add post", "can edit post", "can delete post", "can add user", "can remove user", "can ban user", "can update user profile", "can make a group", "can delete group", "can update group status", "can remove any member from any group"]
sazid.show_privileges()  # This will display the updated admin privileges
