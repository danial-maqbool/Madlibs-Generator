import random


def load_story():
    stories = ['One [adjective] morning, [name] found a [adjective1] box on their doorstep.  It was tied with a ['
               'adjective2] ribbon and had a [adjective3] tag that said, "To: [name]".  [Name] [adverb] opened the box '
               'and found a [adjective2] [noun] inside.  It was so [adjective3] that [name] couldn\'t believe their '
               'eyes!  They decided to [verb] it with their [adjective4] friend, [name]. Together, they had a ['
               'adjective] time [verb ending in -ing] with the [adjective] [noun].',
               'The [adjective] school was buzzing with excitement. It was time for the annual talent show!  [Name] '
               'had been practicing their [adjective] [talent] for weeks.  They were a little [adjective], '
               'but also very [adjective] to perform.  When it was their turn, [name] took a deep breath and stepped '
               'onto the [adjective] stage.  The crowd [verb ending in -ed] as [name] [verb ending in -ed] their ['
               'adjective] [talent].  It was a [adjective] performance!  Everyone cheered and [name] felt like a ['
               'adjective] [noun].',
               'On a [adjective] island, there was a rumor of a [adjective] treasure buried somewhere.  [Name] and '
               'their [adjective] dog, [dog\'s name], decided to go on a [adjective] adventure to find it.  They '
               'followed a [adjective] map that led them through a [adjective] jungle and across a [adjective] river. '
               ' Finally, they reached a [adjective] [place].  [Name] [verb ending in -ed] in the spot marked on the '
               'map and discovered a [adjective] chest filled with [adjective] [noun plural].  [Name] and [dog\'s '
               'name] were [adjective] and celebrated their [adjective] discovery.']

    story_titles = ['The Mysterious Box', 'The Talent Show', 'The Lost Treasure']

    selected_story = random.randint(0, len(story_titles))

    return stories[selected_story], story_titles[selected_story]


raw_story, story_title = load_story()

blanks = set()
check = -1

blanks_start = '['
blanks_end = ']'

for i, char in enumerate(raw_story):
    if char == blanks_start:
        check = i

    if char == blanks_end and check != -1:
        blank_word = raw_story[check: i + 1]
        blanks.add(blank_word)
        check = -1

answers = {}

print('For the Story Title: ', story_title)
for blank_word in blanks:
    user_ans = input('Replace ' + blank_word + ' with: ')
    answers[blank_word] = user_ans

filled_story = raw_story
for blank_word in blanks:
    filled_story = filled_story.replace(blank_word, answers[blank_word])

print(filled_story)
