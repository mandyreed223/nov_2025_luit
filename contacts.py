
contacts = {
    'number': 4,
    'students':
        [
            {'name':'Winifred Sanderson', 'email':'winifred@example.com'},
            {'name':'Mary Sanderson', 'email':'mary@example.com'},
            {'name':'Sarah Sanderson', 'email':'sarah@example.com'},
            {'name':'Michael Myers', 'email':'michael@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])