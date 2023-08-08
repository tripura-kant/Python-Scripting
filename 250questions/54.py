def get_formatted_name(first_name, second_name):
    full_name = f"{first_name} {second_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'henry')
print(musician)
