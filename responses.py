from random import choice, randint

import Snap_News
import card_effect


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'eh bien, quel silence...'
    elif 'salut' in lowered or 'bonjour' in lowered or 'hey' in lowered:
        return 'Bonjour !'
    elif 'jette un dé' in lowered:
        return f'Vous obtenez {randint(1, 6)} !'
    if ('cache' in lowered and 'semaine' in lowered) or ('coffre' in lowered and 'honneur' in lowered) or 'spotlight' in lowered:
        return "**" + Snap_News.character_1 + "**\n" + Snap_News.img_chr1 + "\n**" + Snap_News.character_2 + "**\n" + Snap_News.img_chr2 + "\n**" + Snap_News.character_3 + "**\n" + Snap_News.img_chr3
    if "!effet " in lowered:
        return card_effect.get_card_effect((lowered[8:]))
    else:
        return choice(['Je ne comprends pas...',
                       'De quoi parlez vous ?',
                       'Pourriez-vous répéter autrement ?'])
