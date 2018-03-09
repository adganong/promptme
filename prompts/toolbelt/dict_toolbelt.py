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
    genre_dict = {
            'name': ['general', 'sci-fi', 'fantasy', 'thriller'],
        }
    piece_type_dict = {
            'name': ['person', 'place', 'thing', 'scenario'],
        }
    prompt_piece_dict = dict(name=['Retired Captain', 'A Market', 'A Computer', 'Something has been lost'],
                             description=['description 1', 'description 2', 'description 3', 'description 4'], type=[],
                             genre='')

    prompt_piece_dict['type'] = messy_append(prompt_piece_dict['type'], piece_type_dict['name'])
    prompt_piece_dict['genre'] = genre_dict['name'][2]

    built_prompt_dict = dict(name='a built prompt', person='', place='', thing='', scenario='')

    built_prompt_dict['person'] = build_prompt_piece(prompt_piece_dict, 0)
    built_prompt_dict['place'] = build_prompt_piece(prompt_piece_dict, 1)
    built_prompt_dict['thing'] = build_prompt_piece(prompt_piece_dict, 2)
    built_prompt_dict['scenario'] = build_prompt_piece(prompt_piece_dict, 3)

    # this may actually be a bad idea?
    dict_to_return = dict(genre='', piece_type='', prompt_piece='', built_prompt='')

    dict_to_return['genre'] = genre_dict
    dict_to_return['piece_type'] = piece_type_dict
    dict_to_return['prompt_piece'] = prompt_piece_dict
    dict_to_return['built_prompt'] = built_prompt_dict


    return dict_to_return