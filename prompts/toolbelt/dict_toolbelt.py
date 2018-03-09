# Add and change data here #####################################################################
genre_names                 = ['general', 'sci-fi', 'fantasy', 'thriller']
piece_type_names            = ['person', 'place', 'thing', 'scenario']
prompt_piece_names          = ['Retired Captain', 'A Market', 'A Computer', 'Something has been lost']
prompt_piece_description    = ['description 1', 'description 2', 'description 3', 'description 4']
###############################################################################################


def messy_append(to_return, to_append):
    edited_to_return = to_return

    for item in to_append:
        edited_to_return.append(item)

    return edited_to_return


def build_prompt_piece(passed_dict, index):
    to_return = dict(name='', description='', type='', genre='')
    to_return['name'] = passed_dict['name'][index]
    to_return['description'] = passed_dict['description'][index]
    to_return['type'] = passed_dict['type'][index]
    to_return['genre'] = passed_dict['genre']
    return to_return


def create_test_dict_instance():
    # this is a !#$%@ mess and will need to be fixed. for now it works
    # In retrospect, I should have maybe done the manually

    # Building Genres
    genre_dict = dict(name=[])
    genre_dict['name'] = genre_names
    # Building piece types
    piece_type_dict = dict(name=[])
    piece_type_dict['name'] = piece_type_names

    # Building prompt pieces
    prompt_piece_dict = dict(name=[], description=[], type=[], genre='')
    prompt_piece_dict['name'] = prompt_piece_names
    prompt_piece_dict['description'] = prompt_piece_description
    prompt_piece_dict['type'] = messy_append(prompt_piece_dict['type'], piece_type_dict['name'])
    prompt_piece_dict['genre'] = genre_dict['name'][2]

    # Building built prompt
    built_prompt_dict = dict(name='a built prompt', person='', place='', thing='', scenario='')
    built_prompt_dict['person'] = build_prompt_piece(prompt_piece_dict, 0)
    built_prompt_dict['place'] = build_prompt_piece(prompt_piece_dict, 1)
    built_prompt_dict['thing'] = build_prompt_piece(prompt_piece_dict, 2)
    built_prompt_dict['scenario'] = build_prompt_piece(prompt_piece_dict, 3)

    # Building full dict for return
    dict_to_return = dict(genre='', piece_type='', prompt_piece='', built_prompt='')
    dict_to_return['genre'] = genre_dict
    dict_to_return['piece_type'] = piece_type_dict
    dict_to_return['prompt_piece'] = prompt_piece_dict
    dict_to_return['built_prompt'] = built_prompt_dict

    return dict_to_return
