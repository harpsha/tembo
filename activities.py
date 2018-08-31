#!/usr/bin/python3.6.5

# Without directly modifying the data structures, create a script in either
# python or javascript that cycles through all the parents and prints to the
# terminal the proper activities for their child's age group. When there are no
# more activities for that parent, print “Curriculum complete!”..
#
# (Make sure your script accounts for any edge cases in the provided data!)

parents = {
    'Henry': {'childName': 'Calvin', 'age': 1},
    'Ada': {'childName': 'Lily', 'age': 4},
    'Emilia': {'childName': 'Petra', 'age': 2},
    'Biff': {'childName': 'Biff Jr', 'age': 3},
    'Milo': {}
}

activities = [
    {
        'age': 1,
        'activity': [
            'Go outside and feel surfaces.',
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

class color:
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   END = '\033[0m'

for father in parents:
    activities_found = 0
    kid_age = parents[father].get('age')
    print(color.BOLD + "Activities for " + father +"'s kid: " + color.END, end="\n")

    if kid_age:
        for activities_by_age in activities:
            if activities_by_age.get("age") == kid_age:
                activities_found = 1
                print(color.GREEN + "* ", end="")
                print(*activities_by_age['activity'], sep="\n* ", end=color.END + "\n\n")

        if not activities_found:
            print(color.YELLOW + "No activities found!\n" + color.END)

    else:
        print(color.RED + father + " doesn't seem to have a kid!\n" + color.END)



# Want to really shine and show us your chops?  Work in some of these stretch
# goals using any tools or libraries you see fit.
# - Document your creation process with proper git workflow.
# - Personalize the message output to make it more friendly.
# - Allow users to input new activities & parents before executing the script.
# - Print one activity at a time per parent and continue cycling through until
#   all parents have recieved all their activities.
