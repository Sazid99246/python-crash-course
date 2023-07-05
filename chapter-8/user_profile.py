def build_profile(first, last, **useer_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in useer_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(user_profile)