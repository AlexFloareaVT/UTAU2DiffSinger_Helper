Thank you for downloading my UTAU to DiffSinger conversion helper! Full disclosure, the scripts were created using a mix of ChatGPT and Google Gemini.

This tool will do two things for you:

- Rename Hiragana filenames to Romaji with a distinction between the vowel N and the consonant n, as well as converting ・ to q and ' to vf which are commonly used for glottal stops and vocal fries in UTAU and DiffSinger respectively.
- Write phonetic transcriptions based on either the filename, or an index.csv

#Things to do before using this tool

Make sure that your folder setup is as follows:

- folders
    - singer1
        - file1.wav
        - file2.wav
        - ...
    - singer2
        - file1.wav
        - file2.wav
        - ...

#Running the tool

Make sure you have Python installed and then open CMD in the this folder and run:

python UTAU2DiffSinger_Helper.py

There's one requirement needed for this tool which is "pandas", which is required to parse csv files, but the script checks for it and installs if it you don't have it.

#Warnings

Do NOT run this script on your original folder of UTAU recordings because it will delete all files that aren't wav, as well as potentially rename them if you use that function and it does NOT create backups so any changes made will be PERMANENT. This also goes for the index.csv, should you choose that option, as it will add an extra row at the top.

#How to use the renamer

If you choose to use the filenames I HIGHLY recommend that you use Hiragana filenames for Japanese voicebanks and use the converter as this keeps n and N separate, as well as converts glottal stops and vocal fries to the most commonly used phonemes. If you use filenames that were already romaji you'll have to edit the vowel N in the filenames to be uppercase, ・ and ' are converted using the renamer regardless of whether it is hiragana or romaji so I advise using that anyway (or edit the filenames yourself). If you have any non-standard hiragana in your filenames you may need to define them in the Hiragana2Romaji.py file under the hiragana_mapping, but I did try and add as many as I could find (no katakana).

#Filename transcriptions

Because of the way that the transcription writer for filenames works, any phonemes that are two or more characters long will be split. There are exceptions to this (ch, sh, ts, dh, th, vf, hh, jh, ng) by default, as well as more if you select English (aa, ah, ao, ax, ae, ay, aw, eh, er, ey, ih, iy, ow, ou, uh, uw) and optional for English are tr and dr.

If you would like to add more exceptions to this, for example if you have a custom phoneme system or a language that isn't English or Japanese, you can do so by editing the "no_space_combinations" section at the top of the Gen_Trans.py file in the scripts folder. I may add other languages to this in the future, but since UTAU phonemes can be a bit weird (symbols and whatnot) I would need a direct conversion chart so that the filenames match the phonemes needed and I don't have time to research that at the moment.

#Index.csv transcriptions

If you choose to use the index.csv transcription method, this works regardless of language or phoneme system, so it may be a better choice for languages that aren't English or Japanese.

This takes an index.csv formatted with filenames in column 1 and the transcriptions in column 2, or formatted as such if you're writing it in a text editor:

filename.extension,transcription

An example of a row in an index.csv is as follows

example.wav,k_a_k_i_k_u_k_e_k_o_n_k_a

Again, make sure to backup your index.csv file as this WILL add an extra row to the top of it.

It will ask you how you want your transcriptions formatted (index.csv only)

1 - Raw Phonemes
2 - Raw Phonemes with SP (recommended)
3 - LabelMakr support (Uppercase phonemes with .)

Once your mode has been chosen it will output txt files with the transcriptions wherever the csv file was

#Creating the base labels

While this tool doesn't create any label files for you, I will explain the next steps you should take.

I HIGHLY recommend that for any language you run SOFA locally, through CMD, instead of through LabelMakr. This is because, at the time of writing, LabelMakr doesn't have an option for the NoneG2P module in SOFA which takes pure phonemes without editing them at all. This is why the filename renamer automatically adds SP to the start and end of the file, and it's recommended to use option 2 with the index.csv transcriptions.

I won't go into how to install SOFA, that can all be found at https://github.com/qiuqiao/SOFA

When you're ready to make the base labels/alignments make sure you use the following script for SOFA:

python infer.py --ckpt [path to the SOFA checkpoint for the language you're using] --g2p NoneG2P --in_format txt

This ensures that it's using the SOFA Model for the language you need, NoneG2P and is reading the txt files as the default for sofa is .lab files.

Once that's done just fix up the label files and you're ready to train!

Thank you for using this tool!