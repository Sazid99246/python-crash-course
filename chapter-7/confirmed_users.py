unverified_users = ['alice', 'brine', 'candace']
confirmed_users = []

while unverified_users:
    current_user = unverified_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user)