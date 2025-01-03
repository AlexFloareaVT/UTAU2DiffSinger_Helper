import os
import shutil

def rename_and_clean_files(input_folder):
    """
    Renames files in all subfolders within the input folder based on the embedded Hiragana mapping.
    Deletes any files that do not end with ".wav".

    Args:
        input_folder (str): The path to the main folder containing subfolders with files.
    """

    hiragana_mapping = {
        'あ': 'a',
        'い': 'i',
        'う': 'u',
        'うぇ': 'we',
        'うぃ': 'wi',
        'え': 'e',
        'お': 'o',
        'か': 'ka',
        'が': 'ga',
        'き': 'ki',
        'ぎ': 'gi',
        'く': 'ku',
        'ぐ': 'gu',
        'け': 'ke',
        'げ': 'ge',
        'こ': 'ko',
        'ご': 'go',
        'さ': 'sa',
        'ざ': 'za',
        'し': 'shi',
        'じ': 'ji',
        'す': 'su',
        'ず': 'zu',
        'せ': 'se',
        'ぜ': 'ze',
        'そ': 'so',
        'ぞ': 'zo',
        'た': 'ta',
        'だ': 'da',
        'ち': 'chi',
        'つ': 'tsu',
        'て': 'te',
        'で': 'de',
        'と': 'to',
        'ど': 'do',
        'な': 'na',
        'に': 'ni',
        'ぬ': 'nu',
        'ね': 'ne',
        'の': 'no',
        'は': 'ha',
        'ば': 'ba',
        'ぱ': 'pa',
        'ひ': 'hi',
        'び': 'bi',
        'ぴ': 'pi',
        'ふ': 'hu',
        'ぶ': 'bu',
        'ぷ': 'pu',
        'へ': 'he',
        'べ': 'be',
        'ぺ': 'pe',
        'ほ': 'ho',
        'ぼ': 'bo',
        'ぽ': 'po',
        'ま': 'ma',
        'み': 'mi',
        'む': 'mu',
        'め': 'me',
        'も': 'mo',
        'や': 'ya',
        'ゆ': 'yu',
        'よ': 'yo',
        'ら': 'ra',
        'り': 'ri',
        'る': 'ru',
        'れ': 're',
        'ろ': 'ro',
        'わ': 'wa',
        'を': 'wo',
        'ん': 'N',
        'ヴぁ': 'va',
        'ヴぃ': 'vi',
        'ヴ': 'vu',
        'ヴぇ': 've',
        'ヴぉ': 'vo',
        '・': 'q',
        "'": 'vf',
        'っ': 'xtu',

        # Combinations with small ya, yu, yo:
        'きゃ': 'kya', 'きゅ': 'kyu', 'きょ': 'kyo',
        'しゃ': 'sha', 'しゅ': 'shu', 'しょ': 'sho',
        'ちゃ': 'cha', 'ちゅ': 'chu', 'ちょ': 'cho',
        'にゃ': 'nya', 'にゅ': 'nyu', 'にょ': 'nyo',
        'ひゃ': 'hya', 'ひゅ': 'hyu', 'ひょ': 'hyo',
        'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',
        'ぴゃ': 'pya', 'ぴゅ': 'pyu', 'ぴょ': 'pyo',
        'みゃ': 'mya', 'みゅ': 'myu', 'みょ': 'myo',
        'りゃ': 'rya', 'りゅ': 'ryu', 'りょ': 'ryo',
        'ぎゃ': 'gya', 'ぎゅ': 'gyu', 'ぎょ': 'gyo',
        'じゃ': 'ja',  'じゅ': 'ju',  'じょ': 'jo',
        'ぢゃ': 'ja',  'ぢゅ': 'ju',  'ぢょ': 'jo',
        'びゃ': 'bya', 'びゅ': 'byu', 'びょ': 'byo',

        # Additional entries for small vowel combinations:
        'つぁ': 'tsa', 'つぃ': 'tsi', 'つぇ': 'tse', 'つぉ': 'tso',
        'ふぁ': 'fa', 'ふぃ': 'fi', 'ふぇ': 'fe', 'ふぉ': 'fo',
        'じゃ': 'ja', 'じゅ': 'ju', 'じぇ': 'je', 'じょ': 'jo',
        'ぢゃ': 'ja', 'ぢゅ': 'ju', 'じぇ': 'je', 'ぢょ': 'jo',

        # Small vowel combinations for "by"
        'びぇ': 'bye',

        # Hiragana for "du", "di", "ti", "tu"
        'どぅ': 'du', 'でぃ': 'di', 'てぃ': 'ti', 'とぅ': 'tu',

        # Hiragana for "xye" sounds
        'きぇ': 'kye',
        'みぇ': 'mye',
        'にぇ': 'nye',
        'ぴぇ': 'pye',
        'りぇ': 'rye',
        'ぎぇ': 'gye',
        'ひぇ': 'hye',
        'びぇ': 'bye',

        # Hiragana for "ye"
        'いぇ': 'ye',

        # Added replacements
        'ずぃ': 'zi',  # Hiragana for "zi"
        'しぇ': 'she', # Hiragana for "she"
        'ちぇ': 'che', # Hiragana for "che"
        'すぃ': 'si', # Hiragana for "si"
        'ほぅ': 'hu', # Hiragana for "hu"
        'わぅ': 'wu', # Hiragana for "wu"
        'うぉ': 'wo', # Hiragana for "wo"
    }

    # Sort the mapping by key length in descending order
    sorted_mapping = sorted(hiragana_mapping.items(), key=lambda item: len(item[0]), reverse=True)

    for subdir, dirs, files in os.walk(input_folder):
        for filename in files:
            old_path = os.path.join(subdir, filename)

            # Delete Non-WAV files
            if not filename.lower().endswith(".wav"):
                os.remove(old_path)
                print(f"Deleted: {old_path}")
                continue  # Correctly placed continue

            new_filename = filename
            for hiragana, replacement in sorted_mapping:
                new_filename = new_filename.replace(hiragana, replacement)

            new_path = os.path.join(subdir, new_filename)
            if new_filename != filename:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} -> {new_path}")

if __name__ == "__main__":
    input_folder = input("Enter the input folder path: ")
    
    # Prompt the user for confirmation
    print("It is strongly advised to back up the files you want to convert before running this script.")
    confirmation = input("Are you sure you want to run the script? (Y/N): ")
    if confirmation.lower() in ['y', 'yes']:
        rename_and_clean_files(input_folder)
    else:
        print("Aborting the script.")